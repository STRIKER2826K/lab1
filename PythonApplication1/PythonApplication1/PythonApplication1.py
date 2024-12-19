
from Hotel import Hotel  
try:
    name = input("Name: ")  
    allplace_value = input("Number of seats: ")
    allplace = int(allplace_value)  
    ocplace_value = input("Number of occupied places: ")
    ocplace = int(ocplace_value)  
    price_value = input("Price: ")
    from decimal import Decimal
    price = Decimal(price_value)
    
    if ocplace <= allplace:
        ht = Hotel(name, allplace, ocplace, price)  
        rev = ht.revenue()
        print(rev)  
    else:
        print("Ocplace > Allplace")
except Exception as ex:
    print(f"Error: {ex}")
