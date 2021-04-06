#The code isn't completed yet.
#If it is really urgent, then I would clone this repo,
#Or else, please don't. Because I may develop new UI and designs.
# So please wait...
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
print("The code isn't complete yet. Please check for updates for new version which is much cooler and easy to use")
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
