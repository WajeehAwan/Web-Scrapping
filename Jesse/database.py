import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="jesse_samp",
  consume_results=True
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE jesse_half")
# mycursor.execute("SHOW DATABASES")
# mycursor.execute("DROP TABLE IF EXISTS customers")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
# mycursor.execute("DROP TABLE IF EXISTS foodmanufacturer")
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")
# #These are the new tables as per Requirement if these needs any changes let me know
# foodmanufacturer= "CREATE TABLE foodmanufacturer (foodmanufacturerid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
# mycursor.execute(foodmanufacturer)
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
# mycursor.execute("DROP TABLE IF EXISTS restaurantfastfood")
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")
# restaurantfastfood = "CREATE TABLE restaurantfastfood (restaurantfastfoodid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255))"
# mycursor.execute(restaurantfastfood)
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
# mycursor.execute("DROP TABLE IF EXISTS supermarket")
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")
# supermarket = "CREATE TABLE supermarket (supermarketid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255))"
# mycursor.execute(supermarket)
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
# mycursor.execute("DROP TABLE IF EXISTS other")
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")
# other = "CREATE TABLE other (otherid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255))"
# mycursor.execute(other)

# # These are the tables of categories and subcategory and subcategory table have the forign key added from the category table
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
# mycursor.execute("DROP TABLE IF EXISTS Category")
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")
# Category = "CREATE TABLE Category (CategoryID INT AUTO_INCREMENT PRIMARY KEY,CategoryName varchar(255) NOT NULL)"
# mycursor.execute(Category)
#
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
# mycursor.execute("DROP TABLE IF EXISTS SubCategory")
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")
# SubCategory = "CREATE TABLE SubCategory (SubCategoryID int AUTO_INCREMENT PRIMARY KEY,SubCategoryName varchar(255) NOT NULL, CategoryID int NOT NULL,FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID))"
# mycursor.execute(SubCategory)

mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
mycursor.execute("DROP TABLE IF EXISTS Food")
mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")
#This is the food table with froign Keys of new tables we need to scrape
Food = "CREATE TABLE Food (id int AUTO_INCREMENT PRIMARY KEY, foodmanufacturerid int,restaurantfastfoodid int, supermarketid int, otherid int, SubCategoryID int, name Text)"
#,FOREIGN KEY(SubCategoryID) REFERENCES SubCategory(SubCategoryID),
# FOREIGN KEY(foodmanufacturerid) REFERENCES foodmanufacturer(foodmanufacturerid),
# FOREIGN KEY(supermarketid) REFERENCES supermarket(supermarketid), FOREIGN KEY(restaurantfastfoodid) REFERENCES restaurantfastfood(restaurantfastfoodid),FOREIGN KEY(otherid) REFERENCES other(otherid))
mycursor.execute(Food)
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 0")
# mycursor.execute("DROP TABLE IF EXISTS FoodPortion")
# mycursor.execute("SET FOREIGN_KEY_CHECKS = 1")
# FoodPortion = "CREATE TABLE FoodPortion (FoodPortionID int(100) NOT NULL,FoodID int(100) NOT NULL,Serving varchar(100) DEFAULT NULL,Calories varchar(100) DEFAULT NULL,Total_Fat_Weight varchar(100) DEFAULT NULL,Total_Fat_Value varchar(100) DEFAULT NULL,Saturated_Fat_Weight varchar(100) DEFAULT NULL,Saturated_Fat_Value varchar(100) DEFAULT NULL,Trans_Fat varchar(100) DEFAULT NULL,Polyunsaturated_Fat_Weight varchar(100) DEFAULT NULL,Polyunsaturated_Fat_Value varchar(255) DEFAULT NULL,Monounsaturated_Fat_Weight varchar(100) DEFAULT NULL,Monounsaturated_Fat_Value varchar(255) DEFAULT NULL,Cholesterol_Weight varchar(100) DEFAULT NULL,Cholesterol_Value varchar(100) DEFAULT NULL,Sodium_Weight varchar(100) DEFAULT NULL,Sodium_Value varchar(100) DEFAULT NULL,Total_Carbohydrate_Weight varchar(100) DEFAULT NULL,Total_Carbohydrate_Value varchar(100) DEFAULT NULL,Dietary_Weight varchar(100) DEFAULT NULL,Dietary_Value varchar(100) DEFAULT NULL,Sugars_Weight varchar(100) DEFAULT NULL,Sugars_Value varchar(255) DEFAULT NULL,Protien_Weight varchar(100) DEFAULT NULL,Protien_Value varchar(255) DEFAULT NULL,Vitamin_D_Weight varchar(100) DEFAULT NULL,Vitamin_D_Value varchar(100) DEFAULT NULL,Calcium_Weight varchar(100) DEFAULT NULL,Calcium_Value varchar(100) DEFAULT NULL,Iron_Weight varchar(100) DEFAULT NULL,Iron_Value varchar(100) DEFAULT NULL,Potassium_Weight varchar(100) DEFAULT NULL,Potassium_Value varchar(100) DEFAULT NULL,Vitamin_A_Weight varchar(100) DEFAULT NULL,Vitamin_A_Value varchar(100) DEFAULT NULL,Vitamin_C_Weight varchar(100) DEFAULT NULL,Vitamin_C_Value varchar(100) DEFAULT NULL,url varchar(500) DEFAULT NULL)FOREIGN KEY (FoodID) REFERENCES Food (FoodID)"

# tables = mycursor.execute("SHOW TABLES")
# print(tables)
# # sql = "INSERT INTO Category (CategoryID, CategoryName) VALUES (%s, %s)"
# # val = ("1", "Highway 21")
# mycursor.execute(sql, val)

# sql = "INSERT INTO SubCategory (SubCategoryID, SubCategoryName,CategoryID) VALUES (%s, %s,%s)"
# val = ("1", "Highway 21","1")
# mycursor.execute(sql, val)

mydb.commit()
