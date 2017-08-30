from selenium import webdriver
import time
import datetime
def getCurrentTime():
    return time.strftime("%H:%M:%S")
print ("{} Starting".format(getCurrentTime()))
#########################################
IP         = ''#IP:PORT
url        = ''#url
###########################################
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server='+IP)
driver = webdriver.Chrome(chrome_options=chrome_options)
print("{} Using Proxy".format(getCurrentTime()),IP)
driver.get(url)