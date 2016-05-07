

#Junjie Lin 25792830 and Balkaran Gill 78114430. ICS 31 lab 5, assignment 5.
__author__ = 'dgk'

# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 c: Change prices for the dishes served
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='c':
            b=eval(input('please enter a specified amount by which to change the current price: '))
            C= Collection_change_prices1(C,b)
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")

#########################################
#### Dishes
from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')

def Dish_get_info() -> Dish:
    """ Prompt user for fields of Dish; create and return.
    """
    return Dish(
        input("Please enter the dish's name:  "),
        float(input("Please enter the price of that dish:  ")),
        float(input("Please enter the number of calories of that dish:  ")))

def Dish_str(self1: Dish)-> str:
    '''Returns the dishes in the given form'''
    b = ''
    b = ('      Dish:   '+'Name:'+ self1.name +
         "   Price:${:2.2f}".format(self1.price) + "   Calories:{:2.0f}".format(self1.calories)+'cal')
    return b

##########################################
from collections import namedtuple

Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
Dish = namedtuple('Dish','name price calories')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])	


#C.1
r3 = Restaurant ('Pascal', 'French', '940-752-0107',[Dish('Escargots', 12.95, 250),
                                                     Dish('Poached Salmon', 18.50, 550),
                                                     Dish('Rack of Lamb', 24.00, 850)])
print ('----Collection_change_prices1 by a special parameter(100:double price)-------')
def Dish_change_price(a:Dish,b:int)->Dish:
    '''Takes dish and returns dish with price increased by a special parameter'''    
    return Dish(a.name,(a.price)+((a.price)*b/100) ,a.calories)

def Dishlist_change_price(a:list,b:int)->list:
    '''Takes list of dishes (menu) and returns the list with the price of each dish increased by a special parameter'''
    DL3=[] 
    for i in a:
       DL3.append(Dish_change_price(i,b))
    return DL3

     
def Restaurant_change_prices1(r:Restaurant,b:int)->Restaurant:
    '''Takes all the restaurants and increases price of every dish on menu by a special parameter and returns all the Restaurant with new price'''
    return r._replace(menu=Dishlist_change_price(r.menu,b))

def Collection_change_prices1(a:list,b:int)->list:
    '''Takes all the restaurants and increases price of every dish on menu by a special parameter and returns all the Restaurant with new price'''
    result=[]
    for i in a:
        result.append(Restaurant_change_prices1(i,b))
    return result

###########################################

##### Restaurant
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', Menu)
        
def Restaurant_str(self: Restaurant) -> str:
    a = ''
    a =(
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:" + "\n") 
    for m in self.menu:
         a = a + Dish_str(m) + "\n"
    return a

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter())
    
def Restaurant_change_price(R: Restaurant,m:float)-> Restaurant:
    r1= Restaurant(R.name, R.cuisine, R.dish, R.phone, R.price + R.price * m/100)
    return(r1)

#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]

def Collection_remove_all(C: list) -> list:
    '''Removes all Restaurants in the collection.'''
    C = []
    return C
                          
def Collection_change_price(C: list,m:float) -> list:
    result = []
    for r in C:
        result.append(Restaurant_change_price(r,m))
    return result

###########################################
#### Menus
def Menu_enter():
    Menu = []
    while True:
        response=str(input("Would you like a new dish added? Please enter yes/no: "))
        if response=='yes':
            Menu.append(Dish_get_info())
        elif response=='no':
            break
    return Menu
##########################################
restaurants()



