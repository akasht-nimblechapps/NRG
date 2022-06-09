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
Driver.find_element_by_id("checkLabel").text
Driver.find_element_by_id("checkLabel").click()
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div/div[1]/button").click()
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").send_keys(Keys.ENTER)


ChangePassword = Driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div[3]/button[2]").text
print(ChangePassword)
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div/div[3]/button[2]").click()

Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/input")  #Confirm Password
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/input")       #New Password
Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/input")        #Re enter New Password


for i in range(1):
    print("Enter Digits Only and verify validation error")

    Driver.find_element_by_class_name('label').text                         #Current Password
    Driver.find_element_by_name('password').send_keys("123456")
    time.sleep(1)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    time.sleep(1)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    Driver.find_element_by_class_name("label").text                    #New Password
    Driver.find_element_by_name("newPassword").send_keys("123456789")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_class_name("label").text                        #Re-Enter Password
    Driver.find_element_by_name("confirmPassword").send_keys("123456789")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()

    print("Enter small digit in current password and verify validation error and Password in other two field with special character")
    time.sleep(2)
    Driver.find_element_by_name('password').clear()
    # Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[2]/span").text        #Current Password Validation error
    Driver.find_element_by_name('password').send_keys('akash@123')
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    time.sleep(1)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    Driver.find_element_by_name("newPassword").clear()
    #Driver.find_element_by_name("errorMsg show").text          #shows please enter password
    Driver.find_element_by_name("newPassword").send_keys("A")
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[1]/span").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[2]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[3]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[4]").text
    time.sleep(2)
    Driver.find_element_by_name("newPassword").clear()
    Driver.find_element_by_name("newPassword").send_keys("Akash@@@")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    Driver.find_element_by_name("confirmPassword").clear()
    Driver.find_element_by_name("confirmPassword").send_keys("Akash@@@")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()

    print("Enter Current Password wrong and in other two put password with small letter")
    time.sleep(2)
    Driver.find_element_by_name('password').clear()
    # Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[2]/span").text        #Current Password Validation error
    Driver.find_element_by_name('password').send_keys('Akash@@@')
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    time.sleep(1)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    Driver.find_element_by_name("newPassword").clear()
    # Driver.find_element_by_name("errorMsg show").text          #shows please enter password
    Driver.find_element_by_name("newPassword").send_keys("@")
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[1]/span").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[2]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[3]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[4]").text
    time.sleep(2)
    Driver.find_element_by_name("newPassword").clear()
    Driver.find_element_by_name("newPassword").send_keys("akash@123")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    Driver.find_element_by_name("confirmPassword").clear()
    Driver.find_element_by_name("confirmPassword").send_keys("akash@123")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()


    print("Enter current password proper but in other field add wrong password with character and special character")

    time.sleep(2)
    Driver.find_element_by_name('password').clear()
    # Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[2]/span").text        #Current Password Validation error
    Driver.find_element_by_name('password').send_keys('Admin@123')
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    time.sleep(1)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    Driver.find_element_by_name("newPassword").clear()
    # Driver.find_element_by_name("errorMsg show").text          #shows please enter password
    Driver.find_element_by_name("newPassword").send_keys("1")
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[1]/span").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[2]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[3]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[4]").text
    time.sleep(2)
    Driver.find_element_by_name("newPassword").clear()
    Driver.find_element_by_name("newPassword").send_keys("Ak@Ak@Ak@Ak")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    Driver.find_element_by_name("confirmPassword").clear()
    Driver.find_element_by_name("confirmPassword").send_keys("Ak@Ak@Ak@Ak")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()

    print("Enter # in the current password and enter proper password in other two fields")

    time.sleep(2)
    Driver.find_element_by_name('password').clear()
    # Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[2]/span").text        #Current Password Validation error
    Driver.find_element_by_name('password').send_keys('########')
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    time.sleep(1)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    Driver.find_element_by_name("newPassword").clear()
    # Driver.find_element_by_name("errorMsg show").text          #shows please enter password
    Driver.find_element_by_name("newPassword").send_keys("w")
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[1]/span").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[2]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[3]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[4]").text
    time.sleep(2)
    Driver.find_element_by_name("newPassword").clear()
    Driver.find_element_by_name("newPassword").send_keys("Akash@123")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    Driver.find_element_by_name("confirmPassword").clear()
    Driver.find_element_by_name("confirmPassword").send_keys("Akash@123")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()


    print("Enter current password proper and in other two field enter proper password except capital letter")

    time.sleep(2)
    Driver.find_element_by_name('password').clear()
    # Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[2]/span").text        #Current Password Validation error
    Driver.find_element_by_name('password').send_keys('Admin@123')
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    time.sleep(1)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    Driver.find_element_by_name("newPassword").clear()
    # Driver.find_element_by_name("errorMsg show").text          #shows please enter password
    Driver.find_element_by_name("newPassword").send_keys("()")
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[1]/span").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[2]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[3]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[4]").text
    time.sleep(2)
    Driver.find_element_by_name("newPassword").clear()
    Driver.find_element_by_name("newPassword").send_keys("123@akash")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    Driver.find_element_by_name("confirmPassword").clear()
    Driver.find_element_by_name("confirmPassword").send_keys("123@akash")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()


    print("Enter current password proper, But in other two filed enter different password")

    time.sleep(2)
    Driver.find_element_by_name('password').clear()
    # Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[2]/span").text        #Current Password Validation error
    Driver.find_element_by_name('password').send_keys('Admin@123')
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    time.sleep(1)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    Driver.find_element_by_name("newPassword").clear()
    # Driver.find_element_by_name("errorMsg show").text          #shows please enter password
    Driver.find_element_by_name("newPassword").send_keys("()")
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[1]/span").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[2]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[3]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[4]").text
    time.sleep(2)
    Driver.find_element_by_name("newPassword").clear()
    Driver.find_element_by_name("newPassword").send_keys("123@Akash")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    Driver.find_element_by_name("confirmPassword").clear()
    Driver.find_element_by_name("confirmPassword").send_keys("123@akash")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()

    print("Enter Password proper in the all field")

    time.sleep(2)
    Driver.find_element_by_name('password').clear()
    # Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[2]/span").text        #Current Password Validation error
    Driver.find_element_by_name('password').send_keys('Admin@124')
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    time.sleep(1)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/div[1]/button").click()
    Driver.find_element_by_name("newPassword").clear()
    # Driver.find_element_by_name("errorMsg show").text          #shows please enter password
    Driver.find_element_by_name("newPassword").send_keys("()")
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[1]/span").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[2]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[3]").text
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[2]/div[4]").text
    time.sleep(2)
    Driver.find_element_by_name("newPassword").clear()
    Driver.find_element_by_name("newPassword").send_keys("Admin@123")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/div[1]/button").click()
    Driver.find_element_by_name("confirmPassword").clear()
    Driver.find_element_by_name("confirmPassword").send_keys("Admin@123")
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    time.sleep(2)
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/div[1]/button").click()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").is_displayed()
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/button").click()
    time.sleep(10)
    Driver.quit()

    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[3]/div[2]/input")  # Confirm Password
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[4]/div/input")  # New Password
    Driver.find_element_by_xpath("//*[@id='root']/div/div/div[2]/form/div[5]/div/input")  # Re enter New Password