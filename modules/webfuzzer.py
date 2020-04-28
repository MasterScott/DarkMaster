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
print "\033[96m2 \033[93m[\033[92m+\033[93m] \033[91m Drupal\033[91m"
print "\033[96m3 \033[93m[\033[92m+\033[93m] \033[91m php \033[91m"
print "\033[96m4 \033[93m[\033[92m+\033[93m] \033[91m Joomla \033[91m"
print "\033[96m5 \033[93m[\033[92m+\033[93m] \033[91m Random\033[91m\n"


option = input("\033[92m Enter option : ")

if option == 1:
	f = open("wordpressfuzz.txt","r");
	wordpress = raw_input(" Enter Site Name : " )
        print "\n"
	while True:
		add_link = f.readline()
		if not add_link:
			break
		site_link = "http://"+wordpress+add_link
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
    f = open("drupalfuzz.txt", "r");
    drupal = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + drupal+add_link
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
    f = open("phpfuzz.txt", "r");
    php = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + php + add_link
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
    f = open("joomlafuzz.txt", "r");
    Joomla = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + Joomla + add_link
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
    f = open("random.txt", "r");
    random = raw_input(" Enter Site Name : ")
    print "\n"
    while True:
        add_link = f.readline()
        if not add_link:
            break
        site_link = "http://" + random+"/"+ add_link
        site = Request(site_link)
        try:
            response = urlopen(site)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print O + "Avilable : ", site_link    

                        


