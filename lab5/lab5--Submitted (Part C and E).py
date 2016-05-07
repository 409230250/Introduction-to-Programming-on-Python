
#Junjie Lin 25792830 and Balkaran Gill 78114430. ICS 31 lab 5, assignment 5.
#C
from collections import namedtuple

Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
Dish = namedtuple('Dish','name price calories')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])	

print ('c.1')
#C.1
r3 = Restaurant ('Pascal', 'French', '940-752-0107',[Dish('Escargots', 12.95, 250),
                                                     Dish('Poached Salmon', 18.50, 550),
                                                     Dish('Rack of Lamb', 24.00, 850)])
print ('c.2---------')
#c.2
def Restaurant_first_dish_name(a:Restaurant)->str:
    '''Takes a Restaurant as its argument and returns the name of the first dish on the restaurant's menu
    '''
    b=a.menu
    return b[0].name
assert (Restaurant_first_dish_name(r2)=='Homard Bleu')
print(Restaurant_first_dish_name(r1))

print ('c.3-----------')
#c.3
def Restaurant_is_cheap(a: Restaurant, p:float)->bool:
    '''Returns True if the average price of the Restaurant's menu is less than or equal to the number
    '''
    result=[]
    answer=[]
    for i in a.menu:
        result.append(i.price)
    answer=sum(result)/len(result)
    return (answer<p)
print(Restaurant_is_cheap(r1,11)),'should be False'   
            
            
print ('c.4------------')
#c.4
R=[r1,r2,r3]
print ('-----------Collection_raise_prices by 2.50----------')
def Dish_raise_250(a:Dish)->Dish:
    '''Takes dish and returns dish with price increased by 2.50'''
    return Dish(a.name,((a.price)+ 2.50) ,a.calories)
print(Dish_raise_250(r1.menu[0]))

def Menu_raise_prices(m:list)->list:
    '''Takes list of dishes (menu) and returns the list with the price of each dish increased by 2.50'''
    result=[]
    for i in m:
        result.append(Dish_raise_250(i))
    return result
print(Menu_raise_prices(r1[-1]))

def Restaurant_raise_prices(r:Restaurant)->Restaurant:
    '''Takes restaurant and increases price of every dish on menu by 2.50 and returns Restaurant with new price'''
    return r._replace(menu=Menu_raise_prices(r.menu))
print(Restaurant_raise_prices(r1))

def Collection_raise_prices(a:list)->list:
    '''Takes all the restaurants and increases price of every dish on menu by 2.50 and returns all the Restaurant with new price'''
    result=[]
    for i in a:
        result.append(Restaurant_raise_prices(i))
    return result
print (Collection_raise_prices(R))

print ('----Collection_change_prices1 by a special parameter(100:double price)-------')
def Dish_change_price(a:Dish,b:int)->Dish:
    '''Takes dish and returns dish with price increased by a special parameter'''    
    return Dish(a.name,(a.price)+((a.price)*b/100) ,a.calories)
print (Dish_change_price(r1.menu[0],100))

def Dishlist_change_price(a:list,b:int)->list:
    '''Takes list of dishes (menu) and returns the list with the price of each dish increased by a special parameter'''
    DL3=[] 
    for i in a:
       DL3.append(Dish_change_price(i,b))
    return DL3
print(Dishlist_change_price(r1[-1],100))
     
def Restaurant_change_prices1(r:Restaurant,b:int)->Restaurant:
    '''Takes all the restaurants and increases price of every dish on menu by a special parameter and returns all the Restaurant with new price'''
    return r._replace(menu=Dishlist_change_price(r.menu,b))
print(Restaurant_change_prices1(r1,100))

def Collection_change_prices1(a:list,b:int)->list:
    '''Takes all the restaurants and increases price of every dish on menu by a special parameter and returns all the Restaurant with new price'''
    result=[]
    for i in a:
        result.append(Restaurant_change_prices1(i,b))
    return result
print (Collection_change_prices1(R,100))

#c.5

print ('-----------#c.3(Using the functions described above)------------')
def Restaurant_select_cheap(a: Restaurant, p:float)->Restaurant:
    for i in a.menu:
        if (Restaurant_is_cheap(a,p))== True:
            return a
print(Restaurant_select_cheap(r1,50))
print (Restaurant_select_cheap(r2,100))

def Collection_select_cheap (a:list,b:int)->list:
    '''Takes a Collection and a number and returns a list of all the Restaurants in the collection whose average price is less than or equal to that number'''
    result=[]
    for i in a:
        result.append(Restaurant_select_cheap(i,b))
    return result
print (Collection_select_cheap (R,50)),'should print out r1 and r3'
print (Collection_select_cheap (R,12)),'should print out r1'
print (Collection_select_cheap (R,100)),'should print out R'


#e
#4.13
s='abcdefghijklmnopqrstuvwxyz'
print(s[1:3]=='bc')
print(s[0:14]=='abcdefghijklmn')
print(s[14:26]=='opqrstuvwxyz')
print(s[1:25]=='bcdefghijklmnopqrstuvwxy')

#4.14
#a
log = '128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] "GET /docs/test.txt HTTP/1.0"'
#b
address = log.split()[0]
print(address)
#c
a = (log.find('12/Feb'))
b = (log.find(']'))
date = log[a:b]
print(date)

#4.19
first='Marlena'
last='Sigel'
middle='Mae'
#(a)
a='{}, {} {}'
print (a.format(last,first,middle))
#(b)
b='{}, {} {}.'
print (b.format(last,first,middle[0]))
#(c)

c='{} {}. {}'
print (c.format(first,middle[0],last))
#(d)
d='{}. {}. {}'
print (d.format(first[0],middle[0],last))

#4.23
def average():
    '''Return the average length of a word in the sentence'''
    a=input('Enter a sentence:')
    b=a.split()
    d=len(a)-a.count(' ')
    print (d/len(b))
average()

#4.25
from collections import namedtuple
Count = namedtuple('Count','letter number')
def letter_count(x:str,y:str)->Count:
    lst = []
    '''takes two strings and returns the counts of certain letters in the
first parameter, the second parameter is a string that specifies which
letters to count'''
    for i in y:
        C1 = Count(letter=i,number = x.count(i))
        lst.append(C1)
    return lst
print(letter_count('apple and orange','por'))







