validation = True
Inventory = []

def addProduct ():
    
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
    for sale in Inventory:
        if sale["name"] == name :
            '''i=sales.index(sale)'''   #Opcion para borrar un producto
            sale["quantity"] += quantity
            '''if sale["quantity"] == 0:
                del sales [i]'''        #Opcion para borrar un producto
            foundProduct=True
            print(f"Updated quantity")
            print()

    if not foundProduct:    #If the product does not exist, it is added to the list
        sale={
        "name" : name,
        "price" : price,
        "quantity" : quantity
        }

        Inventory.append(sale)

        print("product added successfully!")
        print()

def inventory():
    return Inventory
