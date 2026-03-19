from add_products import inventory

def total():
    Inventory=inventory()
    totalSales=0

    print()

    #Print the products added to the sale and calculate the total sale
    for products in Inventory:
        subTotalSale = products["price"] * products["quantity"]
        '''number+=1
        if products["quantity"] == 0:
            print(f"Product {number}: {products["name"].capitalize()} | No hay exixtensias")   #    
        else:
            print(f"Product {number}: {products["name"].capitalize()} | Value: ${products["price"]} | Quantity: {products["quantity"]}")   #        '''
        
        totalSales += subTotalSale
    
    print("-----------------------------------------")
    print(f"Total sales: $ {totalSales}")
    print()

def quantityOfProducts():
    Inventory=inventory()
    
    Quantity=len(Inventory)
    
    print("-----------------------------------------")
    print(f"Quantity of products: {Quantity}")
    print()


def calculateStatitics():
    menu="""Options:
    1. Show the total sales
    2. Show the quanqity products
    3. Exit
    """
    Options=True

    while Options :
        try:
            option = int(input(menu + "Please, choose an option: "))
            if option == 1 :
                total ()
                print("--------------------------------")

                

            elif option == 2 :
                print()
                quantityOfProducts()
                print("--------------------------------")


            elif option == 3 :
                Options = False
                print()

            else :
                print("Invalid option. Try again")
                print()
                
        except ValueError:
            print(" Error! Type a number")
            print()