
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
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 e: Remove (erase) all the restaurants from the collection
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
        elif response=='n':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            a = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, a)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            a = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, a):
                print(Restaurant_str(r))
        elif response=='e':
            C = []
        elif response=='c':
            b=eval(input('please enter a specified amount by which to change the current price: '))
            C= Dishlist_change_price(C,b)
        else:
            invalid_command(response)


def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self
        .name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Dish:     " + self.dish + "\n" +
        "Price:    ${:2.2f}".format(self.price) + "\n\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        input("Please enter the name of the best dish:  "),
        int(input("Please enter the price of that dish:  ")))

def Dish_change_price(a:Restaurant,b:int)->Restaurant:
    return Restaurant(a.name, a.cuisine, a.phone, a.dish,a.price+((a.price)*b/100))


def Dishlist_change_price(a:list,b:int)->list:
    DL3=[] 
    for i in a:
       DL3.append(Dish_change_price(i,b))
    return DL3



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

restaurants()

























