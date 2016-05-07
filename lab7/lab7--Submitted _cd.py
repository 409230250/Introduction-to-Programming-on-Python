#  Michael Harris 29314351 and Junjie Lin 25792830.  ICS 31 Lab sec 5.  Lab asst 7.

# (c)
from random import randint
def generate_name() -> str:
    '''reads from a file, randomly selects a name, and returns the name'''
    infile = open('surnames.txt')
    rand_num = randint(0, 999)
    for index in range(rand_num):
        infile.readline()
    surname = (infile.readline()).split()[0]
    surname = surname.lower()
    surname = surname.capitalize()
    infile.close()
    gender = randint(0,1)
    if(gender == 0):
        infile = open('malenames.txt')
        rand_num = (randint(0, 999))
        for index in range(rand_num):
            infile.readline()
        first_name = (infile.readline()).split()[0]
        infile.close()
    else:
        infile = open('femalenames.txt')
        rand_num = randint(0, 999)
        for index in range(rand_num):
            infile.readline()
        first_name = (infile.readline()).split()[0]
        infile.close()
    first_name = first_name.lower()
    first_name = first_name.capitalize()
    return(first_name + ' ' + surname)
# print(generate_name())

def random_names(n: int) -> list:
    '''takes an integer and returns a list of that many strings,
       with each string a randomly generated name'''
    rand_list = []
    for i in range(n):
        rand_list.append(generate_name())
    return(rand_list)
#print(random_names(5))


# (d)
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def Caesar_encrypt(a: str, key: int):
    '''takes a string and an int for the key and returns the ciphertext
    '''
    result=''
    newkey=key%26
    w =str.maketrans(ALPHABET,ALPHABET[newkey:]+ALPHABET[:newkey]) 
    result=a.translate(w)
    return (result)
assert(Caesar_encrypt('cat',28)=='ecv')

def Caesar_decrypt(a:str,key:int)->str:
    '''takes a string and an int for the key and returns the plaintext
    '''
    result=''
    w = str.maketrans(ALPHABET,ALPHABET[-key:]+ALPHABET[:-key]) 
    result=a.translate(w)
    return (result)
assert(Caesar_decrypt('ecv',2)=='cat')

def Caesar_break(ciphertext: str) -> str:
    hit_count = 0
    plaintext = ''
    for i in range(26):
        plaintext2 = Caesar_decrypt(ciphertext,i)
        hit_count2 = decrypt_count(Caesar_decrypt(ciphertext,i))
        if hit_count2 >= hit_count:
            hit_count = hit_count2
            plaintext = plaintext2
    return plaintext

def decrypt_count(plaintext: str) -> int:
    wordcount = 0
    wordlist = plaintext.split()
    dictionary = open('wordlist.txt','r')
    dictionary_collection = dictionary.readlines()
    dictionary_list = []
    for line in dictionary_collection:
        dictionary_list.append(line.strip())
    for word in wordlist:
        if word in dictionary_list:
            wordcount += 1
    dictionary.close()
    return wordcount

assert(Caesar_break('ocz kvnnrjmy dn ht gvno ivhz')=='the password is my last name')


















