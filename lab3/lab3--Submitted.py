5


#Junjie Lin 25792830 and Leon Hsu 7437984. ICS 31 Lab sec 5.  Lab asst 3.

# c

print('Part c----')

# Exercise 3.17

print('Exercise 3.17---')
      
a, b, c, = 3, 4, 5

# a

if a < b:
    print('ok')

# b

if c < b:
    print('ok')

#c

if (a+b) == c:
    print('ok')

#d

if (a+b)**2 == c:
    print('ok')

# Exercise 3.18

print('Exercise 3.18----')

# a

if a < b:
    print('ok')
else:
    print('NOT OK')

# b

if c < b:
    print('ok')
else:
    print('NOT OK')

#c

if (a+b) == c:
    print('ok')
else:
    print('NOT OK')

#d

if (a+b)**2 == c:
    print('ok')
else:
    print('NOT OK')

# Exercise 3.19

print('Exercise 3.19------')

first = ['January', 'February', 'March']

for month in first:
    print(month[0:3])

# Exercise 3.20

print('Exercise 3.20----')

first = [2, 3, 4, 5, 6, 7, 8, 9]

for h in first:
    if (h**2)%8 == 0:
        print(h)

# d.1

print('Problem d.1------')

def is_vowel(n:str)->bool:
    '''Shows if the sring has a vowel'''
    
    return n in 'aeiouAEIOU'

print (is_vowel('b')), '''should be False'''
print (is_vowel('a')), '''should be True'''
print (is_vowel('O')), '''should be True'''



#d.2

print('Problem d.2---')
      
def print_nonvowels(d:str)-> str:
    '''Removes all the vowels in a string'''

    for b in d:
        if is_vowel(b) == False:
            print(b)

print('break')
print_nonvowels('break')
print('towel')
print_nonvowels('towel')
print('apple')
print_nonvowels('apple')

#d.3

print('Problem d.3-----')

def nonvowels(d:str)-> str:
    '''Removes all the vowels in a string'''
    
    result = ''
    for b in d:
        if is_vowel(b) == False:
            result = result + b
    return result
assert(nonvowels('hello') == 'hll')

print('hello')
print(nonvowels('hello'))
print('cake')
print(nonvowels('cake'))
print('cream pie')
print(nonvowels('cream pie'))
print(nonvowels('I am number 1'))

#d.4

print('Problem d.4----')

def is_vowel2(n:str)->bool:
    '''Shows if the sring has a vowel'''
    
    return n in 'aeiouAEIOU 0123456789'

def consonants(d:str)->str:
    '''Returns all the consonants in a string'''

    result = ''
    for b in d:
        if is_vowel2(b) == False:
            result = result + b
    return result

assert(consonants('hello world') == 'hllwrld')

print(consonants('Hello 2 guys'))
print(consonants('My partner is th3 b3st'))

#d.5

print('Problem d.5-----')

def vowels(d:str)->str:
    '''Returns all the vowels in a str'''
    
    result = ''
    for b in d:
        if is_vowel(b) == True:
            result = result + b
    return result

def select_letters(n:str, b:str)->str:
    '''Returns all the vowels or consonants of the second string'''

    if n == 'v':
        return vowels(b)
    elif n == 'c':
        return  consonants(b)
    else:
        return ''
assert(select_letters('c', 'Hello') == 'Hll')
print(select_letters('v', 'Hello'))
print(select_letters('c', 'Hello'))
print(select_letters('d', 'Hello'))  # Empty line

#d.6

print('Problem d.6-----')

def hide_vowels(d:str)->str:
    '''Replaces all the vowels with hyphens'''
    
    result = ''
    for b in d:
        if is_vowel(b) == True:
            result = result + '-'
        elif is_vowel(b) == False:
            result = result + b
    return result
            

print(hide_vowels('Hello'))
print(hide_vowels('stop'))
print(hide_vowels('banana'))


#e

#Exercise 3.22

print('Excercise 3.22----')

def not_secret(d:list)->str:
    '''Prints the list that isn't secret'''

    for b in d:
        if b != 'secret':
            print(b)
not_secret(['cia','secret','mi6','isi','secret'])

#Exercise 3.23

print('Exercise 3.23----')

def print_A_M(d:list)->str:
    '''Only print names that start with A-M'''

    for b in d:
        if b[0] in 'ABCDEFGHIJKLM':
            print(b)

print_A_M(['Ellie','Steve','Sam','Owen','Gavin'])

#Exercise 3.24

print('Exercise 3.24----')

def first_last(d:list)->int:
    '''Prints first and last element of the list'''

    print('The first list element is', d[0])
    print('The last list element is', d[-1])

    
first_last([3,5,7,9])

#f

from collections import namedtuple

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number,
#	best dish, price of that dish

R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]

#f.1

print('f.1---')

def alphabetical(d:list)->list:
    '''Makes the list alphabetical order by name'''

    RL.sort()
    print(RL)

alphabetical(RL)

#f.2

print('f.2----')

def alphabetical_names(d:list)->str:
    '''Returns a list of the names of all restaurants'''

    RL.sort()
    for b in d:
        print(b.name)

alphabetical_names(RL)

#f.3

print('f.3-----')

def all_Thai(d:list)->list:
    '''Returns a list of all the Thai restaurants in a list)'''

    for b in d:
        if b.cuisine == 'Thai':
            print(b.name)

all_Thai(RL)

#f.4

print('f.4------')

def select_cuisine(d:list, n:str)->list:
    '''Takes a list of restaurants and a str cuisine and returns restaurants that serve it'''

    for b in d:
        if b.cuisine == n:
            print(b.name)

select_cuisine(RL,'Indian')

#f.5

print('f.5------')

def select_cheaper(d:list, n:float)->list:
    '''Returns a list of restaurants whose price is less than the specified number'''

    for b in d:
        if b.price < n:
            print(b.name)
print('< 15.00')
select_cheaper(RL, 15.00)
print('< 5.00')
select_cheaper(RL, 5.00)

#f.6

print('f.6-----')

def average_price(g:list)->float:
    '''Returns the average price of the list'''

    total = 0
    for h in g:
        total = total + h.price
    avg = total/len(g)
    return avg

print(average_price(RL))

#f.7

print('f.7------')

def select_cuisine1(d:list, n:str)->list:
    '''Takes a list of restaurants and a str cuisine
    and returns a LIST restaurants that serve it'''
    g = []
    for b in d:
        if b.cuisine == n:
            g.append(b)
    return g
      
print(average_price(select_cuisine1(RL, 'Indian')))

#f.8

print('f.8------')

print(average_price(select_cuisine1(RL, 'Chinese'))
      + average_price(select_cuisine1(RL, 'Thai')))

#f.9

print('f.9-----')
def select_cheaper1(d:list, n:float)->list:
    '''Returns a list of restaurants whose price is less than $15.00'''

    for b in d:
        if b.price < n:
            print(b.name)

select_cheaper1(RL, 15.00)


            


    










