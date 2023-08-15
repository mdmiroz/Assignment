from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys


keyword=input("Enter the search item:")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.co.in/search?q="+keyword)
time.sleep(5)

list=driver.find_elements("//ul[@role='listbox']//descendant::div@class='sbli'")

print(list)
