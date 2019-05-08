from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import datetime


print("* * *    *      * * *  *    *  * * *     * * *  *    *  * * *")
print("*    *   *        *    * *  *  *    *    *       *  *   *    ")
print("* * *    *        *    *  * *  *     *   * *      **    * *  ")
print("*    *   *        *    *   **  *    *    *        *     *    ")
print("* * *    * * *  * * *  *    *  * * *     * * *   *      * * *")

# enter the number of the person by the user
target = str(input("Enter the name of target: "))

# chrome driver
chrome_options = Options()
driver = webdriver.Chrome('/home/rohit/blind-eye/chromedriver')
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
assert "WhatsApp" in driver.title

# finds the target and navigate to it
x_arg = '//span[contains(@title, '+ '"' +target + '"'+ ')]'
person_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
print(target)
person_title.click()

# check status
while True:
	i=0
	try:
		status = driver.find_element_by_class_name('O90ur').text
		i=1
	except NoSuchElementException:
		status = 'offline'
		i=0
	print(datetime.datetime.now())
	print(status)
	while True:
		if i == 1:
			try:
				re_status = driver.find_element_by_class_name('O90ur').text
				continue
			except NoSuchElementException:
				re_status = 'offline'
				break
		else:
			try:
				re_status = driver.find_element_by_class_name('O90ur').text
				break
			except NoSuchElementException:
				re_status = 'offline'
				continue
	time.sleep(1)