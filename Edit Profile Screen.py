import time
from telnetlib import EC
import pyautogui
import self as self

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
time.sleep(4)



EditProfile = Driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div[3]/button[1]").text
print(EditProfile)
time.sleep(2)
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div[3]/button[1]").click()
time.sleep(2)

Driver.find_element_by_name("userName").click()
Driver.find_element_by_name("userName").send_keys(Keys.SPACE)
Driver.find_element_by_name("userName").send_keys(Keys.SPACE)
Driver.find_element_by_name("userName").send_keys(Keys.SPACE)
Driver.find_element_by_name("userName").send_keys(Keys.SPACE)
Driver.find_element_by_name("userName").send_keys(Keys.SPACE)
Driver.find_element_by_name("userName").send_keys(Keys.SPACE + "NRG")
#Driver.find_element_by_name("userName").send_keys(Keys.SEMICOLON + "NRG")

time.sleep(2)

Driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)

Driver.find_element_by_xpath("/html/body/div/div/div/div/div/form/div[2]/button[1]").is_enabled()
time.sleep(1)
Driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/form/div[2]/button[1]").click()
time.sleep(2)

Driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div[3]/button[1]").click()
Driver.implicitly_wait(5)

Driver.find_element_by_name("userName").click()
time.sleep(2)
Driver.find_element_by_name("userName").clear()

Driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)

Driver.save_screenshot("Save Changes Button On.png")



Driver.close()

