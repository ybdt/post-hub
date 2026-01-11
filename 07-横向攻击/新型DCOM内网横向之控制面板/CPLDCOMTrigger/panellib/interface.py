from impacket.dcerpc.v5.dcomrt import DCOMCALL, IRemUnknown2
from impacket.dcerpc.v5.dtypes import LPWSTR, DWORD, NULL
from impacket.uuid import string_to_bin
from impacket.dcerpc.v5.rpcrt import DCERPCException
from impacket import hresult_errors

IID_IOpenControlPanel = string_to_bin('D11AD862-66DE-4DF4-BF6C-1F5621996AF1')

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