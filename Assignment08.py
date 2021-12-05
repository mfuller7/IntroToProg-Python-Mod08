# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# MFuller,12.03.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product():
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MFuller,12.03.2021,Modified code to complete assignment 8
    """

    # Constructor
    def __init__(self, product_name:str, product_price:float):
        self.__product_name = product_name
        self.__product_price = product_price

    # Properties
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception('Name should be alpha characters')

    @property
    def product_price(self):
        return str(self.__product_price).title()

    @product_price.setter
    def product_price(self, value):
        try:
            self.__product_price = value * 1
        except Exception as e:
            print('type of value is: ' + str(type(value)))
            print('Price should be numeric value')
            print(e)
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor():
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MFuller,12.03.2021,Modified code to complete assignment 8
    """
    @staticmethod
    def read_data_from_file(file_name):
        data = []

        with open(file_name, 'r+') as file:
            for row in file:
                tempProduct = Product('', 0)
                tempProduct.product_name, tempProduct.product_price = row.split(',')
                data.append(tempProduct)

        print('File loaded!')
        return data
    # DONE: Add Code to process data from a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        with open(file_name, 'w+') as file:
            for row in list_of_product_objects:
                file.write(row.product_name + ', ' + str(row.product_price).strip() + '\n')
    # DONE: Add Code to process data to a file

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Communicate options to user and receive input:

        methods:

        changelog: (When,Who,What)
            RRoot,1.1.2030,Created Class
            MFuller,12.03.2021,Modified code to complete assignment 8
        """
    # DONE: Add docstring
    @staticmethod
    def menu():
        print('\nMENU\n'
              '1) Show current data\n'
              '2) Add Item\n'
              '3) Save data and exit\n'
              )
    # DONE: Add code to show menu to user
    @staticmethod
    def userChoice():
        choice = input('Please enter number corresponding to menu item.\n')
        return choice
    # DONE: Add code to get user's choice
    @staticmethod
    def currentData():
        print('--- Current Data ---')
        if not lstOfProductObjects:
            print('File is empty.')
        else:
            for each in lstOfProductObjects:
                print(each.product_name + ', $' + each.product_price)
    # DONE: Add code to show the current data from the file to user
    @staticmethod
    def addData():
        tempProduct = Product('', 0)
        tempProduct.product_name = input('Enter product name: ')
        tempProduct.product_price = float(input('Enter product price: '))
        lstOfProductObjects.append(tempProduct)
        print('%s added.' % tempProduct.product_name)
    # DONE: Add code to get product data from user
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects.clear()
lstOfProductObjects.extend(FileProcessor.read_data_from_file(strFileName))
IO.currentData()

while True:
    # Show user a menu of options
    IO.menu()
    # Get user's menu option choice
    a = str(IO.userChoice())
    # Show user current data in the list of product objects
    if a == '1':
        IO.currentData()
    # Let user add data to the list of product objects
    elif a == '2':
        try:
            IO.addData()
        except:
            print(Exception('Please only enter STRING for \'Product Name\' and FLOAT for \'Product Price\'.'))
            continue
    # Let user save current data to file and exit program
    elif a == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print('Data saved. Goodbye!')
        break
    else:
        print('Please enter a valid menu choice.')

# Main Body of Script  ---------------------------------------------------- #

