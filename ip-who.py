# This is the free version of ip-who.
# It includes very limited features and
# will only work for 45 requests/min.

# Pro version features:
# cli-argument support increasing speed and stability of the program. Free version is interactive but only 1 req per session
# Search for ip/domains from a file. Will result in faster response and speed in collecting data.
# Include port scan without nmap. This will help you scan for open ports in target without using nmap and return the results in beautiful UI
# Includes shodan search. This will help in banner grabbing and also find osint info
# Find OSINT info using google dorking. Read more at https://github.com/psychoSherlock/ip-who
# And much more. To use ip-who pro, contact the author on twitter: www.twitter.com/psycho_sherlock
import requests
import os
from time import sleep, gmtime, strftime
from datetime import datetime
from terminaltables import AsciiTable
from colorama import Fore, init, Style
from platform import system



init(autoreset=True)


if system()=='Windows':
    os.system("color 0a")

else:
    pass




print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +  """
   _______     _      ____ ______  ___ 
  /  _/ _ \___| | /| / / // / __ \/__ |
 _/ // ___/___/ |/ |/ / _  / /_/ / /__/
/___/_/       |__/|__/_//_/\____/ (_)  
                                                                                
"""+ Fore.RED + Style.BRIGHT + "\nAuthor: " + Fore.GREEN + Style.BRIGHT +  "@psychoSherlock")
print(Fore.RED + Style.BRIGHT + "You are using the free version of IP-WHO.\nThe pro version is much cooler and easy to use. \nIt also includes features like "+ Fore.YELLOW + Style.BRIGHT + "Port Scan, Banner Grabbing with Shodan, OSINT, and Google Dorking (more info on https://github.com/psychoSherlock/ip-who)." + Fore.RED + Style.BRIGHT + "\nBuy it now before the limited offer expires by contacting" +Fore.GREEN+ Style.BRIGHT + " @psycho_sherlock" + Fore.RED + Style.BRIGHT +" on twitter")
#Getting Ip

ip = input("\n[?] Ip or Domain of Target: ")

print("\n" + Fore.MAGENTA + Style.BRIGHT + "[+] Connecting...")
sleep(0.30)

gbr = Fore.GREEN + Style.BRIGHT

dataTable = []

table = AsciiTable(dataTable)

fields = "?fields=status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,mobile,proxy,hosting,query"

try:
    r = requests.get("http://ip-api.com/json/" + ip + fields) # Connecting to API


    def search(comment, data):
        """
        Searches for certain data in
        the request JSON reponse and prints it
        """
        response = r.json().get(data) # Searches for specific data in the returned JSON 
        

        dataTable.append([comment, str(response)])

        return # If return in NOT precent then it will return None.


    def output():
        """
        Prints the data that we want.
        """
        search('Searching For: ','query')
        search('Status: ', 'status')
        search('ISP: ','isp')
        search('Organisation: ', 'org')
        search('Inc: ', 'as')
        search('Country: ', 'country')
        search('Region: ', 'regionName')
        search('District: ', 'district')
        search('City: ', 'city')
        search('Zip: ', 'zip')
        search('Timezone: ', 'timezone')
        search('Latitude: ', 'lat')
        search('Longitude: ', 'lon')
        search('Mobile Connection: ', 'mobile')
        search('Proxy Connection: ', 'proxy')
        search('Hosting Server: ', 'hosting')
        
        print(Fore.GREEN + Style.BRIGHT + "Ip-who? scan report for " + Fore.YELLOW + Style.BRIGHT + r.json().get('query') +  Fore.RESET + " at: "+ Fore.LIGHTMAGENTA_EX + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n" + Fore.RESET + table.table)
        return

    if r.status_code == 200:
        print("\n" + Fore.YELLOW + Style.BRIGHT + "[+] Connected Successfully...")
        
        if r.json().get('status')=='success':
            sleep(0.50)
            print('\n'+ Fore.GREEN + Style.BRIGHT + '[+] Searching...\n')
            sleep(0.70)
            output()
            save = input("\n[?] Save to File? (y OR n) >> ")

            if save.lower()=="y":
                path = input("\n[?] Path to File to Write: ")
                
                try: 
                    op = f = open(path, "a")
                    print(Fore.LIGHTWHITE_EX  + Style.BRIGHT + "\n[+] Writing to File...")
                    f.write("\n\n" + "Ip-who? scan report for " + r.json().get('query') + " at: "+ strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n"+ table.table + "\n")
                    f.close()
                    sleep(0.50)
                    print(Fore.YELLOW + Style.BRIGHT + "\n[+] Saved Successfully in " + path)
                    exit
                
                except FileNotFoundError:
                    print(Fore.RED + Style.BRIGHT +"\n[-] Invalid File")


            elif save.lower()=='n':
                print(Fore.RED + Style.BRIGHT +"\n[-] Quiting...\n")
                exit

            else:
                print(Fore.RED + Style.BRIGHT +"\n[-] Invalid! Quiting...\n")
                exit 

        else:
            sleep(3)
            print('\n'+ Fore.RED + Style.BRIGHT +'[-] Failed while searching! Invalid Ip')
        

    else:
        sleep(3)
        print('\n' + Fore.RED + Style.BRIGHT +'[-] Some ERROR had occured... Please try again later')# change this!!



except requests.exceptions.ConnectionError: 
    sleep(3)
    print('\n'+Fore.RED + Style.BRIGHT +'[-] Connection Failed!!.. Check Your Internet Connection...')
