import time 
import random
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


import random
from datetime import datetime
 

import string
import pickle



def chrometest(): 
    compval = "base"
    macrovalue = ""
    macrostr = ""
    x = 0
    chrome_options = Options()

    #Keyword searched in the chrometest

    #You need a chrome profile logged into coinbase. Any basic account will do. The goal is just to utilize the stats
    #displayed and updated by coinbase without refreshing the page or being flagged as a bot
    #Having a logged in account minimizes site interaction, which lowers the chance of detection
    chrome_options.add_argument('--user-data-dir=C:/Users/arcaz/Documents/Programming Projects/ShibTrackr/User Data2')
    chrome_options.add_argument('--profile-directory=Default')


    #Gets rid of errors \ selenium hook log bs
    chrome_options.add_argument('--log-level=3')
    #Gets rid of errors \ selenium hook log bs
    
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")


    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.coinbase.com/price/shiba-inu")
    
      
    print('test')
    time.sleep(5)
    
    
    while True:
        now = datetime.now()
        time.sleep(.2)

        for x in range(10):
            val = driver.find_elements_by_xpath('//*[@class="Flex-l69ttv-0 PriceTickerChar__ValueContainer-sc-1q68ya3-2 WBuZA"]')[x].get_attribute('innerText')
            #Adding everything to a larger string
            macrostr+=val
        
        #functionally useless, but it merges into the og setup
        macrovalue = str(macrostr)
        
        #Look at the value, if it isn't new, don't do anything
        if compval == macrovalue:
            pass
        else:
            print('---------')
            #Makes sure it won't repeat in the next iteration
            compval = macrovalue

            #Functional output of the program
            print('$' + macrovalue, end="")
            print (" | " + now.strftime("%Y-%m-%d %H:%M:%S"))

    time.sleep(10000)


        #print("---")
        #print(compval)  
        #print(macrovalue)   
        #print("---")

chrometest()



