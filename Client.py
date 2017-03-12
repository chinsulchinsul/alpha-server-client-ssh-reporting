#!/usr/bin/env python
import time
import re
import socket
import sys
server = "127.0.0.1"
port = 8888
auth_log = '/var/log/auth.log'

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def report(host,port,attempt_count):
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(attempt_count)
        print "Data sent to server"

    except socket.error, msg:
        print "Socket closed %s" % str(msg)
    s.close()

if __name__ == '__main__':
    logfile = open(auth_log,"r")
    loglines = follow(logfile)
    for line in loglines:
        if re.match('.*sshd.*Failed.*',line) is not None:
            report(server, port, '1')