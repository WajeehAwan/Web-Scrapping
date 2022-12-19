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

linkfood = []
linkresturant = []
linkmarket = []
linkother = []
def scrapemfood():
    manufname = []
    numf=0

    for i in range(32):
        url = f'https://www.fatsecret.com/Default.aspx?pa=brands&pg={i}&f=a&t=1'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        # print('runiing')
        for i in soup.find_all('h2')[:-1]:
            a_tag = i.find_all("a")
            for i in a_tag:
                linkfood.append(i.attrs['href'])
                manufname.append(i.text)
        #foodmanufacturerInsert(manufname)
    for i in range(len(linkfood)):
        numf+=1
        bpage = requests.get(f'https://www.fatsecret.com{linkfood[i]}')
        soup1 = BeautifulSoup(bpage.text, 'lxml')
        table = soup1.find('div', {"class": 'leftCellContent'})
        rows = table.find_all("tr")  # here you have to use find_all for finding all rows of table
        for tr in rows:
            cols = tr.find_all('td')  # here also you have to use find_all for finding all columns of current row
            if cols == []:  # This is a sanity check if columns are empty it will jump to next row
                continue
            else:
                for i in cols:
                    atag = i.find_all('a')
                    for i in atag:
                        if i == []:
                            continue
                        else:
                            variable_1 = numf
                            variable_2 = i.text
                            varlist = [(f'{variable_1}','0', '0', '0', '0', f'{variable_2}')]
                            sql = "INSERT INTO Food (foodmanufacturerid,restaurantfastfoodid, supermarketid, otherid, SubCategoryID, name) VALUES (%s,%s,%s,%s,%s,%s)"
                            mycursor.executemany(sql, varlist)
                            mydb.commit()
def resturantscrape():
    restname = []
    numf=0
    for i in range(2):
        url = f'https://www.fatsecret.com/Default.aspx?pa=brands&pg={i}&f=a&t=2'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        for i in soup.find_all('h2')[:-1]:
            a_tag = i.find_all("a")
            # print(i)
            for i in a_tag:
                linkresturant.append(i.attrs['href'])
                restname.append(i.text)
        #resturantInsert(restname)
    for j in range(len(linkresturant)):
        numf+=1
        bpage= requests.get(f'https://www.fatsecret.com{linkresturant[j]}')
        soup1 = BeautifulSoup(bpage.text, 'lxml')
        table = soup1.find('div', {"class": 'leftCellContent'})
        rows = table.find_all("tr")  # here you have to use find_all for finding all rows of table
        for tr in rows:
            cols = tr.find_all('td')  # here also you have to use find_all for finding all columns of current row
            if cols == []:  # This is a sanity check if columns are empty it will jump to next row
                continue
            else:
                for i in cols:
                    atag = i.find_all('a')
                    for i in atag:
                        if i == []:
                            continue
                        else:
                            variable_1 = numf
                            variable_2 = i.text
                            varlist = [('0',f'{variable_1}','0','0','0', f'{variable_2}')]
                            sql="INSERT INTO Food (foodmanufacturerid,restaurantfastfoodid, supermarketid, otherid, SubCategoryID, name) VALUES (%s,%s,%s,%s,%s,%s)"
                            mycursor.executemany(sql, varlist)
                            mydb.commit()
                            #Food(i.text)
