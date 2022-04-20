#!/usr/bin/env python3


# 标准库
import hashlib
import base64
import argparse
import sys


# 第三方库
from Cryptodome.Cipher import AES
import pandas as pd
'''
pip3.exe install pycryptodomex
pip3.exe install pandas
'''


def usage():
    parser = argparse.ArgumentParser(description="Decrypt mRemoteNG passwords")
    group = parser.add_mutually_exclusive_group()# 保证-f和-s只允许有一个
    group.add_argument("-f", "--file", help="Name of file which containing mRemoteNG password")
    group.add_argument("-s", "--string", help="Base64 string of mRemoteNG password")
    parser.add_argument("-p", "--password", help="Custom password", default="mR3m")

    # 保证只输入程序名，也会输出帮助信息
    if len(sys.argv) < 2:
        parser.print_help(sys.stderr)
        sys.exit(1)# 0为正常退出，1-127为非正常退出
    
    args = parser.parse_args()
    file_name = args.file
    string_name = args.string
    password = args.password
    return file_name, string_name, password


def decrypt(encrypted_data, password):
    salt = encrypted_data[:16]
    associated_data = encrypted_data[:16]
    nonce = encrypted_data[16:32]
    ciphertext = encrypted_data[32:-16]
    tag = encrypted_data[-16:]
    key = hashlib.pbkdf2_hmac("sha1", password.encode(), salt, 1000, dklen=32)

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    cipher.update(associated_data)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return "{}".format( plaintext.decode("utf-8") )


def handle_1(file_name):
    handle_1_name = "tmp-" + file_name.strip(".xml") + ".txt"
    with open(file_name, "r", encoding="UTF-8") as fr:
        with open(handle_1_name, "w", encoding="UTF-8") as fw:
            lines = fr.readlines()
            total_count = len(lines)# 统计原文件一共多少行
            valid_count = 0
            invalid_count = 0
            for line in lines:
                line = line.strip("\n")
                if len( line.split() ) <= 3:
                    invalid_count += 1
                    continue
                else:
                    valid_count += 1# 统计每行分割后大于3段的行数
                    multi_parts = line.split()
                    i = 0
                    for j in multi_parts:
                        if multi_parts[i].startswith("Name"):
                            element = multi_parts[i]
                            fw.write(element + " ")
                        elif multi_parts[i].startswith("Username"):
                            element = multi_parts[i]
                            fw.write(element + " ")
                        elif multi_parts[i].startswith("Password"):
                            element = multi_parts[i]
                            fw.write(element + " ")
                        elif multi_parts[i].startswith("Hostname"):
                            element = multi_parts[i]
                            fw.write(element + " ")
                        i += 1
                    fw.write("\n")
            print( "Total lines are: {}".format(total_count) )
            print( "Valid lines are: {}".format(valid_count) )
            print( "Invalid lines are: {}".format(invalid_count) )
            print("Content write to: {}".format(handle_1_name) )
    return handle_1_name


def handle_2(file_name):
    handle_2_name = "tmp-" + file_name
    with open(file_name, "r", encoding="UTF-8") as fr:
        with open(handle_2_name, "w", encoding="UTF-8") as fw:
            lines = fr.readlines()
            total_lines = len(lines)
            valid_lines = 0
            invalid_lines = 0
            for line in lines:
                line = line.strip("\n")
                if len( line.split() ) < 4:
                    invalid_lines += 1
                    continue
                elif line.split()[2].strip("Password=").strip('"') == "":
                    invalid_lines += 1
                    continue
                else:
                    valid_lines += 1
                    #print(line)
                    fw.write(line + "\n")
            print()
            print( "Total lines are: {}".format(total_lines) )
            print( "Valid lines are: {}".format(valid_lines) )
            print( "Invalid lines are: {}".format(invalid_lines) )
            print("Content write to: {}\n".format(handle_2_name) )
    return handle_2_name


def main():
    file_name, string_name, password = usage()

    if file_name != None:
        handle_1_name = handle_1(file_name)
        handle_2_name = handle_2(handle_1_name)

        name_field = []
        user_field = []
        host_field = []
        pass_field = []
        with open(handle_2_name, "r", encoding="UTF-8") as fr:
            lines = fr.readlines()
            total_lines = len(lines)
            for line in lines:
                encrypted_data = line.strip("\n")
                tmp_list = encrypted_data.split()
                name = tmp_list[0].strip("Name=").strip('"')
                user = tmp_list[1].strip("Username=").strip('"')
                encrypt_pass = tmp_list[2].strip("Password=").strip('"')
                host = tmp_list[3].strip("Hostname=").strip('"')
                encrypted_data = encrypt_pass
                encrypted_data = base64.b64decode(encrypted_data)
                decrypt_pass = decrypt(encrypted_data, password)
                #print( "{} {} {} {}".format(name, host, user, decrypt_pass) )
                name_field.append(name)
                user_field.append(user)
                host_field.append(host)
                pass_field.append(decrypt_pass)
        dataframe = pd.DataFrame( {"Name": name_field, "Hostname": host_field, "Username": user_field, "Password": pass_field} )
        dataframe.to_csv("mPass.csv", mode="w", index=False, sep=",")
        print( "Total lines are: {}".format(total_lines) )
        print("Content write to: mPass.cvs")
    elif string_name != None:
        encrypted_data = string_name
        encrypted_data = base64.b64decode(encrypted_data)
        decrypt(encrypted_data, password)
    else:
        print("Please use either the file (-f, --file) or string (-s, --string) flag")
        sys.exit(1)


if __name__ == "__main__":
    main()