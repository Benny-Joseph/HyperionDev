
#========The beginning of the class==========
class Shoe:
    ''' In this function, you must initialise the following attributes:
                ● country,
                ● code,
                ● product,
                ● cost, and
                ● quantity.
            '''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity


    def get_cost(self):
    #    function to return the cost of the shoe in this method.
        return(self.cost)

    def get_quantity(self):
    #    Function to return the quantity of the shoes.
        return(self.quantity)

    def get_code(self):
    #    Function to return the code of the shoe in this method.
        return(self.code)

    def get_product_name(self):
    #    Function to return the product of the shoe in this method.
        return(self.product)

    def get_country(self):
    #    function to return the country of the shoe in this method.
        return(self.country)

    def __str__(self):
        # Add a code to returns a string representation of a class. MUST RETURN LIST OF ATTRIBUTES
        print(f"{str(self.country):^20}{str(self.code):^20}{str(self.product):^20}{str(self.cost):^20}"
              f"{str(self.quantity):^20}")

#=============Shoe list===========
# The list will be used to store a list of objects of shoes.

shoe_list = []

#==========Functions outside the class==============

# Function to read all shoe data from inventory.txt and save to shoe_list as list of Shoe Objects and return
def read_shoes_data():
    shoe_list = []
    try:
        inventory_file = open("inventory.txt", 'r+', encoding='utf-8')
        for line in inventory_file:  # - Read a line from the file. "South Africa,SKU44386,Air Max 90,2300,20"
            temp_list = line.split(",")  # - Split that line where there is comma.
            # - assign the items in the temp_list to attributes if Shoe class as per content/ position in txt file line
            country = temp_list[0].strip()
            prod_code = temp_list[1].strip()
            prod_name = temp_list[2].strip()
            prod_cost = temp_list[3].strip()
            prod_qty = temp_list[4].strip()

            # - Call constructor of Class Shoe to create onject
            shoe_obj = Shoe(country=country, code=prod_code, product=prod_name, cost=prod_cost, quantity=prod_qty)
            shoe_list.append(shoe_obj)

        shoe_list = shoe_list[1:]  # Skipping first line from file
        inventory_file.close()  # close the txt file after read operation is done
        return shoe_list

    except (FileNotFoundError):
        print("inventory.txt file not found")


# This function will take data from user about a shoe as arguments and use this data to create a shoe object
# and append this object inside the shoe_list.
def capture_shoes(country, code, product_name, cost, quantity):
    class_obj = Shoe(country=country, code= code, product= product_name, cost= cost, quantity= quantity)

    shoe_list.append(class_obj)

    output_str = "Country,Code,Product,Cost,Quantity\n"

    for i in range(0, len(shoe_list)):
        temp_str = ""
        country1 = shoe_list[i].get_country()
        code1 = shoe_list[i].get_code()
        product1 = shoe_list[i].get_product_name()
        cost1 = shoe_list[i].get_cost()
        quantity1 = shoe_list[i].get_quantity()
        output_str += f"{country1},{code1},{product1},{cost1},{quantity1}\n"

    write_txt_file("inventory.txt" , output_str)

# This function will iterate over the shoes_list and print the details of shoes using the __str__ function.
def view_all():
    print("\nDisplaying details of all Shoes in the inventory: \n")
    print(f"{'Country':^20}{'Product Code':^20}{'Product Name':^20}{'Cost':^20}{'Quantity':^20}\n")
    for shoe in shoe_list :
        shoe.__str__()


''' This function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked. 
    Ask the user if they want to add this quantity of shoes and then update it. 
    This quantity will be updated on the file for this shoe. '''
def re_stock():
    min_qty = int(shoe_list[0].get_quantity())
    min_object = shoe_list[0]
    for i in range(0,len(shoe_list)):
        if int(int(shoe_list[i].get_quantity()) <= min_qty) :
            min_qty = int(shoe_list[i].get_quantity())
            min_object = shoe_list[i]

    print(f"The details of shoe having lowest quantity in stock is as below :")
    print(f"{'Country':^20}{'Product Code':^20}{'Product Name':^20}{'Cost':^20}{'Quantity':^20}\n")
    min_object.__str__()

    while True :
        choice = input("Do you want to re-stock this shoe (Y/N): ").upper()
        if choice == 'Y':
            while True :
                try:
                    re_stock_qty = input("Please enter the quantity you want to order and add to this stock: ")
                    break
                except(Exception) :
                    print("Please enter integer values only to re-stock. Try again!!")

            str_re_stock_qty = str(int(min_object.get_quantity()) + int(re_stock_qty))

            old_str = f"{min_object.country},{min_object.code},{min_object.product},{min_object.cost},{min_object.quantity}\n"
            replace_str = f"{min_object.country},{min_object.code},{min_object.product},{min_object.cost},{str_re_stock_qty}\n"

            update_txt_file("inventory.txt" , old_str, replace_str)
            break

        elif choice == 'N':
            print("\n You have chosen not to re-stock this shoe. In-stock quantity remains low!!")
            break

        else:
            print("\n You have entered invalid choice!! ")



