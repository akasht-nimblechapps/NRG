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



print("Both field Blank")

time.sleep(3)
Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/Login Screenshots/Both Field Blank.png")

print("Enter Mail id and Clear it, Enter password and clear it")


Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").send_keys("akash@nimblechapps.com")
time.sleep(2)
print("Not Found Login Button Enable")
Driver.delete_all_cookies()
print("cookies")
Driver.refresh()
time.sleep(4)
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").send_keys("Admin@123")
time.sleep(2)


time.sleep(2)

# Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").click()           #click on email box
# Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").clear()


# Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").send_keys("Admin@123")
time.sleep(2)
Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/Login Screenshots/Login Button.png")
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").click()
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").clear()
time.sleep(3)
Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/Login Screenshots/Login Button shows when no field fillup.png")
Driver.delete_all_cookies()
print("cookies 1")
time.sleep(2)
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()


time.sleep(5)
Driver.close()




# Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input")
# Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input")
# for i in range(1):
#     print("Enter Half Mail id and Incorrect password twice time")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").send_keys("Keval")
#     time.sleep(2)
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").send_keys("Admin@124")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[1]/button").click()
#     Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/Login Screenshots/Password Show.png")
#     time.sleep(2)
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[1]/button").click()
#     time.sleep(2)
#     Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/Login Screenshots/Password Hide.png")
#
#     print("Enter Incorrect mail id and enter correct Password")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").clear()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").send_keys("nrg@nimblechapps.com")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").clear()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").send_keys("Admin@123")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[1]/button").click()
#     time.sleep(3)
#     Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/Login Screenshots/Incorrect Mail Id.png")
#
#     print("Enter Correct Mail Id and Incorrect Password")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").clear()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").send_keys("nrg@mailinator.com")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").clear()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").send_keys("Admin@1256")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[1]/button").click()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[1]/button").click()
#     time.sleep(3)
#     Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/Login Screenshots/Incorrect Password.png")
#
#     print("Enter Half Correct Mail Id and Correct Password")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").clear()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").send_keys("nrg@mailinator.")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").clear()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").send_keys("Admin@123")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[1]/button").click()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[1]/button").click()
#     time.sleep(3)
#     Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/Login Screenshots/Half Mail ID.png")
#
#
#     print("Forgot Your Password Button working and Appear Forgot Your Password screen")
#
#     Driver.find_element_by_class_name("link").text
#     Driver.find_element_by_class_name("link").click()
#     time.sleep(2)
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/span").click()
#
#
#     print("Checking Remember me box working or not")
#
#     Driver.find_element_by_id("checkLabel").click()
#     time.sleep(1)
#     Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/Login Screenshots/Remember Me Select.png")
#     Driver.find_element_by_id("checkLabel").click()
#     time.sleep(1)
#     Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/Login Screenshots/Remember Me Unselect.png")
#     Driver.find_element_by_id("checkLabel").click()
#
#     print("Enter Correct Mail Id and Correct Password")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").clear()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input").send_keys("nrg@mailinator.com")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").clear()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input").send_keys("Admin@123")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[1]/button").click()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[1]/button").click()
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()
#     time.sleep(4)
#     Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/Login Screenshots/Login Success.png")
#
#     time.sleep(2)
#     Driver.close()
#
#
#
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[2]/div/input")
#     Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/input")
#
#
#
