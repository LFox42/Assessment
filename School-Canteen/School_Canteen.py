
#School Canteen

#Ver 1.0: Create bottle server, create classes
#Ver 2.0: Create HTML for 
#Ver 3.0: Add Purchase/Restock pages
#Ver 4.0: Add restock imput



from bottle import run, route, view, get, post, request, static_file

###Class START WITH CAPITAL LETTERS

class Food:
    
    # _ signifies a private variable. not to be used outside of this class.

    
    def __init__(self, name, image, amount): 
        #not passing ID as we want it to create it.

        self.name = name
        self.image = image
        self.amount = amount


#Data on products in stock.
store_test = [
    Food("Sushi Roll Pack", "image", 5),
    Food("Hot Dog and Chips", "image", 12),
    Food("Ham and Cheese Sandwiches", "image",4),
    ]

curr_food = None #store_test[0]
#Pages

#Store page
@route('/')
@view ('Purchase_Page')
def Purchase():
    #buy and restock Product
    data = dict (store_list = store_test)
    return data

#the purshase was successful.
@route('/purchase-success/<food_name>')
@view('purchase-success')
def purchase_success(food_name):
    #removes 1 food    
    found_food = None
    for food in store_test:
        if food.name == food_name:
            found_food = food
    data = dict (food = found_food)
    found_food.amount = found_food.amount - 1
    return data

#to input the amount to restock
@route('/restock/<food_name>')
@view('restock')
def Restock(food_name):
    global curr_food
    found_food = None
    for food in store_test:
        if food.name == food_name:
            found_food = food    
    curr_food = found_food

#to restock the inputted amount
@route('/restock_success', method="POST")
@view('restock_success')
def restock_success():
    amount = request.forms.get('amount')
    curr_food.amount += int(amount)
    return dict(food = curr_food)



#address to main page (localhost:8080)
run(host='0.0.0.0', port = 8080, reloader=True, debug=True)