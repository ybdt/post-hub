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

from panellib.interface import IID_IOpenControlPanel, IOpenControlPanel


CODEC = sys.stdout.encoding
CLSID_COpenControlPanel = string_to_bin('06622D85-6856-4460-8DE1-A81921B41C4B')


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