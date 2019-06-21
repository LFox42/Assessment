#School Canteen

#Ver 1.0: Create bottle server, create classes
#Ver 2.0: Create HTML for 
#Ver 3.0: Add Purchase/Restock pages


from bottle import run, route, view, get, post, request, static_file
from itertools import count

###Class START WITH CAPITAL LETTERS

class Food:
    
    # _ signifies a private variable. not to be used outside of this class.
    _ids = count (0)
    
    def __init__(self, name, image, amount): 
        #not passing ID as we want it to create it.
        self.id = next(self._ids)
        self.name = name
        self.image = image
        self.amount = amount


#Data on products in stock.
store_test = [
    Food("Sushi Roll Pack", "image", 5),
    Food("Hot Dog and Chips", "image", 12),
    Food("Ham and Cheese Sandwiches", "image",4),
    ]

#Pages

#Store page
@route('/')
@view ('Purchase_Page')
def Purchase():
    #buy and restock product
    data = dict (store_list = store_test)
    return data

@route('/purchase-success/<food_id>')
@view('purchase-success')
def purchase_success(food_id):
    #removes 1 food
    food_id = int(food_id)
    found_food = None
    for food in store_test:
        if food.id == food_id:
            found_food = food
    data = dict (food = found_food)
    found_food.amount = found_food.amount - 1
    return data


#address to main page (localhost:8080)
run(host='0.0.0.0', port = 8080, reloader=True, debug=True)