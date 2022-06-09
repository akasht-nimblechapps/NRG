import time

from selenium import webdriver
from selenium.webdriver import Keys

Driver = webdriver.Chrome(executable_path='/Users/akashtiwari/PycharmProjects/NimbleChapps\ Project/NRG\ Project/Drivers/chromedriver')
Driver.maximize_window()
Driver.implicitly_wait(5)
Driver.get("https://nrg-staging.herokuapp.com/login")

Driver.find_element_by_class_name("link").click()
LabelName = Driver.find_element_by_class_name("labelTitle").text
print(LabelName)
Driver.find_element_by_name("email").send_keys("akasht@nimblechapps.c")
ValidationError = Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[2]/span").text
print(ValidationError)

Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()
time.sleep(3)
Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/ForGot Passwrod Image screenshots/Email Incorrect 1.png")
time.sleep(2)


Driver.find_element_by_name("email").click()
Driver.find_element_by_name("email").clear()
LabelName = Driver.find_element_by_class_name("labelTitle").text
print(LabelName)
Driver.find_element_by_name("email").send_keys("nrg@mailinator")
ValidationError = Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[2]/span").text
print(ValidationError)
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()
Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/ForGot Passwrod Image screenshots/Email Incorrect 2.png")
time.sleep(3)

Driver.find_element_by_name("email").click()
Driver.find_element_by_name("email").clear()
LabelName = Driver.find_element_by_class_name("labelTitle").text
print(LabelName)
Driver.find_element_by_name("email").send_keys("nrgmailinator.com")
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()
time.sleep(2)
Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/ForGot Passwrod Image screenshots/Email Incorrect 3.png")

Driver.find_element_by_name("email").click()
Driver.find_element_by_name("email").clear()
LabelName = Driver.find_element_by_class_name("labelTitle").text
print(LabelName)
Driver.find_element_by_name("email").send_keys("123564QWerty")
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()
time.sleep(2)
Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/ForGot Passwrod Image screenshots/Email Incorrect 4.png")


Driver.find_element_by_name("email").click()
Driver.find_element_by_name("email").clear()
LabelName = Driver.find_element_by_class_name("labelTitle").text
print(LabelName)
Driver.find_element_by_name("email").send_keys("12345@@###$$.com")
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()
time.sleep(2)
Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/ForGot Passwrod Image screenshots/Email Incorrect 5.png")


Driver.find_element_by_name("email").click()
Driver.find_element_by_name("email").clear()
LabelName = Driver.find_element_by_class_name("labelTitle").text
print(LabelName)
Driver.find_element_by_name("email").send_keys("nrg@nimblechapps.com")
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
time.sleep(1)
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()
time.sleep(3)
Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/ForGot Passwrod Image screenshots/Email Incorrect 6.png")


Driver.find_element_by_name("email").click()
Driver.find_element_by_name("email").clear()
LabelName = Driver.find_element_by_class_name("labelTitle").text
print(LabelName)
Driver.find_element_by_name("email").send_keys("nrg@nimblechapps...com")
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()
time.sleep(3)
Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/ForGot Passwrod Image screenshots/Email Incorrect 7.png")


Driver.find_element_by_name("email").click()
Driver.find_element_by_name("email").clear()
LabelName = Driver.find_element_by_class_name("labelTitle").text
print(LabelName)
Driver.find_element_by_name("email").send_keys("nrg@mailinator.com")
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
time.sleep(2)
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()
time.sleep(3)
# Driver.find_element_by_name("email").send_keys("nrg@mailinator.com")
Driver.save_screenshot("/Users/akashtiwari/PycharmProjects/PythonProject/ForGot Passwrod Image screenshots/Email Correct.png")

time.sleep(5)
Driver.close()





print("Not Moved on the Login screen")