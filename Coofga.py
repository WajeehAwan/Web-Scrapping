import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
import os
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
os.environ['PATH'] += r"C:\Users\SL LAPTOP\PycharmProjects\pythonProject/chromedriver.exe"
driver = webdriver.Chrome()
driver.get('https://www.cpcoofga.com/cpco-member-directory/')
driver.maximize_window()
header=[]
check =[]
name = []
address = []
phone = []
email=[]
county = []
dict={}
driver.implicitly_wait(20)


for k in range(2,26):
        for i in range(1,21):
            try:
                head = driver.find_elements(By.XPATH,
                                        f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[1]/div/h2')
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                    (By.XPATH,
                    f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[1]/div/h2')))
                for myelement in head:
                    header.append(myelement.text)

                name_element = driver.find_elements(By.XPATH,
                                                    f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[3]/div/div/div/div')
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                    (By.XPATH,
                     f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[3]/div/div/div/div')))
                for myelement in name_element:
                    name.append(myelement.text)

                address_ele = driver.find_elements(By.XPATH,
                                                   f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[4]/div/div/div')
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                    (By.XPATH,
                     f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[4]/div/div/div')))
                for myelement in address_ele:
                    address.append(myelement.text)

                phones_ele = driver.find_elements(By.XPATH,
                                                  f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[5]/div/div/div/div')
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                    (By.XPATH,
                     f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[5]/div/div/div/div')))
                for myelement in phones_ele:
                    phone.append(myelement.text)

                email_ele = driver.find_elements(By.XPATH,
                                                 f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[6]/div/div/div/div')
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                    (By.XPATH,
                     f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[6]/div/div/div/div')))
                for myelement in email_ele:
                    email.append(myelement.text)

                county_ele = driver.find_elements(By.XPATH,
                                                  f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[7]/div/div/div/div')
                time.sleep(1)
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                    (By.XPATH,
                     f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[1]/div/div/div/div[{i}]/div/div/div/section/div[2]/div/div/div/div/section/div/div/div/div/div/div[7]/div/div/div/div')))
                for myelement in county_ele:
                    county.append(myelement.text)

            except StaleElementReferenceException as er:
                print(f'error header {er}')
            except TimeoutException as er:
                print(f'time out {er}')
            print(header)
            print(name)
            print(address)
            print(phone)
            print(county)
        try:
            time.sleep(3)
            next = driver.find_element(By.XPATH,
                                f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[2]/div/div/div/div[{k}]/div')
            time.sleep(3)
            WebDriverWait(driver, 100).until(EC.element_to_be_clickable(
                    (By.XPATH,
                            f'/html/body/div[2]/div/div/section[3]/div/div/div/div/div/div[2]/div/div/div/div[{k}]/div')))
            next.click()
        except StaleElementReferenceException as er:
            print(f'error click stale {er}')
        except ElementClickInterceptedException as er:
            print(f'this is not clickable {er}')

for j in range(len(header)):
    dict[header[j]] = f'{name[j]},{address[j]},{phone[j]},{email[j]},{county[j]}'
    print(dict)
    df = pd.DataFrame(data=dict, index=[0])
    df = (df.T)
    print(df)
    df.to_csv(f'file1.csv')

