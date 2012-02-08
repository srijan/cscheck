#!/usr/bin/env python2
import Queue
import socket
import threading
from netaddr import IPNetwork

socket.setdefaulttimeout(0.05)

def parsing(txt):
    txt=txt.replace('\377', '')
    if txt.find('m') == 0:
        serv_name=txt.split('\0') [1]
        serv_map=txt.split('\0') [2]
        serv_engine=txt.split('\0') [3]
        serv_game=txt.split('\0') [4]
    print '\t\tServer name:', serv_name
    print '\t\tGame:', serv_game, '('+serv_engine+')'
    print '\t\tMap:', serv_map

class ClientThread (threading.Thread):
    def run (self):
        excp = False
        ip = None
        while True:
            if ipPool.qsize() > 0:
                ip = ipPool.get()
            else:
                break
            if ip != None:
                excp = False
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                try:
                    sock.connect((ip, 27015))
                except Exception,e:
                    sock.close()
                    print ip, e
                    break
                sock.send('\377\377\377\377TSource Engine Query\0')
                while 1:
                    try:
                        text=sock.recv(1024)
                    except Exception,e:
                        #print ip + " : " , e
                        excp = True
                        break
                    print ip+" : "
                    text=parsing(text)
                    if not text:
                        break
                    print '[GET]', text
                sock.shutdown(socket.SHUT_RDWR)
                sock.close()
                if not excp:
                    print ' '

subnetList = [
                "172.16.1.0/24",
                "172.16.2.0/24",
                "172.16.3.0/24",
                "172.16.4.0/24",
                "172.16.5.0/24",
                "172.16.6.0/24",
                "172.16.7.0/24",
                "172.16.8.0/24",
                "172.16.9.0/24",
                "172.16.10.0/24",
                "172.16.11.0/24",
                "172.16.12.0/24",
                "172.16.13.0/24",
                "172.16.14.0/24",
                "172.16.15.0/24",
                "172.16.16.0/24",
                "172.16.17.0/24",
                "172.16.18.0/24",
                "172.16.19.0/24",
                "172.16.20.0/24",
                "172.17.1.0/24",
                "172.17.2.0/24"
             ]
ipPool = Queue.Queue(0)


def checkIPs():
    for subnet in subnetList:
        for ip in IPNetwork(subnet).iter_hosts():
            ipPool.put('%s' % ip)

    for x in xrange(100):
        ClientThread().start()

checkIPs()
while True:
    if ipPool.empty():
        print '--End--'
        # write file
        # wait 1 min
        # redo..
        break
