import os
os.system("clear")

# Variables
sales = []

saleStatus=True
addProducts=True
totalSales=0
validation=True
number=0

# Program
print("Welcome to the inventory management system")  #Welcome message
print("--------------------------------")
while saleStatus:   #Loop to add products to the sale
    while validation:
        name=input("Please, Enter the product name: ").lower().strip()  #Enter the product name and converts everything to lowercase
        if name:    #Verify that the user has entered something
            break
        else: print("Error! You must enter a product.") 

    while validation:   #Loop to validate the price and quantity inputs
        try:
            price=float(input("Please, Enter the product value: ")) #Enter the product price and converts in float
            if price<=0: #Verify that the value is greater than 0
                print()
                print("The price must be greater then zero")
                print()
                continue
            break 
        except ValueError:  #Verifies that the user has entered a numeric value
            print()
            print("Error: Please enter a valid numeric value")
            print()

    while validation:   #Loop to validate the price and quantity inputs
        try:
            quantity=float(input("Please, Enter the quantity of the product: "))    #Enter the product quantity and converts in float
            break 
        except ValueError:  #Verifies that the user has entered a numeric value
            print()
            print("Error: Please enter a valid numeric value")
            print()

    #Check if the user is entering a product that is already registered
    foundProduct=False
    for sale in sales:
        if sale["name"] == name :
            sale["quantity"] += quantity
            foundProduct=True
            print(f"Updated quantity")
            print()

    if not foundProduct:    #If the product does not exist, it is added to the list
        sale={
        "name" : name,
        "price" : price,
        "quantity" : quantity
        }

        sales.append(sale)

        print("product added successfully!")
        print()   

    print("Partial summary")
    for sale in sales:
        subTotalSale = sale["price"] * sale["quantity"]
        number+=1
        print(f"Product {number}: {sale["name"].capitalize()} | Value: ${sale["price"]} | Quantity: {sale["quantity"]} | Total: ${subTotalSale}")   #
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
    addProducts=True

print("Total Sale")
print("--------------------------------")

#Print the products added to the sale and calculate the total sale
for sale in sales:
    subTotalSale = sale["price"] * sale["quantity"]
    number+=1
    print(f"Product {number}: {sale["name"].capitalize()} | Value: ${sale["price"]} | Quantity: {sale["quantity"]} | Total: ${subTotalSale}")   #
    totalSales += subTotalSale

number=0
    
#Print the total sale    
print(f"Total sale is: ${totalSales}")
print("--------------------------------")
print("Thank you for your purchase!")