def search_shoe(search_code):
    '''  This function will search for a shoe from the list
         using the shoe code and return this object so that it will be printed.'''

    for shoe in shoe_list :
        if shoe.code == search_code:
            return shoe

    print(f"Shoe with code : {search_code} not found!!")



def value_per_item():
    '''This function will calculate the total value(= cost * quantity)  for each item
     and  display Shoe Code, Product Name , Value per item for all shoes in the inventory'''
    print(f"{'Shoe Code' : ^20} {'Product Name' : ^20} {'Value Per Item' : ^20}\n")
    for shoe in shoe_list :
        code = shoe.get_code()
        name = shoe.get_product_name()
        value = str(int(shoe.get_cost()) * int(shoe.get_quantity()))
        print(f"{code : ^20} {name : ^20} {value : ^20}")


def highest_qty():
    # Function to determine the product with the highest quantity and print this shoe as being for sale.

    max_qty = int(shoe_list[0].get_quantity())
    max_object = shoe_list[0]
    for i in range(0, len(shoe_list)):
        if int(int(shoe_list[i].get_quantity()) >= max_qty):
            max_qty = int(shoe_list[i].get_quantity())
            max_object = shoe_list[i]

    return max_object


# Function to write changes to txt file after each Edit.,  used while re-stocking
def update_txt_file(file_name, old_text, new_text) :
    ''' This function will take file_name, old_text and new_text as arguments, Open the file_name.txt ->
        read the whole file into string variable, In the string variable find and replace the old_text with
        the new_text, Then write the whole string back to the file'''

    with open(file_name, 'r+', encoding='utf-8') as read_file :
        whole_txt_file = read_file.read()

    whole_txt_file = whole_txt_file.replace(old_text , new_text)

    with open(file_name, 'w+', encoding='utf-8') as write_file :
        write_file.write(whole_txt_file)


# Function to write text to file used after adding new shoe details to shoe_list
def write_txt_file(file_name, text) :
    # This function will take file_name, text as arguments Open the file_name.txt -> write the whole string to the file

    with open(file_name, 'w', encoding='utf-8') as write_file :
        write_file.write(text)



#==========Main Menu=============
# - Code to display the options available to user and input response
menu = ""
while (menu != "0"):
    menu = input(f"\nSelect one of the following Options below:\n"
             f"        1 - Read Shoe Data\n"      # call read_shoe_data() to Read from file & create objects list
             f"        2 - Adding a Shoe\n"       # call capture_shoes() to input shoe data & add to object list
             f"        3 - View all Shoes\n"      # call view_all() and __str__ to print all shoes in list
             f"        4 - Re-Stock\n"            # call re_stock() to find min qty, input qty to add, write to file
             f"        5 - Search Shoe\n"         # call search_shoe() find using Code from list and display object
             f"        6 - Show Value per Item\n" # call value_per_item() display cost*qty for all shoes
             f"        7 - Show Highest Quantity\n" # call highest_qty() to find highest qty Shoe and put on sale
             f"        0 - Exit\n"
             f"       : ")

    if menu == '1':     # 1 - Read Shoe Data to Read from txt file & create objects list

        shoe_list = read_shoes_data()
        print("Inventory Data read successfully!!")


    elif menu == '2':  #  2 - Adding a Shoe : capture_shoes() to input shoe data & add to object list
        shoe_list = read_shoes_data()
        country = input("Enter Country name : ")
        code = input("Enter Product Code : ")
        product_name = input("Enter Product Name : ")
        cost = input("Enter per unit Cost of Product : ")
        quantity = input("Enter In-Stock Quantity of Product : ")

        capture_shoes(country, code, product_name, cost, quantity)

        print("Product added successfully!")

    elif menu == '3':   # 3 - View all Shoes:  view_all() through __str__ to print all shoes in list
        shoe_list = read_shoes_data()
        view_all()

    elif menu == '4':   # 4 - Re-Stock : re_stock() to find Shoe in min qty, input qty to add stock , write to file

        re_stock()

    elif menu == '5':   # 5 - Search Shoe : search_shoe() find Shoe using Code from list and display details of Shoe use __str__
        search_code = input("Enter Product Code of Shoe to display details : ")
        found_shoe = search_shoe(search_code) # shoe object returned as list
        # display details of found_shoe
        print(f"The details of shoe searched is as below :")
        print(f"{'Country':^12}{'Product Code':^12}{'Product Name':^12}{'Cost':^12}{'Quantity':^12}\n")
        found_shoe.__str__()

    elif menu == '6':   # 6 - Show Value per Item : value_per_item() display cost*qty for all shoes

        shoe_list = read_shoes_data()
        value_per_item()


    elif menu == '7':  # 7 - Show Highest Quantity" : highest_qty() to find highest qty Shoe and put on sale

        shoe_list = read_shoes_data()
        sale_shoe = highest_qty() # returns __str__ of shoe object

        print(f"The shoe with the following details is in highest in-stock quantity and should be put on SALE!!\n")
        print(f"{'Country':^20}{'Product Code':^20}{'Product Name':^20}{'Cost':^20}{'Quantity':^20}\n")
        sale_shoe.__str__()


    elif menu == "0":
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")

