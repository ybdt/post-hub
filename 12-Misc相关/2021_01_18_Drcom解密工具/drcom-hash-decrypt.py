#!/usr/bin/env python2

def encrypt(each, k):
    array = [28, 57, 86, 19, 47, 76, 9, 38, 66, 95, 28, 57, 86, 18, 47, 76]
    new_each = ord(each) + array[k]
    if new_each > 126:
        new_each = new_each - 126 - 1 + 32
    return chr(new_each)

def main():
    a_passwd = raw_input('please input the hashed passwd: ')
    print a_passwd
    passwd = a_passwd[:-1]
    k = 0
    sum = ''
    for i in passwd:
        for j in range(32, 127):
            if i == encrypt(chr(j), k):
                sum += chr(j)
                break
        k += 1
    print sum

if __name__ == '__main__':
    main()
