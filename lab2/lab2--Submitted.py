#Junjie Lin 25792830 and Hong Zhou 83966257. ICS 31 Lab Sec 5. Lab TA Yi.

from collections import namedple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Mee Krob", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Stracotto", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

#c.1
print (RC[2][0])
print (RC[2].name)
#c.2
print (RC[0][1]==RC[3][1])
print (RC[0].cuisine ==RC[3].cuisine)
#c.3
print (RC[6][-1])
print (RC[-1].price)
#c.4
RC.sort()
print(RC)

#c.5
RCbest_dish=["Mee Krob","Mee Krob","Stracotto","Stracotto","Jambalaya","Birch Sap","Yesiga Tibs"]
RCbest_dish.sort ()
print (RCbest_dish[-1])

#c.6
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]
RC.sort ()
print (RC[0], RC[1], RC[-2], RC [-1])

#d
#2.26
import turtle

s=turtle.Screen()
t=turtle.Turtle()
print(t.left(90))
print(t.forward(100))
print(t.left(90))
print(t.forward(100))
print(t.left(90))
print(t.forward(100))
print(t.left(90))
print(t.forward(100))
s.bye()

#2.27
import turtle
s=turtle.Screen()
t=turtle.Turtle()
print(t.left(60))
print(t.forward(100))
print(t.left(60))
print(t.forward(100))
print(t.left(120))
print(t.forward(100))
print(t.left(60))
print(t.forward(100))
print(t.left(60))
s.bye()


#2.28
import turtle
s=turtle.Screen()
t=turtle.Turtle()
print(t.left(72))
print(t.forward(100))
print(t.left(72))
print(t.forward(100))
print(t.left(72))
print(t.forward(100))
print(t.left(72))
print(t.forward(100))
print(t.left(72))
print(t.forward(100))
print(t.left(72))
s.bye()

import turtle
s=turtle.Screen()
t=turtle.Turtle()
print(t.left(60))
print(t.forward(100))
print(t.left(60))
print(t.forward(100))
print(t.left(60))
print(t.forward(100))
print(t.left(60))
print(t.forward(100))
print(t.left(60))
print(t.forward(100))
print(t.left(60))
print(t.forward(100))
print(t.left(60))
s.bye()

import turtle
s=turtle.Screen()
t=turtle.Turtle()
print(t.left(51.42))
print(t.forward(100))
print(t.left(51.42))
print(t.forward(100))
print(t.left(51.42))
print(t.forward(100))
print(t.left(51.42))
print(t.forward(100))
print(t.left(51.42))
print(t.forward(100))
print(t.left(51.42))
print(t.forward(100))
print(t.left(51.42))
print(t.forward(100))
print(t.left(51.42))
s.bye()

import turtle
s=turtle.Screen()
t=turtle.Turtle()
print(t.left(45))
print(t.forward(100))
print(t.left(45))
print(t.forward(100))
print(t.left(45))
print(t.forward(100))
print(t.left(45))
print(t.forward(100))
print(t.left(45))
print(t.forward(100))
print(t.left(45))
print(t.forward(100))
print(t.left(45))
print(t.forward(100))
print(t.left(45))
print(t.forward(100))
print(t.left(45))
s.bye()

#2.29
import turtle
s=turtle.Screen()
t=turtle.Turtle()
print(t.circle(100))
print (t.penup())
print (t.goto(60,-90))
print(t.pendown())
print(t.circle(100))
print (t.penup())
print (t.goto(-60,-90))
print(t.pendown())
print(t.circle(100))
s.bye()

#2.32
import turtle
s=turtle.Screen()
t=turtle.Turtle()
print(t.circle(1))
print (t.penup())
print (t.goto(0,100))
print(t.pendown())
print(t.circle(109))
s.bye()

#e
import turtle
s=turtle.Screen()
t=turtle.Turtle()
print (t.pensize(1.5))
print (t.circle(60,60))
print (t.circle(60,-120))
print (t.circle(60,120))
print (t.left(60))
print (t.circle(60,120))
print (t.penup())
print (t.goto(0,30))
print (t.dot(30))
s.bye ()

#f
#3.36
def abbreviation (n:str):
    return (n[0]+n[1])
print (abbreviation('Tuesday'))
print (abbreviation('Monday'))
print (abbreviation('Sunday'))
print (abbreviation('Friday'))

#3.43
def distance (n:float):
    return (n*.34029)
print (distance(3))
print (distance(6))
print (distance(9))

#3.32
def pay (w: int, h: int):
    if h>=40 :   
        return ((w*40)+((h-40)*1.5*w))
    else:
        return (w*h)
print (pay(10,10))
print (pay(10,35))
print (pay(10,45))

#3.35
import math
def function_points (x1: int, y1: int, x2: int, y2: int):
    return (math.sqrt(((x2-x1)**2)+((y2-y1)**2)))
print (function_points(0,0,1,1))
print (function_points(0,0,0,1))

#3.44
def polygon (n:int):
    if n>=3:
        import turtle
        s=turtle.Screen()
        t=turtle.Turtle()
        for i in range (n):
            (t.left(360/n))
            (t.forward(100))
        s.bye()
print (polygon(4))
print (polygon(6))
print (polygon(7))
print (polygon(10))

#g.1
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]
def restaurant_price(n:str):
    return (n[-1])
print (restaurant_price(RC[0]))
print (restaurant_price(RC[1]))
print (restaurant_price(RC[-1]))

#g.2
def restaurant_price(n:str):
    return (n[-1])
RC.sort (key=restaurant_price)
print (RC)
print ('9.3--------')
#g.3
def costliest (n:str):
    return (n[-1])
RC.sort (key=restaurant_price)
print (costliest(RC[-1]))

print ('h---------')
#h
import turtle
s=turtle.Screen()
t=turtle.Turtle()

def draw_eye(x,y):
    t.setheading(0)
    t.pensize(1.5)
    t.penup()
    t.goto(x+80,y+190)
    t.pendown()
    t.circle(60,60)
    t.circle(60,y-120)
    t.circle(60,120)
    t.left(60)
    t.circle(60,120)
    t.penup()
    t.goto(x+80,y+220)
    t.dot(30)
    
draw_eye(1,2)
draw_eye(-150,2)

def draw_face(x,y):
    t.setheading(0)
    t.pensize(1.5)
    t.penup()
    t.goto(x+0,y+0)
    t.pendown()
    t.circle(200)
draw_face(1,2)


def draw_mouth(x,y):
    t.setheading(0)
    t.pensize(1.5)
    t.penup()
    t.goto(x+0,y+50)
    t.pendown()
    t.circle(100,60)
    t.circle(100,y-120)
draw_mouth(1,2)

def draw_nose(x,y):
    t.setheading(0)
    t.pensize(1.5)
    t.penup()
    t.goto(x-5,y+100)
    t.pendown()
    t.circle(30,80)
    t.left(60)
    t.circle(-40,70)
draw_nose(1,2)

def draw_tongue(x,y):
    t.setheading(0)
    t.pensize(1.5)
    t.penup()
    t.goto(x+20,y+50)
    t.pendown()
    t.right(60)
    t.forward(10)
    t.left(60)
    t.circle(60,50)
    t.left(60)
    t.forward(15)
draw_tongue(1,2)


import turtle
s=turtle.Screen()
t=turtle.Turtle()
def draw_eyebrow(x,y):
    t.setheading(0)
    t.pensize(1.5)
    t.penup()
    t.goto(x+80,y+265)
    t.pendown()
    t.circle(-120,20)
    t.circle(-120,-40)

draw_eyebrow(1,2)
draw_eyebrow(-150,2)

s.bye()
        

