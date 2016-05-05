# Junjie Lin 25792830 and Michael Punla 18147712. ICS 31 Lab sec 5.  Lab asst 1.

print(2*7)
print(3*9)
print(3**2)
print(100/3)
print(150-30)

14
27
9
33.333333333333336
120

#2.12
#(a)
print(1+2+3+4+5+6+7)
28

#2.13(b)
s1 = '-'
s2 = '+'
print (s1 + s2)
'-+'

#2.13(e)
print((s2 + (s1 * 2)) * 10 + s2)
'+--+--+--+--+--+--+--+--+--+--+'

#2.14
s = 'abcdefghiklmnopqrstuvwxyz'
print(s[0])
'a'
print(s[2])
'c'

#2.15
s ='goodbye'

#(a)
print (s[0] == 'g')
True

#(b)
print (s[6] == 'g')
False

#(c)
print (s[0] + s[1] == 'ga')
False

#2.16
#(a)
a=6

b=7


#(b)----------------------------------------------------------

c=(a+b)/2


#(c)
inventory = ['paper', 'staples', 'pencil']
print(inventory)


#(d)
first = 'John'
middle = 'Fitzgerald'
last = 'Kennedy'
print(first)
print(middle)
print (last)

#(e)
fullname = first + ' ' + middle + ' ' + last
print (fullname)
'John Fitzgerald kennedy'

#2.17
#(a)
print((17 + (-9)) < 10)
True

#(b)
print ((len('inventory') > 5 * len('fullname')))
False


#(c)
print(c <= 24)
True

#(d)
print (a<6.75<b)
True

#(e)
print((len(middle) > len(first) and len(middle) < len(last)))
False

#(f)
print((len(inventory) == 0 or len(inventory) > 10))
False

#2.18
#(a)
flowers = ['rose', 'bougainvillea', 'yucca', 'marigold', 'daylilly', 'lilly of the valley']
print(flowers)

#(b)

print (not 'potato' in flowers)
True

#(c)
thorny = [flowers[0], flowers[1], flowers[2]]
print(thorny)

#(d)
poisonous = [flowers[-1]]
print(poisonous)

#(e)
dangerous = thorny, poisonous
print(dangerous)

#2.21
s = ['t', 'o', 'p']
s.reverse()
print(s[0]+s[1]+s[2])
'pot'

#2.22
s = 'Michael Punla'
print(s[0] + s[8])

from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)
#(d.1)
print(still_another.title)

#(d.2)
print(another.price)

#(d.3)
print((favorite.price + another.price + still_another.price) / 3)

#(d.4)
print(favorite.year < 1900)

#(d.5)
print(still_another._replace(price = 26.00))

#(d.6)
print(still_another._replace(price = (25.00 * 1.20)))

#(e)
from collections import namedtuple
animal=namedtuple('animal','name species age weight food')
i=animal('Jumbo','elephant',50,1000,'peanuts')
ii=animal('Perry','platypus',7,1.7,'shrimp')

print (not i.weight<ii.weight)

#f
booklist = [favorite, another, still_another]

#(f.1)
print (favorite.price<another.price)

#(f.2)
print (not favorite.price>still_another.price)
