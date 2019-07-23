print("Hello Felix")

from selenium import webdriver as webdriver
from selenium.webdriver.common.keys import keys


driver = webdriver.Chrome()
driver.set_page_load_timeout(10)

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

import time

#driver = webdriver.Chrome(executable_path='C:\Program Files\Dev_Programs\chromedriver\chromedriver.exe')
#driver = webdriver.Firefox(executable_path='C:\Program Files\Dev_Programs\firefox\geckodriver.exe')

#driver.implicitly_wait(10)
#driver.maximize_window()

driver.get('http://automationpractice.com/index.php')

driver.find_element_by_class_name("login").click()
driver.find_element_by_id("email_create").send_keys("orofelix7@gmail.com")
driver.find_element_by_id("SubmitCreate").click()




time.sleep(2)
driver.close()
driver.quit()
print('Test Completed')

## https://github.com/Raghav-Pal/PythonAutomationFrameworkPractice_1.git




 ##Fill out the Reg Form
driver.find_element_by_id("id_gender1")                                           #Radio Button
driver.find_element_by_id("customer_firstname").send_keys("Felix")                #First Name
driver.find_element_by_id("customer_lastname").send_keys("Oro")                   #Last Name
driver.find_element_by_id("email").send_keys("orofelix7@gmail.com")                #Skip email
driver.find_element_by_id("passwd").send_keys("#1Bayelsastate")                     #Passsword
driver.find_element_by_id("uniform-days")                                            #DOB- Day<"days"> TWO ACTIONS WILL BE PERFORMED  CLICK & SELECT
driver.find_element_by_id("uniform-months")                                          #DOB- Month<"days"> TWO ACTIONS WILL BE PERFORMED  CLICK & SELECT
driver.find_element_by_id("years")                                                #DOB- Year<"days"> TWO ACTIONS WILL BE PERFORMED  CLICK & SELECT
driver.find_element_by_id("newsletter")                                        #Newsletter Checkbox
driver.find_element_by_id("optin")                          #Special Offers Checkbox

#Address Fields
 driver.find_element_by_id("firstname").send_keys("Felix")          #First Name
 driver.find_element_by_id("lastname").send_keys("Felix")            #Last Name
 driver.find_element_by_id("company").send_keys("Felix")             #Company
 driver.find_element_by_id("address1").send_keys("Felix")            #Address Line 1
 driver.find_element_by_id("address2").send_keys("Felix")            #Address Line 2
 driver.find_element_by_id("city").send_keys("Felix")                #City

  driver.find_element_by_id("uniform-id_state")   #State< PERFORM TWO ACTIONS: CLICK & SELECT
 driver.find_element_by_id("postcode")            #Zip/Postal Code
 driver.find_element_by_id("id_country")          #Skip Country Drop-down <PERFORM TWO ACTIONS:

driver.find_element_by_id("other")                #Addithonal Information Text Field
driver.find_element_by_id("phone")                #Home Phone Number
driver.find_element_by_id("phone_mobile")         #Mobile Phone Number
driver.find_element_by_id("alias").send_keys("Felix")               #Alias Address- Test Field
driver.find_element_by_id("submitAccount").click()      #Register

#Thread.sleep(5000)
#driver.Close()
#driver.Quit()


time.sleep(2)
driver.close()
driver.quit()
print('Test Completed')



##
#driver.find_element_by_class_name()
#driver.find_element_by_css_selector()
#driver.find_element_by_id()
#driver.find_element_by_link_text()
#driver.find_element_by_name()
#driver.find_element_by_partial_link_text()
#driver.find_element_by_tag_name()
#driver.find_element_by_xpath()

#.click()
#.send_keys()
#.driver.quit()
#.clear()
