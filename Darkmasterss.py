import requests
import json
from urllib2 import *
from platform import system
import sys
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
W  = '\033[0m'
R  = '\033[31m'
G  = '\033[32m'
O  = '\033[33m'
B  = '\033[34m'
P  = '\033[35m'
C  = '\033[36m'
GR = '\033[37m'
T  = '\033[93m'
M = '\033[1;35;32m'

def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
banner = ''' \033[1m \033[91m 
              .======.
              | INRI |
              |      |
              |      |
     .========'      '========.\033[93m
     |   _      xxxx      _   |
     |  /_;-.__ / _\  _.-;_\  |
     |     `-._`'`_/'`.-'     |
     '========.`\   /`========'
              | |  / |
              |/-.(  |
              |\_._\ |
              | \ \`;|
              |  > |/|
              | / // |
              | |//  |
              | \(\  |
              |  ``  |\033[96m
              |      |
              |      |
              |      |
              |      |\033[92m
   \\F3 _  _\\| \//  |// Max  \// 
 ^ `^`^ ^`` `^ ^` ``^^`  `^^` `^ ^
[--------------------] 
[+] Name : D4RKMASTER\033[96m                                  
[+] Version: 3.0 \033[91m                                        
[+] Author : Mr.silent coder \033[93m                            
[+] Facebook: https://facebook.com/f3max \033[95m                
[---------------------------------------]
'''

print banner

def menu():
   print'''
\033[91m 1  \033[93m[\033[96m*\033[93m]\033[92m Link Cracker 
\033[91m 2  \033[93m[\033[96m*\033[93m]\033[92m Robots.txt
\033[91m 3  \033[93m[\033[96m*\033[93m]\033[92m Who Is
\033[91m 4  \033[93m[\033[96m*\033[93m]\033[92m Reverse Ip
\033[91m 5  \033[93m[\033[96m*\033[93m]\033[92m Dns Lookup
\033[91m 6  \033[93m[\033[96m*\033[93m]\033[92m Reverse Dns
\033[91m 7  \033[93m[\033[96m*\033[93m]\033[92m Dns Host Records
\033[91m 8  \033[93m[\033[96m*\033[93m]\033[92m Shared Dns Servers
\033[91m 9  \033[93m[\033[96m*\033[93m]\033[92m Zone Transfer
\033[91m 10 \033[93m[\033[96m*\033[93m]\033[92m IP Locator
\033[91m 11 \033[93m[\033[96m*\033[93m]\033[92m Tcp Port Scan
\033[91m 12 \033[93m[\033[96m*\033[93m]\033[92m HTTP Header Check
\033[91m 13 \033[93m[\033[96m*\033[93m]\033[92m Trace Route
\033[91m 14 \033[93m[\033[96m*\033[93m]\033[92m Ping
\033[91m 15 \033[93m[\033[96m*\033[93m]\033[92m Admin Finter 
\033[91m 16 \033[93m[\033[96m*\033[93m]\033[92m Cms Checker
\033[91m 17 \033[93m[\033[96m*\033[93m]\033[92m Cms Fuzzer
\033[91m 18 \033[93m[\033[96m*\033[93m]\033[92m Url Fuzzer
\033[91m 19 \033[93m[\033[96m*\033[93m]\033[92m About Me
\033[91m 00 \033[93m[\033[96m*\033[93m]\033[92m Exit
'''
slowprint("\033[1;91m  A Warm Welcome to D4RK V1LL10N5 " + " \n\033[1;94m  Special Thanks @Dark Coders " + " \n \033[93m https://www.facebook.com/D4RKV1LL10N5" + " \n \033[1;95m https://www.darkcoders.world " + "\n\033[92m  Network Pentesting tool!" + "\n \033[93m Stay Legal! \033[96m")

menu()

def ext():
    ex = raw_input ('\033[92mContinue/Exit:\033[91m(C/E) ')
    if ex[0].upper() == 'E' :
           print 'Good bye..'
           exit()
    else:
           clear()
           print banner
           menu()
           select()

