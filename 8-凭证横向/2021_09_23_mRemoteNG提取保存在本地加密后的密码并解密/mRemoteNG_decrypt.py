#!/usr/bin/env python3


# 标准库
import hashlib
import base64
import argparse
import sys


# 第三方库
from Cryptodome.Cipher import AES


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
    print( "Password: {}".format( plaintext.decode("utf-8") ) )


def main():
    file_name, string_name, password = usage()
    if file_name != None:
        with open(file_name) as fr:
            lines = fr.readlines()
            for line in lines:
                encrypted_data = line.strip("\n")
                encrypted_data = encrypted_data.strip()
                encrypted_data = base64.b64decode(encrypted_data)
                decrypt(encrypted_data, password)
    elif string_name != None:
        encrypted_data = string_name
        encrypted_data = base64.b64decode(encrypted_data)
        decrypt(encrypted_data, password)
    else:
        print("Please use either the file (-f, --file) or string (-s, --string) flag")
        sys.exit(1)


if __name__ == "__main__":
    main()