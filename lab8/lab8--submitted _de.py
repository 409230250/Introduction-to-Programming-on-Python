# Junjie Lin 25792830 and Khang Tran 47508988. ICS 31 Lab sec. 5. Lab asst 8.

# c) is in the other file.

from collections import namedtuple
from random import *
import random
NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4  # 3 choices is A/B/C, 4 choices is A/B/C/D, 5 is A/B/C/D/E

# d.1)

def random_answers()-> str:
    ''' Generates and returns a string of letters representing the correct answers to the test.
    '''
    choices = ['A','B','C','D']
    result= ''
    for i in range(NUMBER_OF_QUESTIONS):
        answer = random.randrange(0,NUMBER_OF_CHOICES)
        result += choices[answer]
    return result
ANSWERS = random_answers()

# d.2)

Student = namedtuple('Student', 'name answers')
def file_o_r_c(t: "textfile") -> str:
    ''' Takes a textfile that is opened, read to a string, closed, and
       returned as a string.'''
    infile = open(t)
    content = infile.read()
    infile.close()
    return content

def extract_names_and_properly_capitalize(s: str) -> list:
    ''' Takes a string and returns a list of strings consisting
       of the names in the form Firstname Lastname.'''
    result = []
    for element in s.split():
        if element.isalpha():
            result.append(element.capitalize())
    return result

def random_names(n: int) -> list:
    ''' Takes an integer and returns a list with that many strings,
       with each string a randomly generated name.'''
    result = []
    surnames = file_o_r_c("surnames.txt")
    female_names = file_o_r_c("femalenames.txt")
    male_names = file_o_r_c("malenames.txt")
    surnames_list = extract_names_and_properly_capitalize(surnames)
    F_and_M_namelist = extract_names_and_properly_capitalize(female_names) + extract_names_and_properly_capitalize(male_names)
    for i in range(n):
        result.append(F_and_M_namelist[randint(0, len(F_and_M_namelist) - 1)]
                      + " " + surnames_list[randint(0, len(surnames_list) - 1)])
    return result

def random_students() -> list:
    ''' Generates and returns a list of Student namedtuples.
    '''
    result = [ ]
    for s in range(NUMBER_OF_STUDENTS):
        result.append(Student(random_names(1), random_answers()))
    return result

# d.3)

Student = namedtuple('Student', 'name answers scores total')
def random_students() -> list:
    ''' Generates and returns a list of Student namedtuples.
    '''
    result = [ ]
    for s in range(NUMBER_OF_STUDENTS):
        a = random_answers()
        score = [ ]
        total = 0
        for i in range(NUMBER_OF_QUESTIONS):
            if a[i] == ANSWERS[i]:
                score.append(1)
                total += 1
            else:
                score.append(0)
        result.append(Student(random_names(1), a, score, total))
    return result
stud = random_students()

def Student_total(s: Student) -> int:
    ''' Return the Student's total score.
    '''
    return s.total

stud.sort(key=Student_total, reverse=True)
print("Top 10 Students")
print(stud[:10])
t_scores = 0
for t in stud:
    t_scores += t.total
print("Mean Score")
print(t_scores/NUMBER_OF_STUDENTS)

# d.4)

def generate_weighted_student_answer(s: str) -> str:
    ''' Takes a string representing the correct answer and returns a string representing the randomly chosen weighted student answer.
    '''
    choices = ['A','B','C','D']
    r = random.randint(0, NUMBER_OF_CHOICES*2)
    if r == 0:
        pass
    else:
        for i in range(r):
            choices.append(s)
    answer = random.randrange(0,(NUMBER_OF_CHOICES + r))
    return(choices[answer])  

def random_answers2():
    ''' Generates and returns a string of letters representing the correct answers to the test.
    '''
    result= ''
    for i in range(NUMBER_OF_QUESTIONS):
        result += generate_weighted_student_answer(ANSWERS[i])
    return result

