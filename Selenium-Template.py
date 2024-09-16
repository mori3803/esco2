import undetected_chromedriver as uc
import os
import time
import datetime
driver = uc.Chrome(headless=True,use_subprocess=False)
driver.get('https://www.google.co.uk/')
time.sleep(10)
print(driver.title)

"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import os
import time
import datetime
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

username = os.environ["username"]
password = os.environ["password"]

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1200,1200")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--enable-logging")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver = webdriver.Chrome(options=options)
#https://food.esfahansteel.ir/Lego.Web/Kevlar/Account/Login
driver.get('https://food.esfahansteel.ir/Lego.Web/Kevlar/Account/Login?ReturnUrl=%2FLego.Web%2F')
time.sleep(10)
print(driver.title)

driver.find_element("id", "UserName").send_keys(username)
driver.find_element("id", "Password").send_keys(password)
driver.find_element("id", "btnSubmit").click()
time.sleep(15)

driver.find_elements(By.CLASS_NAME,'favmenu-item-inner-wrapper')[1].click()
#f3[1].click()
#f.send_keys(Keys.RETURN)
time.sleep(50)
#logs = driver.get_log("performance")
#driver.save_screenshot("screenshot.png")
#print(driver.page_source)
foods = driver.find_elements(By.CLASS_NAME,'food-name')
#for food in foods : 
    #print(food.text)
print(datetime.datetime.now())

#text = driver.find_element("class", "text-title")
#driver.find_element(By.XPATH , '//a | //*[contains(concat( " ", @class, " " ), concat( " ", "title", " " ))]').click()
#time.sleep(10)
#txt = driver.find_element(By.CLASS_NAME, "text-title")
with open('./GitHub_Action_Results.txt', 'w') as f:
    for food in foods:
        f.write(f"{(food.text).replace('آب معدني نيم ليتري', '')}\n")
"""
driver.quit()
#print(txt.text)