def  select():
  try:

   option = input("\033[93m[\033[92m Darkmaster \033[93m]: ")

   if option == 1:
       link = raw_input('\nEnter URL: ')
       page_url = "https://api.hackertarget.com/pagelinks/?q=" + link
       craw = urlopen(page_url).read()
       print R + (craw) + R
       ext()


   if option == 2:
       print 'use : http://'
       domain = raw_input('\nEnter Domain -> ')
       txt = domain + "/robots.txt"
       robotxt = urlopen(txt).read()
       print W + (robotxt) + W
       ext()

   if option == 3:
       ip = raw_input('\nEnter Domain or IP Address -> ')
       whois = "http://api.hackertarget.com/whois/?q=" + ip
       who = urlopen(whois).read()
       print B + (who) + B
       ext()

   if option == 4:
       ip = raw_input('\nEnter Domain or IP Address -> ')
       url = "http://api.hackertarget.com/reverseiplookup/?q=" + ip
       craw = urlopen(url).read()
       print P + (craw) + P
       ext()
   if option == 5:
       url2 = raw_input('\nEnter Domain or Ip : ')
       Dns = "http://api.hackertarget.com/dnslookup/?q=" + url2
       craw = urlopen(Dns).read()
       print GR + (craw) + GR
       ext()
   if option == 6:
       url3 = raw_input('\nEnter Domain or Ip : ')
       Dns2 = "https://api.hackertarget.com/reversedns/?q=" + url3
       craw = urlopen(Dns2).read()
       print T + (craw) + T
       ext()
   if option == 7:
       url4 = raw_input('\nEnter Domain  : ')
       Host = "http://api.hackertarget.com/hostsearch/?q=" + url4
       craw = urlopen(Host).read()
       print C + (craw) + C
       ext()
   if option == 8:
       dns2 = raw_input('\nHost Name : ')
       hdns = "http://api.hackertarget.com/findshareddns/?q=" + dns2
       craw = urlopen(hdns).read()
       print O + (craw) + O
       ext()
   if option == 9:
       dom = raw_input('\nEnter Domain : ')
       zone = "http://api.hackertarget.com/zonetransfer/?q=" + dom
       craw = urlopen(zone).read()
       print P + (craw) + P
       ext()
   if option == 10:
       loc = raw_input('\nEnter Ip : ')
       geo = "http://api.hackertarget.com/geoip/?q=" + loc
       craw = urlopen(geo).read()
       print G + (craw) + G
       ext()
   if option == 11:
       port = raw_input('\nEnter Ip : ')
       tcp = "http://api.hackertarget.com/nmap/?q=" + port
       craw = urlopen(tcp).read()
       print P + (craw) + P
       ext()
   if option == 12:
       head = raw_input('\nEnter web address : ')
       http = "http://api.hackertarget.com/httpheaders/?q=" + head
       craw = urlopen(http).read()
       print O + (craw) + O
       ext()
   if option == 13:
       trace = raw_input('\nEnter ip or Domain : ')
       mtr = "https://api.hackertarget.com/mtr/?q=" + trace
       craw = urlopen(mtr).read()
       print W + (craw) + W
       ext()
   if option == 14:
       ping = raw_input('\nEnter ip or Domain : ')
       nping = "https://api.hackertarget.com/nping/?q=" + ping
       craw = urlopen(nping).read()
       print P + (craw) + P
       ext()

   if option == 15:
       print '\033[95m \n Admin page checker \033[95m \n '
       path = os.getcwd()
       os.system('cd ' +  path  + '/modules && python checker.py')
       ext()
   if option == 16:
       link = raw_input('\nEnter URL:\033[96m ')
       URL="https://whatcms.org/APIEndpoint?key=620c898e90cb882dbab6cf32adf1e0690a6725cde9158a5afe4046212d581ac9b3619c&url=" + link

       r = requests.get(url = URL)
       data = r.json()
       name = data['result']['name']
       version = data['result']['version']
       print("\n\033[93mCms Name: \033[91m%s\n\n\033[93mVersion: \033[91m%s" %(name,version))
       ext()

   if option == 17:
       print '\033[95m \n CMS Fuzzer \033[95m \n '
       path = os.getcwd()
       os.system('cd ' +  path  + '/modules && python fuzzer.py')
       ext()

   if option == 18:
       print '\033[95m \n Url Fuzzer \033[95m \n '
       path = os.getcwd()
       os.system('cd ' +  path  + '/modules && python webfuzzer.py')
       ext()

   if option == 19:
       print "D4RK V1LL10N5" 
       print "Name : DARKMASTER\033[92m" 
       print "Version : 3.0 \033[91m" 
       print "------------>"
       print "Author: Mr.silent coder \033[96m"
       print "Facebook : https://facebook.com/f3max  \033[91m"
       print "Youtube : https://www.youtube.com/mrsilentcoder \033[96m"
       print "Facebook : http://facebook.com/D4RKV1LL10N5 \033[96m "
       ext()
       
   if option == 00:
    print "Good bye...!"
  except(KeyboardInterrupt):
    print "\nCtrl + C -> Exiting!!"
select()





