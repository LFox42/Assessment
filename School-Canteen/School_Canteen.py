

#Build log for Sign up web page
#Ver 1.1 - Created TEST data for Ticket variable
#Ver 1.2 - Adding server functionality to python


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

#index page
@route('/')
@view ('index')
def index():
    #Display information
    data = dict (comic_list = comic_test)
    return data


run(host='0.0.0.0', port = 8080, reloader=True, debug=True)