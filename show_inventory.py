from add_products import inventory

def showInventory():
    number=0
    products=inventory()
    subTotalSale=0

    
    print("Inventory")
    print("--------------------------------")
    for product in products:
        subTotalSale = product["price"] * product["quantity"]
        number += 1
        if product["quantity"] == 0:
            print(f"Product {number}: {product["name"].capitalize()} | No hay exixtensias")
        else:
            print(f"Product {number}: {product["name"].capitalize()} | Value: ${product["price"]} | Quantity: {product["quantity"]}")

    return subTotalSale
    