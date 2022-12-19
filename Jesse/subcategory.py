import mysql.connector
import requests
from bs4 import BeautifulSoup

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="jesse_samp",
  consume_results=True
)

mycursor = mydb.cursor()
def subcategoryscrapper():
  subcategoryname= []
  numf=0
  bpage = requests.get('https://www.fatsecret.com/calories-nutrition/')
  soup1 = BeautifulSoup(bpage.text, 'lxml')
  #print(soup1)
  # table = soup1.find('table', {"class": 'generic common'})
  # link = table.findAll('a')
  link=[tag.find("a")["href"] for tag in soup1.select("td:has(a)")]
  print([link[4:]])
  for j in range(len(link)):
    page = requests.get(f'https://www.fatsecret.com{link[j]}')
    soup = BeautifulSoup(page.text, 'lxml')
    h2 = soup.find_all('h2')
    if (j>=4):
      numf += 1
    for i in h2:
      a_tag = i.find_all("a")
      for i in a_tag:
        variable_1 = numf
        variable_2 = i.text
        varlist = [('0', '0', '0', f'{variable_1}', f'{variable_1}', f'{variable_2}')]
        sql = "INSERT INTO Food (foodmanufacturerid,restaurantfastfoodid, supermarketid, otherid, SubCategoryID, name) VALUES (%s,%s,%s,%s,%s,%s)"
        mycursor.executemany(sql, varlist)
        mydb.commit()


subcategoryscrapper()