def random_students2():
    ''' Generates and returns a list of Student namedtuples with weighted answers.
    '''
    result = [ ]
    for s in range(NUMBER_OF_STUDENTS):
        a = random_answers2()
        score = [ ]
        total = 0
        for i in range(NUMBER_OF_QUESTIONS):
            if a[i] == ANSWERS[i]:
                score.append(1)
                total += 1
            else:
                score.append(0)
        result.append(Student(random_names(1), a, score, total))
    return result

stud = random_students2()
stud.sort(key=Student_total, reverse=True)
print("Top 10 Cheaters")
print(stud[:10])
t_scores = 0
for t in stud:
    t_scores += t.total
print("Rigged Mean Score")
print(t_scores/NUMBER_OF_STUDENTS)

# d.5)

def question_weights(l:list) ->list:
    ''' Takes a list of Student records and returns a list of numbers,
    one number for each question on the test, where each number is the
    number of students who answered that question incorrectly. '''
    weights = []
    for i in range(NUMBER_OF_QUESTIONS):
        point = 0
        for student in l:
            if student.scores[i] == 0:
                point += 1
        weights.append(point)
    return(weights)
weight = question_weights(stud)
# print(weight)

def Student_weighted_score(s: Student) ->Student:
    ''' Takes a Student record and uses the list of question weights
    to return that Student record with its total field changed to reflect
    that student's score based on his or her correct answers and the
    corresponding question weights. '''
    newtotal = 0
    s = Student(s.name, s.answers, s.scores, newtotal)
    for i in range(len(s.scores)):
        if s.scores[i] == 1:
            newtotal += weight[i]
    s = Student(s.name, s.answers, s.scores, newtotal)
    return(s)

for i in range(len(stud)):
    stud[i] = Student_weighted_score(stud[i])
stud.sort(key=Student_total, reverse=True)
print("Top 10 Cheaters with Curves")
print(stud[:10])
t_scores = 0
for t in stud:
    t_scores += t.total
print("Rigged Mean Score with Curves")
print(t_scores/NUMBER_OF_STUDENTS)

# 6.21

def ticker(s: 'Name of file') -> str:
    infile = open(s)
    counter = 0
    companies = {}
    for line in infile:
        counter += 1
        if (counter%2 == 1):
            key = line.strip()
        else:
            value = line.strip()
            companies[key] = value
    infile.close()
    while True:
        co = input('Enter Company name: ')
        if co in companies.keys():
            print('Ticker symbol: ' + companies[co])
        else:
            break
ticker('nasdaq.txt')

# 6.26

days = {'Mo':'Monday',
        'Tu':'Tuesday',
        'We':'Wednesday',
        'Th':'Thursday',
        'Fr':'Friday',
        'Sa':'Saturday',
        'Su':'Sunday'}

def week():
    ''' Repeatedly asks the user to enter an abbreviation
    for a day of the week, then prints the corresponding day. '''
    while True:
        a=input('Enter day abbreviation: ')
        if a in days.keys():
            print(days[a])
        else:
            break
week()

#6.25

c=[[1,2],[2,3],[3,4]]
b=[[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]]
a=[[1,0,1],[0,1,0]]

def different(table:list) ->int:
    ''' Takes a two-dimensional table as input and returns the number
    of distinct entries in the table. '''
    result=[]
    for lst in table:
        for number in lst:
            result.append(number)
            result=list(set(result))
    return len(result)
assert(different(a)==2)
assert(different(b)==10)
assert(different(c)==4)

# 6.30

def simul(n: int) ->str:
    ''' Takes an input integer n and simulates n rounds of Rock, Paper, Scissors
    between two players. The player who wins the most rounds wins the n-round
    game, with ties possible. '''
    p1 = 0
    p2 = 0
    rounds = 0
    while rounds != n:
        a = random.randint(1,3)
        b = random.randint(1,3)
        if (a == 1) and (b == 3):
            p1 += 1
        elif (b == 1) and (a == 3):
            p2 += 1
        elif a > b:
            p1 += 1
        elif a < b:
            p2 += 1
        rounds += 1
    if p1 > p2:
        print('Player 1')
    elif p1 < p2:
        print('Player 2')
    else:
        print('Tie')

simul(5)
