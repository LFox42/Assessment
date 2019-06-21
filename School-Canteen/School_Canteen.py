

#School Canteen

#Ver 1.0: Create bottle server, create classes



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


#Test Data
store_test = [
    Food("Sushi Roll Pack", "image", 5),
    Food("Hot Dog and Chips", "image", 12),
    Food("Ham and Cheese Sandwiches", "image",4),
    ]

#Pages

#index page
@route('/')
@view ('index')
def index():
    #need this function to attach the decorators above.
    pass


#address to main page (localhost:8080)
run(host='0.0.0.0', port = 8080, reloader=True, debug=True)