#Importing selenium and all the stuff we need
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import random
from random import randrange
import os
import time
from userAgents import agents
botCount = 0
counter = 1
chooseAgent = ""
current_path = os.path.dirname(os.path.realpath(__file__))

url = input("URL to visit: ")


agentPrint = input("What Agent do you want to use? [iPhone, Android, Random]: ")
if(agentPrint == "Android"):
    chooseAgent = "user-agent=Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19"
elif(agentPrint == "iPhone"):
    chooseAgent = "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"

maxloop = input("How Many times do you want to visit the page?: ")

while True: #Loop
    
    if(agentPrint == "Random"):
        chooseAgent = random.choice(agents) #Take random choice from the agents array
    botCount +=1
    print(u"\u001b[34;1mBot N.",botCount, "\u001b[0m")
    print("Views: ",int(counter),"/",int(maxloop))
    print("Url: ",url)
    lines = open(current_path+'/proxies.txt').read().splitlines() #Open the proxies.txt file and read all the lines
    chooseProxy = random.choice(lines) #Choose a random line
    print("Proxy: ",chooseProxy)
    print(chooseAgent)

    #Options
    opts = Options()
    opts.add_argument(chooseAgent) 
    opts.add_experimental_option('excludeSwitches', ['enable-logging']) #Disable useless logs in the console
    opts.add_argument('--proxy-server=%s' % chooseProxy) #Set proxy
    opts.add_argument('headless') #Make it run in background
    driver = webdriver.Chrome(current_path+"/chromedriver.exe",options=opts) #Select WebDriver
    driver.set_page_load_timeout(15) #Setting a 15 seconds timeout
    try:
        driver.get(url) #Fire the url
        time.sleep(2) #Wait 2 seconds
    except TimeoutException as ex:
        print(u"\u001b[31mBot is taking too much time... Skipping\u001b[0m")
        counter-=1
    else:
        print(u"\u001b[32;1mDone!\u001b[0m")
    print("Cleaning Cookies")
    driver.delete_all_cookies() #Clean the cookies
    print("Cookie cleaned, exiting..\n")
    driver.quit() #exit
    counter+=1
    if int(counter) > int(maxloop):
        print("Finished!")
        break
        
