#	5. Create a `Product` class with attributes `name`, `price`, and `stock`. 
# Write a method `check_availability(quantity)` that returns whether the 
# requested quantity is available.

class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    
    def check_availability(self,required):
        return self.stock>required
    

pro=Product("Phone",20000,100)
req=int(input("Enter the amount of the stock that is required: "))
if pro.check_availability(req):
    print('The requested quantity is available')
else:
    print('The requested quantity is not available')
    
