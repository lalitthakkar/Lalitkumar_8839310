# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the apple homepage
driver.get("https://www.apple.com/")
driver.maximize_window()  # Maximizing the browser window
time.sleep(5)

# Clicking on the appstore link on the header
appstore = driver.find_element("xpath","/html/body/div[1]/nav/div/ul/li[2]/div/div/div[1]/ul/li[1]/a/span[1]")
appstore.click()

# Waiting for the page to load
time.sleep(5)

# Clicking on iphone link
c_iphone = driver.find_element("xpath","//html/body/div[2]/div[2]/div[4]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/img")
c_iphone.click()

# Waiting for the page to load
time.sleep(10)

# click on iphone 14 pro button
iphone_buy = driver.find_element("xpath","/html/body/div[2]/div[2]/div[5]/div/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/img")
iphone_buy.click()
#
#
# #
time.sleep(10)


# Clicking on buy button
click_buy = driver.find_element("xpath", "/html/body/div[3]/div/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[2]/a")
click_buy.click()


# Closing the webdriver
driver.quit()