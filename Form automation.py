import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:\Users\SL LAPTOP\PycharmProjects\pythonProject/chromedriver.exe"
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/watch?v=N0lxfilGfak')
comments = []
my_length = len(WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="content-text"]'))))
for i in range(2):
    try:
        driver.execute_script("window.scrollBy(0,800)")
        time.sleep(1)
        comments.append([my_elem.text for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="content-text"]')))])
    except TimeoutException:
        driver.quit()
        break
print(comments[0])