def marketscraper():
    marketname = []
    catemarketname = []
    numf = 0
    for i in range(2):
        url = f'https://www.fatsecret.com/Default.aspx?pa=brands&pg={i}&f=a&t=3'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        for i in soup.find_all('h2')[:-1]:
            a_tag = i.find_all("a")
            for i in a_tag:
                linkmarket.append(i.attrs['href'])
                marketname.append(i.text)
        #marketInsert(marketname)

    for i in range(len(linkmarket)):
        numf+=1
        bpage = requests.get(f'https://www.fatsecret.com{linkmarket[i]}')
        soup1 = BeautifulSoup(bpage.text, 'lxml')
        table = soup1.find('div', {"class": 'leftCellContent'})
        rows = table.find_all("tr")  # here you have to use find_all for finding all rows of table
        for tr in rows:
            cols = tr.find_all('td')  # here also you have to use find_all for finding all columns of current row
            if cols == []:  # This is a sanity check if columns are empty it will jump to next row
                continue
            else:
                for i in cols:
                    atag = i.find_all('a')
                    for i in atag:
                        if i == []:
                            continue
                        else:
                            variable_1 = numf
                            variable_2 = i.text
                            varlist = [('0', '0', f'{variable_1}', '0', '0', f'{variable_2}')]
                            sql = "INSERT INTO Food (foodmanufacturerid,restaurantfastfoodid, supermarketid, otherid, SubCategoryID, name) VALUES (%s,%s,%s,%s,%s,%s)"
                            mycursor.executemany(sql, varlist)
                            mydb.commit()
def otherscrape():
    othername = []
    numf=0
    for i in range(77):
        url = f'https://www.fatsecret.com/Default.aspx?pa=brands&pg={i}&f=a&t=5'
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'lxml')
        for i in soup.find_all('h2')[:-1]:
            a_tag = i.find_all("a")
            for i in a_tag:
                linkother.append(i.attrs['href'])
                othername.append(i.text)
        #otherInsert(othername)
    for i in range(len(linkother)):
        numf += 1
        bpage = requests.get(f'https://www.fatsecret.com{linkother[i]}')
        soup1 = BeautifulSoup(bpage.text, 'lxml')
        table = soup1.find('div', {"class": 'leftCellContent'})
        rows = table.find_all("tr")  # here you have to use find_all for finding all rows of table
        for tr in rows:
            cols = tr.find_all('td')  # here also you have to use find_all for finding all columns of current row
            if cols == []:  # This is a sanity check if columns are empty it will jump to next row
                continue
            else:
                for i in cols:
                    atag = i.find_all('a')
                    for i in atag:
                        if i == []:
                            continue
                        else:
                            variable_1 = numf
                            variable_2 = i.text
                            varlist = [('0', '0','0', f'{variable_1}', '0', f'{variable_2}')]
                            sql = "INSERT INTO Food (foodmanufacturerid,restaurantfastfoodid, supermarketid, otherid, SubCategoryID, name) VALUES (%s,%s,%s,%s,%s,%s)"
                            mycursor.executemany(sql, varlist)
                            mydb.commit()



def foodmanufacturerInsert(name):
    x = [s[1:] for s in name]
    for i in range(len(x)):
        print(x[i])
        sql = "INSERT INTO foodmanufacturer(name) VALUES (%s)"
        value = (f'{x[i]}')

        try:
            mycursor.execute(sql, (value,))
            mydb.commit()
        except:
            print('rolled back')
def resturantInsert(name):
    x = [s[1:] for s in name]
    for i in range(len(x)):
        print(x[i])
        sql = "INSERT INTO restaurantfastfood(name) VALUES (%s)"
        value = (f'{x[i]}')

        try:
            mycursor.execute(sql, (value,))
            mydb.commit()
            print('Inserted')
        except:
            print('rolled back')
def marketInsert(name):
    x = [s[1:] for s in name]
    for i in range(len(x)):
        print(x[i])
        sql = "INSERT INTO supermarket(name) VALUES (%s)"
        value = (f'{x[i]}')

        try:
            mycursor.execute(sql, (value,))
            mydb.commit()
        except:
            print('rolled back')
def otherInsert(name):
    x = [s[1:] for s in name]
    for i in range(len(x)):
        print(x[i])
        sql = "INSERT INTO other(name) VALUES (%s)"
        value = (f'{x[i]}')

        try:
            mycursor.execute(sql, (value,))
            mydb.commit()
        except:
            print('rolled back')


scrapemfood()
marketscraper()
resturantscrape()
otherscrape()


mydb.close()

