from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"

for i in range(1,10):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=2AZFGVVZZZ6C8&sprefix=lapto%2Caps%2C360&ref=nb_sb_noss_2")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container") 

    print(elems) # class list
    for elem in elems:
        print(elem.text)
        print(len(elems))
    

# print(elem.text) # Fethching element
# print(elem.get_attribute("outerHTML")) 

    time.sleep(2)

driver.close()


