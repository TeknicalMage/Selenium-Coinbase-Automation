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


#Clicking Google Search button 
#driver.find_element_by_xpath("//input[@value='Google Search']").click()

#Keyword searched in the chrometest

x = 1



def chrometest(): 
    compval = "base"
    macrovalue = ""
    chrome_options = Options()

    #Keyword searched in the chrometest

    chrome_options.add_argument('--user-data-dir=C:/Users/arcaz/Documents/Programming Projects/ShibTrackr/User Data2')

    chrome_options.add_argument('--profile-directory=Default')

    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")


    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://www.coinbase.com/price/shiba-inu")
    
    #driver.find_element_by_xpath("//*[@name='q']").send_keys(searchtext)  
    #driver.find_element_by_xpath("//*[@name='q']").send_keys(Keys.ENTER)  
    print('test')
    time.sleep(5)
    
    
    while True:
        now = datetime.now()
        val1 = driver.find_elements_by_xpath('//*[@class="Flex-l69ttv-0 PriceTickerChar__ValueContainer-sc-1q68ya3-2 WBuZA"]')[0].get_attribute('innerText')
        val2 = driver.find_elements_by_xpath('//*[@class="Flex-l69ttv-0 PriceTickerChar__ValueContainer-sc-1q68ya3-2 WBuZA"]')[1].get_attribute('innerText')
        val3 = driver.find_elements_by_xpath('//*[@class="Flex-l69ttv-0 PriceTickerChar__ValueContainer-sc-1q68ya3-2 WBuZA"]')[2].get_attribute('innerText')
        val4 = driver.find_elements_by_xpath('//*[@class="Flex-l69ttv-0 PriceTickerChar__ValueContainer-sc-1q68ya3-2 WBuZA"]')[3].get_attribute('innerText')
        val5 = driver.find_elements_by_xpath('//*[@class="Flex-l69ttv-0 PriceTickerChar__ValueContainer-sc-1q68ya3-2 WBuZA"]')[4].get_attribute('innerText')
        val6 = driver.find_elements_by_xpath('//*[@class="Flex-l69ttv-0 PriceTickerChar__ValueContainer-sc-1q68ya3-2 WBuZA"]')[5].get_attribute('innerText')
        val7 = driver.find_elements_by_xpath('//*[@class="Flex-l69ttv-0 PriceTickerChar__ValueContainer-sc-1q68ya3-2 WBuZA"]')[6].get_attribute('innerText')
        val8 = driver.find_elements_by_xpath('//*[@class="Flex-l69ttv-0 PriceTickerChar__ValueContainer-sc-1q68ya3-2 WBuZA"]')[7].get_attribute('innerText')
        val9 = driver.find_elements_by_xpath('//*[@class="Flex-l69ttv-0 PriceTickerChar__ValueContainer-sc-1q68ya3-2 WBuZA"]')[8].get_attribute('innerText')
        val10 = driver.find_elements_by_xpath('//*[@class="Flex-l69ttv-0 PriceTickerChar__ValueContainer-sc-1q68ya3-2 WBuZA"]')[9].get_attribute('innerText')
        time.sleep(.2)
        bignumber = (val1+val2+val3+val4+val5+val6+val7+val8+val9+val10)

        

        macrovalue = str(bignumber)
        

        if compval == macrovalue:
            pass
        else:
            print('---------')
            compval = macrovalue
            print('$' + macrovalue, end="")
            print (" | " + now.strftime("%Y-%m-%d %H:%M:%S"))

    time.sleep(10000)


        #print("---")
        #print(compval)  
        #print(macrovalue)   
        #print("---")

chrometest()
