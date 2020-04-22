import os
import requests

HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

header = RED+"""    _      _       _        ___ _         _         
   /_\  __| |_ __ (_)_ _   | __(_)_ _  __| |___ _ _ 
  / _ \/ _` | '  \| | ' \  | _|| | ' \/ _` / -_) '_|
 /_/ \_\__,_|_|_|_|_|_||_| |_| |_|_||_\__,_\___|_|  """

os.system('clear')
print header
print GREEN+" ---------------------------------------------------"
print GREEN+" -                   version 1.0                   -"
print GREEN+" -                author : prhnahmd                -"
print GREEN+" ---------------------------------------------------"
print GREEN+" "

target = raw_input('[-]URL >>'+ RESET+' ')
print " "

f=open('wordlist.txt','r')
content=f.read()
x=content.split('\n')

for i in x:
	url=target+'/'+i
	code=requests.get(str(url)).status_code
	if code== 200:
		print BLUE+">> " +url + GREEN+" [VALID]"
	else:
		print BLUE+">> " +url + RED+" [NOT VALID]"

print RESET+"DONE :)"
