import os
os.system("clear")

from add_products import addProduct
from show_inventory import showInventory
from calculate_statitics import calculateStatitics

# Variables
menu = """Options: 
1. Add product
2. Show inventory
3. Calculate statistics
4. Exit
"""

Inventory = []
saleStatus=False
addProducts=False
program = True
totalSales=0
validation=True
number=0

print("Welcome to the inventory management system")
# Program
while program :
    print("-----------------------------------------")

    try:
        option = int(input(menu + "Please, choose an option: "))
        if option == 1 :
            print()
            addProduct ()
            

        elif option == 2 :
            print()
            showInventory ()
            print()

        elif option == 3 :
            print()
            calculateStatitics ()

        elif option == 4 :
            program = False

        else :
            print("Invalid option. Try again")
            print()
            
    except ValueError:
        print("Error! Type a number")
        print()
         

        '''print("Partial summary")
        for sale in Inventory:
            subTotalSale = sale["price"] * sale["quantity"]
            number+=1
            if sale["quantity"] == 0:
                print(f"Product {number}: {sale["name"].capitalize()} | No hay exixtensias")   #    
            else:
                print(f"Product {number}: {sale["name"].capitalize()} | Value: ${sale["price"]} | Quantity: {sale["quantity"]}")   #        
            
            totalSales += subTotalSale
        
        number=0
        print(f"Subtotal: $ {totalSales}")

        totalSales=0
        print()

        while addProducts:  
            addProduct=input("Want add more product? (Yes) or (No): ").lower()  #Ask the user if they want to add more products to the sale
            print()
            if addProduct == "yes":
                addProducts=False
            elif addProduct == "no":
                saleStatus=False
                addProducts=False
            else:
                print("--------------------------------")
                print("Invalid option, try again, type (yes) or (no)")  #If the user enters an invalid option, it will ask again
        addProducts=True'''

    '''print("Total Inventory")
    print("--------------------------------")

    #Print the products added to the sale and calculate the total sale
    for sale in Inventory:
        subTotalSale = sale["price"] * sale["quantity"]
        number+=1
        if sale["quantity"] == 0:
            print(f"Product {number}: {sale["name"].capitalize()} | No hay exixtensias")   #    
        else:
            print(f"Product {number}: {sale["name"].capitalize()} | Value: ${sale["price"]} | Quantity: {sale["quantity"]}")   #        
        
        totalSales += subTotalSale
        '''
    
print("--------------------------------")
print("Thank you for your purchase!")