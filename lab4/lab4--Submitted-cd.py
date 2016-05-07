#Junjie Lin 25792830 and Taylor Baudoin 14166069 ICS 31 Lab sec 5.  Lab asst 4.

#c
#3.25--------------
def postive_integer(n:int):
    '''print the first four multiple of n'''
    print (n*0)
    print (n*1)
    print (n*2)
    print (n*3)
postive_integer(5)

#3.26---------------
def integer(n:int):
    '''print the squares of all number from 0 up to'''
    for i in range(n):
        print (i**2)
integer(4)
integer(7)

#d
#d.1---------------
from collections import namedtuple

Dish=namedtuple('Dish','name price calories')
d1=Dish('Pizza',10,200)
d2=Dish('Sandwich',5,150)
d3=Dish('Yogurt',2,100)

d4=Dish('Pasta',15,500)
d5=Dish('Burger',9,600)
d6=Dish('Ice cream',3,100)
d7=Dish('Coffee',4,150)
d8=Dish('Rice',6,180)
d9=Dish('Cake',7,160)

#d.2--------------
def Dish_str(a:Dish)->str:
    '''return a string in this form: Paht Woon Sen ($9.50): 330 cal
    '''
    return(a.name+"  (${:2.2f})".format(a.price)+ ": {:2.0f}".format(a.calories)+' cal')
print (Dish_str(d1))
print (Dish_str(d2))

#d.3--------------
def Dish_same(b:Dish, c:Dish)->bool:
    '''returns True if the names of the two dishes and their calorie counts are equal
    '''
    return (b.calories==c.calories)
assert(Dish_same(d1,d2) == False)
assert(Dish_same(d1,d3) == False)
assert(Dish_same(d2,d3) == False)
print (Dish_same(d6,d4))
print (Dish_same(d7,d2))
print ('444444444444444')
#d.4--------------
def Dish_change_price(a:Dish,b:int)->Dish:
    
    return Dish(a.name,(a.price)+((a.price)*b/100) ,a.calories)
print (Dish_change_price(d1,100))
print (Dish_change_price(d2,-50))  
print ('55555')
#d.5--------------
def Dish_is_cheap(a:Dish,n:int)->bool:
    '''return True if the Dish's price is less than that number (and False otherwise)
    '''
    return a.price<n
assert(Dish_is_cheap(d7,5)==True)
print(Dish_is_cheap(d1,5))
print(Dish_is_cheap(d1,11))
print ('6666')
#d.6----------------
DL=[d1,d2,d3,d4,d5]
DL2=[d6,d7,d8,d9]
DL.extend(DL2)
print(DL)

def Dishlist_display(a:list)->str:
    '''return one large string consisting of the string representation of each dish followed by a newline ('\n') character.
    '''
    DL=''
    for i in a:
        DL=DL+'Name:'+i.name+'  Price:${:2.2f}'.format(i.price)+'  Calories:{:2.0f}cal'.format(i.calories) +'\n'
    return DL
print(Dishlist_display(DL))
print (Dishlist_display(DL2))
print ('7777')
#d.7--------------------
def Dishlist_all_cheap(a:list,b:int)->bool:
    '''return True if the price of every dish on the list is less than that number
    '''
    result=[]
    for i in a:
        result.append(Dish_is_cheap(i,b))
    return(False not in result)
assert (Dishlist_all_cheap(DL,10)==False)
print (Dishlist_all_cheap(DL,21))
print (Dishlist_all_cheap(DL,14))
print ('888')
#d.8------------------
def Dishlist_change_price(a:list,b:int)->list:
    '''return the list of Dishes with each price changed by the specified amount
    '''
    DL3=[] 
    for i in a:
       DL3.append(Dish_change_price(i,b))
    return DL3
Dishlist_change_price(DL,100),'should be double the price'
Dishlist_change_price(DL,-50),'should be half of the price'
print ('999')
#d.9-------------------
def Dishlist_prices(a:list)->list:
    '''return a list of numbers containing just the prices of the dishes on that list
    '''
    result=[]
    for i in a:
        result.append(i.price)
    return result
print (Dishlist_prices(DL))
print ('101010')
#d.10----------------------
def Dishlist_average(a:list)->int:
    '''return the average price of those dishes
    '''
    result=[]
    answer=[]
    for i in a:
        result.append(i.price)
    answer=sum(result)/len(result)
    return (answer)
print (Dishlist_average(DL))
print ('1111111')
#d.11------------------
def Dishlist_keep_cheap(c:list, b:int)->list:
    '''return a list of those dishes on the original list that have prices less than that number
    '''
    result=[]
    for i in c:
        if i.price<b:
            result=result + [i]
    return(result)
print (Dishlist_keep_cheap(DL,10))
        
print ('1212')        
#d.12-----------------
def  before_and_after():
    '''print the result of Dishlist_display on the big list of restaurants you've already defined in your file; then it changes all the prices of the restaurants on the big list; then it prints the result of Dishlist_display again
    '''
    response=input('Price Change:')
    print(Dishlist_display(DL))
    print(Dishlist_display(Dishlist_change_price(DL,int(response))))
before_and_after()






