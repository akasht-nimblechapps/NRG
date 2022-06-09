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
time.sleep(4)
Driver.save_screenshot("Login.png")

# wait = WebDriverWait(Driver, 5)
# USER = wait.until(EC.textToBePresentInElement((By.XPATH,"//*[@id='root']/div/div/div[3]/button[1]/div[1]")))
time.sleep(3)
Driver.find_element_by_class_name("colCard").click()     #Click on User Screen
time.sleep(2)

# Counter = Driver.find_element_by_xpath("//*[@id='main-table']/thead/tr/th[1]/i")   # This code for checking multiples time Ascending and Decening order working or not
# for i in range(10000):
#     Counter.click()
# print("Passs")
# Driver.find_element_by_xpath("//*[@id='main-table']/thead/tr/th[1]/i")


Driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(3)


Driver.find_element_by_css_selector("#main-table > tbody > tr:nth-child(74) > td:nth-child(6) > div > label > span").click()
time.sleep(2)
TitleOfPage = Driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div[1]").text
print(TitleOfPage)
ConfirmationMessage = Driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/p").text
print(ConfirmationMessage)
Note = Driver.find_element_by_css_selector("body > div.fade.confirmModal.deactivateModal.modal.show > div > div > div.modal-body > div.noteText").text
print(Note)




time.sleep(2)
CancelButton = Driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/button[2]").is_enabled()

if CancelButton==True:
    print("Button Visible")
else:
    print("Button Disable")
time.sleep(2)

Driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/button[1]").click()


time.sleep(2)
Driver.close()

