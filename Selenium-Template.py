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
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

driver = webdriver.Chrome(options=options)

driver.get('https://food.esfahansteel.ir/Lego.Web/Kevlar/Account/Login')
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
driver.quit()
#print(txt.text)
