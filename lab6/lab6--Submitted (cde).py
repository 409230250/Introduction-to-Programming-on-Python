##
##
##
##
###cancel print ('CDE')
###########
##
##
from random import randint
def roll() -> int:
    
    ''' Return a roll of two dice, 2-12
    '''
    die1 = randint(1, 6)
    die2 = randint(1, 6)
    n = die1 + die2
    return n

def repeat_roll(z:int) ->list:
    ''' takes the dice rolls and add them to a list'''
    v = []
    for i in range(z):
        p = roll()
        v.append(p)
    return v

print ('Distribution of dice rolls \n')

def count_roll(w: list):
    
    for i in range(2,13):
        for n in range(2,13):
            count = w.count(i)
            if i == n:
                print('{0:2}:'.format(n), '{0:6}'.format(count),
                      '({0:4.1f}%)'.format(count/len(w)*100),
                      ' {0:}'.format('*' * int(count/len(w)*100)))
    print ('-----------------\n    ',len(w),'rolls')                              
count_roll(repeat_roll(45666))

##
###d.1
##ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
##
##def Caesar_encrypt(a: str, key: int)->str:
##    result=''
##    w = str.maketrans(ALPHABET,ALPHABET[key:]+ALPHABET[:key]) 
##    result=a.translate(w)
##    return result
##assert(Caesar_encrypt('cat',2)=='ecv')
##
##def Caesar_decrypt(a:str,key:int)->str:
##    result=''
##    w = str.maketrans(ALPHABET,ALPHABET[-key:]+ALPHABET[:-key]) 
##    result=a.translate(w)
##    return (result)
##assert(Caesar_decrypt('ecv',2)=='cat')
##
###d.2
###d.3
##def Caesar_encrypt1(a: str, key: int):
##    result=''
##    newkey=key%26
##    w = str.maketrans(ALPHABET,ALPHABET[newkey:]+ALPHABET[:newkey]) 
##    result=a.translate(w)
##    return (result)
##assert(Caesar_encrypt1('cat',28)=='ecv')
##
##print('\n')
###e.1
##lst=[ "Four score and seven years ago, our fathers brought forth on",
##  "this continent a new nation, conceived in liberty and dedicated",
##  "to the proposition that all men are created equal.  Now we are",
##  "   engaged in a great 		civil war, testing whether that nation, or any",
##  "nation so conceived and so dedicated, can long endure.        " ]
##second=[ "Four score and seven years ago, our fathers brought forth on",
##  "this continent a new nation, conceived in liberty and dedicated",
##  "to the proposition that all men are created equal.  Now we are",
##  "   engaged in a great 		civil war, testing whether that nation, or any",
##  "nation so conceived and so dedicated, can long endure.        ",
##  "Four score and seven years ago, our fathers brought forth on",
##  "Four score and seven years ago, our fathers brought forth on",
##  "Four score and seven years ago, our fathers brought forth on",'', "nation so conceived and so dedicated, can long endure.        ",
##  "nation so conceived and so dedicated, can long endure.        ",'' ]
##
##def print_line_numbers(a:list):
##    
##    for i in range (0,len(a)):
##        print ('{0:3}:'.format(i+1),'{0:3}'.format(a[i]))
##print_line_numbers(lst)
##print('------------------------------------------')
###print('\n')
##print_line_numbers(second)
##
##print('\n')
###e.2
##def stats(a:list):
##    w=a.count('')
##    print('{:5}'.format(len(a)),'  lines in the list','\n',
##          '{:4}'.format(w),'  empty lines','\n',
##          '{:6.1f} {}'.format(len(str(a))/len(a), 'average characters per line'),'\n',
##          '{:6.1f} {}'.format(len(str(a))/(len(a)-w), 'avergage characters per non-empty line'))
##stats(lst)
###print('\n')
###stats(second)
##
##
###e.3
##def list_of_words(a:list)->list:
##    result=[]
##    for line in a:
##        words=line.split()
##        result2=[]
##        for i in words:
##            result2.append(i.strip('!@$%^&*(<>?/.,'))
##        result.extend(result2)
##    return result    
##'''
##print(list_of_words(lst)==['Four', 'score', 'and', 'seven', 'years',
##                           'ago', 'our', 'fathers', 'brought', 'forth',
##                           'on', 'this', 'continent', 'a', 'new', 'nation',
##                           'conceived', 'in', 'liberty', 'and', 'dedicated',
##                           'to', 'the', 'proposition', 'that', 'all', 'men',
##                           'are', 'created', 'equal', 'Now', 'we', 'are',
##                           'engaged', 'in', 'a', 'great', 'civil', 'war',
##                           'testing', 'whether', 'that', 'nation', 'or', 'any',
##                           'nation', 'so', 'conceived', 'and', 'so', 'dedicated',
##                           'can', 'long', 'endure'])
###print (list_of_words(second)) 
##
##'''
##
##
##
##
##
##
