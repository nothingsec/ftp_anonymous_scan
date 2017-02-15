#!/usr/bin/env python
# coding=utf-8
# author:nothing

import ftplib
import optparse
from threading import *
mutexLock = Semaphore(value=1)
def anonLogin(host):
    try:
        print '[*] Scaning host %s ' % str(host)
        ftp = ftplib.FTP(host)
        ftp.login('anonymous','test@test.com')
        ftp.quit()
        mutexLock.acquire()
        print '[*] ' + str(host) + 'FTP Anonymous Logon Succeeded.'
        return True
    except Exception,e:
        mutexLock.acquire()
        print '[!] %s FTP Anonymous Logon Failed.' % str(host)
        return False
    finally:

        mutexLock.release()

def attack(host):
    try:
        hostname = open(host)
        hosts = hostname.readlines()
        for hostss in hosts:
            t = Thread(target=anonLogin,args=(hostss))
            t.start()
    except:
        hostname = host
        anonLogin(host)

def main():
    parser = optparse.OptionParser('usage : -t <target host> or -f <host file>')
    parser.add_option('-t', dest='target_host', type='string')
    parser.add_option('-f', dest='host_file', type='string')
    (options, args) = parser.parse_args()
    host = options.target_host
    hosts = options.host_file
    # print parser.usage
    # if (host == None and hosts != None) or (host != None and hosts == None):
    if host is None or hosts is None:
        print parser.usage
        exit(0)
    attack(host)
if __name__ == '__main__':
    main()