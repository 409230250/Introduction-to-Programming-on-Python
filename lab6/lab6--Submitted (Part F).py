#Junjie Lin 25792830 and John Huynh 26096654. ICS 31 lab 5, assignment 6.

#if i dont put the menu, can i still print the list?
#

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

            
            n = input("How would you like to search for restaurants? \n Please enter 'sc' for specified cuisine \n Please enter 'dn' for Dish name \n")
            if n== 'sc':
                cuisine = input("What kind of cuisine would you like to search by? ")
                r_list = Collection_search_by_cuisine(C, cuisine)
                super_menu = []
                for r in r_list:
                    print(Restaurant_str(r))
                    super_menu.extend(r.menu)
                average_price = Restaurant_average_price(super_menu)
                print("Average price of all", cuisine, "dishes: ", "{:5.2f}".format(average_price))
            elif n == 'dn':
                dish_name = input("What dish name would you like to search for? ")
                for r in C:
                    if Restaurant_has_Dish_named(dish_name, r):
                        print(Restaurant_str(r))
            else:
                invalid_command(n)
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
    b = ('Dish: '+'Name:'+ self1.name +
         "   Price:${:2.2f}".format(self1.price) + "   Calories:{:2.0f}".format(self1.calories)+'cal')
    return b


##### Restaurant
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', Menu)
        
def Restaurant_str(self: Restaurant) -> str:
    
    a = ''
    a =('\n'+
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        
        "Phone:    " + self.phone + "\n" +
        "Menu:" + Menu_str(self.menu) +
        "     Average price: ${:4.2f}.  Average calories:{:4.0f}cal".format(Restaurant_average_price(self.menu), Restaurant_average_calories(self.menu)))
    
    return a
    

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter())
    
def Restaurant_change_price(R: Restaurant,m:int)-> Restaurant:
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
        if r.name == name:
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

def Collection_search_by_cuisine(C: list, cuisine: str) -> list:
    """ Return list of Restaurants in input list whose cuisine matches input string.
    """
    result = [ ]
    for r in C:
        if r.cuisine == cuisine:
            result.append(r)
    return result
##############Lab6 f.3
def Restaurant_has_Dish_named(name: str, r:Restaurant) -> bool:
    '''Returns True if Restaurant has a Dish containing given name.'''
    for dish in r.menu:
        if name in dish.name:
            return True
    return False

########################################## #Lab 5
from collections import namedtuple
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

def Menu_str(menu : list) -> str:
    '''Creates display string for menu of dishes'''
    
    info = '\n'
    for d in menu:
        info = info + '\t' + Dish_str(d) + "\n"
        
    return info
##########################################
def Restaurant_average_price(menu : list) -> float:
    '''Calculates average price of all Dishes on menu.'''
    total_price = 0
    for dish in menu:
        total_price += dish.price
    average_price = total_price/len(menu)
    return average_price


def Restaurant_average_calories(menu : list) -> float:
    '''Calculates average calories of all Dishes on Restaurant's menu.'''
    total_calories = 0
    for dish in menu:
        total_calories += dish.calories
    average_calories = total_calories/len(menu)
    return average_calories
##############################

restaurants()

