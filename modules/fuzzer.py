from urllib2 import Request, urlopen, URLError, HTTPError
class color:

    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


G = '\033[32m'
O = '\033[33m'
C = '\033[36m'

print "\033[96m1 \033[93m[\033[92m+\033[93m] \033[91m Wordpress \033[91m"
print "\033[96m2 \033[93m[\033[92m+\033[93m] \033[91m Drupal \033[91m"
print "\033[96m3 \033[93m[\033[92m+\033[93m] \033[91m Symphony \033[91m"
print "\033[96m4 \033[93m[\033[92m+\033[93m] \033[91m Sharepoint \033[91m"
print "\033[96m5 \033[93m[\033[92m+\033[93m] \033[91m Php nuke \033[91m"
print "\033[96m6 \033[93m[\033[92m+\033[93m] \033[91m Caobox \033[91m"
print "\033[96m7 \033[93m[\033[92m+\033[93m] \033[91m Coldfusion \033[91m"
print "\033[96m8 \033[93m[\033[92m+\033[93m] \033[91m Magento \033[91m"
print "\033[96m9 \033[93m[\033[92m+\033[93m] \033[91m Joomla \033[91m\n"

option = input("\033[92m Enter option : ")

if option == 1:
	f = open("wordpress.txt","r");
	wordpress = raw_input(" Enter Site Name : " )
        print "\n"
	while True:
		add_link = f.readline()
		if not add_link:
			break
		site_link = "http://"+wordpress+"/"+add_link
		site = Request(site_link)
		try:
			response = urlopen(site)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print O + "Avilable : ",site_link



if option == 9:
    f = open("joomla.txt", "r");
    joomla = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + joomla + "/" + add_link
        site = Request(site_link)
        try:
            response = urlopen(site)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print O + "Avilable : ", site_link

if option == 2:
    f = open("drupal.txt", "r");
    drupal = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + drupal + "/" + add_link
        site = Request(site_link)
        try:
            response = urlopen(site)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print O + "Avilable : ", site_link

if option == 3:
    f = open("symphony.txt", "r");
    symphony = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + symphony + "/" + add_link
        site = Request(site_link)
        try:
            response = urlopen(site)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print O + "Avilable : ", site_link   

if option == 4:
    f = open("sharepoint.txt", "r");
    sharepoint = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + sharepoint + "/" + add_link
        site = Request(site_link)
        try:
            response = urlopen(site)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print O + "Avilable : ", site_link                      

if option == 5:
    f = open("phpnuke.txt", "r");
    phpnuke = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + phpnuke + "/" + add_link
        site = Request(site_link)
        try:
            response = urlopen(site)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print O + "Avilable : ", site_link           

if option == 6:
    f = open("caobox.txt", "r");
    caobox = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + caobox + "/" + add_link
        site = Request(site_link)
        try:
            response = urlopen(site)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print O + "Avilable : ", site_link           

if option == 7:
    f = open("coldfusion.txt", "r");
    coldfusion = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + coldfusion + "/" + add_link
        site = Request(site_link)
        try:
            response = urlopen(site)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print O + "Avilable : ", site_link  

if option == 8:
    f = open("magento.txt", "r");
    magento = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + magento + "/" + add_link
        site = Request(site_link)
        try:
            response = urlopen(site)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print O + "Avilable : ", site_link  


