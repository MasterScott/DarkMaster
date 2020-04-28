from urllib2 import Request, urlopen, URLError, HTTPError
class color:

    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


G = '\033[32m'
O = '\033[33m'
C = '\033[36m'

print "\033[96m1 \033[93m[\033[92m+\033[93m] \033[91m Mass finter (small)\033[91m"
print "\033[96m2 \033[93m[\033[92m+\033[93m] \033[91m Top Search (large)\033[91m\n"

option = input("\033[92m Enter option : ")

if option == 1:
	f = open("admin.txt","r");
	link = raw_input(" Enter Site Name : " )
        print "\n"
	while True:
		add_link = f.readline()
		if not add_link:
			break
		site_link = "http://"+link+"/"+add_link
		site = Request(site_link)
		try:
			response = urlopen(site)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print O + "Avilable : ",site_link



if option == 2:
 f = open("mass.txt", "r");
link = raw_input(" Enter Site Name : ")
print "\n"
while True:
    add_link = f.readline()
    if not add_link:
        break
    site_link = "http://" + link + "/" + add_link
    site = Request(site_link)
    try:
        response = urlopen(site)
    except HTTPError as e:
        continue
    except URLError as e:
        continue
    else:
        print O + "Avilable : ", site_link




