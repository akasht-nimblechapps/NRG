import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

Driver = webdriver.Chrome(executable_path='../Drivers/chromedriver')
Driver.maximize_window()
Driver.implicitly_wait(5)
Driver.get("https://nrg-staging.herokuapp.com/login")


Driver.find_element_by_name("email").send_keys("nrg@mailinator.com")
Driver.find_element_by_name("password").send_keys("Admin@123")
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[1]/button").click()
time.sleep(2)
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").send_keys(Keys.ENTER)

Driver.find_element_by_css_selector("#root > div > div > div > div.rightPart > div > div.profileBtnRow > button:nth-child(3)").click()
time.sleep(2)
Driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/button[2]").text
Driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/button[2]").click()

Driver.find_element_by_css_selector("#root > div > div > div > div.rightPart > div > div.profileBtnRow > button:nth-child(3)").click()
time.sleep(2)

Title = Driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div").text
print(Title)
Confirmation = Driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/p").text
print(Confirmation)
LOGOUTBUTTON = Driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/button[1]").text
print(LOGOUTBUTTON)

time.sleep(2)

Driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/button[1]").click()


time.sleep(2)

Driver.close()
