#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. Functions
#     - Parameters: `**kwargs`, `*`, positional-only
#     - Scoping (LEGB)
#     - Inner functions
#     - Dispatch tables
# 2. Comprehensions
#     - List
#     - Set
#     - Dict
#     - Nested
# 3. Functional programming
#     - Functions as arguments
#     - `lambda`
# 4. Modules and packages

# In[1]:


# https://github.com/reuven
# https://github.com/reuven/dfend-2021-12Dec-adv1/blob/main/2021-12Dec-23.ipynb


# In[3]:


# positional -- 10, 20,30
# keyword  -- always in the form name=value
#     a=10, b=20 -- keyword arguments

def add(first, second):
    return first + second

add(10, 3)   # both positional


# In[4]:


add(first=1, second=2)   # both keyword


# In[5]:


add(1, second=2)   # first positional, then keyword


# In[6]:



def mysum(start, *args):
    total = start
    for one_number in args:
        total += one_number
    return total

mysum(10, 10, 20, 30)   # 10-> start, (10,20,30)->args


# In[8]:


# make start a keyword-only parameter

def mysum(*args, start):  # args gets all positional, start is keyword only
    total = start
    for one_number in args:
        total += one_number
    return total

mysum(10, 20, 30)   # error!  


# In[9]:


mysum(10, 20, 30, start=15)


# In[10]:


mysum([100, 200], [10, 20, 30], [40], start=[])


# In[12]:


# make start a keyword-only parameter

def mysum(*args, start=0):  # args gets all positional, start is keyword only with a default
    total = start
    for one_number in args:
        total += one_number
    return total

mysum(10, 20, 30)  


# In[13]:


help(sum)


# In[14]:


def myfunc(a, b, c):
    return f'{a=}, {b=}, {c=}'

myfunc(a=100, b=200, c=300)


# In[15]:


myfunc(a=100, b=200, c=300, d=400)


# In[16]:


# **kwargs -- keyword arguments -- kwargs always a dict!
# kwargs has all keyword pairs that no other parameter got

def myfunc(a, b, c, **kwargs):
    return f'{a=}, {b=}, {c=}, {kwargs=}'

myfunc(a=100, b=200, c=300, d=400, e=[10, 20, 30])


# In[17]:


def write_config(filename, **kwargs):
    with open(filename, 'w') as f:
        for key, value in kwargs.items():
            f.write(f'{key}:{value}\n')


# In[18]:


write_config('myconfig.txt', a=100, b=[20, 30, 40], c=123.456, d='hello')


# In[19]:


get_ipython().system('cat myconfig.txt')


# In[22]:


#           positional->filename
write_config('myconfig.txt', filename='a', x=100)


# # Exercise: XML writer
# 
# 1. Write a function called `xml` that takes several arguments:
#     - tag name
#     - text content between the open-close tags
#     - keyword arguments with attributes
# 2. The function should return a string with valid XML.
# 
# Example:
# 
# ```python
# xml('tagname')                   # <tagname></tagname>
# xml('tagname', 'a')              # <tagname>a</tagname>
# xml('tagname', 'a', x=100)       # <tagname x="100">a</tagname>
# xml('tagname', 'a', x=1, b=2)    # <tagname x="1" b="2">a</tagname>
# ```

# In[23]:


print('abc')
print('def')


# In[24]:


print('abc', end='***')
print('def')


# In[32]:


def xml(tagname, text='', **kwargs):
    attributes = ''
    
    for key, value in kwargs.items():
        attributes += f' {key}="{value}"'
    
    return f'<{tagname}{attributes}>{text}</{tagname}>'

xml('a')


# In[33]:


xml('a', 'b')


# In[34]:


xml('a' ,(xml('b', xml('c', 'hello'))))


# In[35]:


xml('a', 'b', x=100, y=200)


# # Parameter types
# 
# 1. Mandatory (positional or keyword)
# 2. Optional (positional or keyword)
# 3. `*args` (all remaining positional)  **OR** `*` if we don't want `*args`
# 4. Keyword-only (mandatory)
# 5. Keyword-only (optional)
# 6. `**kwargs` (all remaining keywords)

# In[39]:


def add(*args, first, second):
    return first + second

add(first=10, second=3)   # all must be keyword-only!


# In[40]:


add(10, 3)


# In[41]:


def add(*, first, second):    # just a * means: after here, all are keyword-only
    return first + second

add(first=10, second=3)   # all must be keyword-only!


# In[ ]:





# # Parameter types
# 
# 0. Positional-only before `/`
# 1. Mandatory (positional or keyword)
# 2. Optional (positional or keyword)
# 3. `*args` (all remaining positional)  **OR** `*` if we don't want `*args`
# 4. Keyword-only (mandatory)
# 5. Keyword-only (optional)
# 6. `**kwargs` (all remaining keywords)

# In[43]:


help(sum)


# In[44]:


help(len)


# In[45]:


sum(iterable=[10, 20, 30])


# In[47]:


def xml(tagname, text='', /, **kwargs):
    attributes = ''
    
    for key, value in kwargs.items():
        attributes += f' {key}="{value}"'
    
    return f'<{tagname}{attributes}>{text}</{tagname}>'

xml('a', tagname='thing')


# In[49]:


def add(first, second):
    return first + second

t = (10, 2)

add(*t)    # unrolling


# In[52]:


d = {'a':1, 'b':2, 'c':3}

xml('mytag', 'mytext', **d)    # turns the dict into keyword arguments


# In[54]:


list(d)


# In[55]:


xml('mytag', 'mytext', *d) 


# # Scoping

# In[57]:


for i in range(10):
    print(i, end=' ')
    x = i


# In[58]:


x


# In[59]:


i


# In[60]:


x = 100

print(f'x = {x}')  # is x global? YES, 100


# # Python has 4 scopes:
# 
# - `L` Local (start here, if we're in a function body)
# - `E` Enclosing
# - `G` Global (start here if *not* in a function body)
# - `B` Builtin

# In[61]:


'x' in globals() 


# In[64]:


x = 100

def myfunc():
    print(f'In myfunc, x = {x}') # is x local? NO.  is x global? YES, 100

print(f'Before, x = {x}')  # is x global? YES, 100
myfunc()
print(f'After, x = {x}')  # is x global? YES, 100


# In[63]:


myfunc.__code__.co_varnames


# In[65]:


def otherfunc():
    myfunc()   # is myfunc local? NO. is myfunc global? YES
    
otherfunc()    


# In[66]:


x = 100

def myfunc():
    x = 200
    print(f'In myfunc, x = {x}')  # is x local? YES, 200

print(f'Before, x = {x}')  # is x global? YES, 100
myfunc()
print(f'After, x = {x}')  # is x global? YES, 100


# In[67]:


myfunc.__code__.co_varnames


# In[68]:


x = 100

def myfunc():
    print(f'In myfunc, x = {x}') # is x local? YES
    x = 200   # hoisting problem

print(f'Before, x = {x}')  
myfunc()
print(f'After, x = {x}')  


# In[69]:


x = 100

def myfunc():
    x += 1   # x = x + 1
    print(f'In myfunc, x = {x}') 

print(f'Before, x = {x}')  
myfunc()
print(f'After, x = {x}')  


# In[70]:


def add_one(x):
    x.append(1)

mylist = [10, 20, 30]
add_one(mylist)
mylist


# In[75]:


x = 100
y = [10, 20, 30]

def myfunc():
    global x
    x = 200
    y[0] = '!'
    print(f'In myfunc, x = {x}') 

print(f'Before, x = {x}')    
myfunc()
print(f'After, x = {x}') 
print(f'After, y = {y}')


# In[72]:


myfunc.__code__.co_varnames


# In[77]:


import __main__ 

x = 100

def myfunc():
    __main__.x = 200     # instead of global!
    print(f'In myfunc, x = {x}') 

print(f'Before, x = {x}')    
myfunc()
print(f'After, x = {x}') 


# In[78]:


list('abcd')


# In[79]:


dict(a=1, b=2)


# In[80]:


sum([10, 20, 30])


# In[81]:


sum = 5   # I create a new global variable, sum!  blocks access to __builtins__.sum


# In[82]:


sum([10, 20, 30])


# In[85]:


dir(__builtin__)


# In[88]:


__builtins__.sum([10, 20, 30])


# In[89]:


del(sum)  # delete the global sum


# In[90]:


sum([10, 20, 30])


# In[91]:


del(sum)


# In[92]:


t = (10, 20)
t


# In[93]:


t = 10, 20
t


# In[94]:


x = 100
y = 200

x,y = y,x


# In[95]:


x


# In[96]:


y


# In[97]:


def outer():
    def inner():
        return 'Hello from inner!'
    return inner

func = outer() 


# In[98]:


type(func)


# In[99]:


func()


# In[100]:


id(func)


# In[101]:


func = outer()
id(func)


# In[102]:


outer.__code__.co_varnames


# In[103]:


def outer(x):        # closure
    def inner(y):
        return f'Hello from inner, {x=}, {y=}'
    return inner

func = outer(10)    # x is 10


# In[105]:


func(20) 


# In[107]:


def outer(x):        # closure
    counter = 0

    def inner(y):
        nonlocal counter
        counter += 1
        return f'{counter} Hello from inner, {x=}, {y=}'
    return inner

func = outer(10)
func(5)


# In[108]:


func(6)


# In[109]:


func(7)


# In[110]:


func1 = outer(10)
func2 = outer(20)


# In[111]:


func1(100)


# In[112]:


func1(200)


# In[113]:


func(300)


# In[114]:


func1(400)


# In[115]:


func2(555)


# In[118]:


outer.__code__.co_cellvars  # what variables does the outer function need to store/keep?


# In[117]:


func1.__code__.co_freevars   # what variables are in the enclosing/outer function?


# In[119]:


nonlocal x


# In[120]:


def foo():
    nonlocal x
    x = 5


# # Exercise: make_password_maker
# 
# 1. Write `make_password_maker`, which takes a string, and returns a function
# 2. The returned function takes an int argument, and returns a string
# 
# `random.choice` 
# 
# 
# ```python
# make_alpha_password = make_password_maker('abcdefg')
# make_alpha_password(5)   # returns 5 random characters from 'abcdefg'
# make_alpha_password(10)  # returns 10 random characters from 'abcdefg'
# 
# make_symbol_password = make_symbol_password('!@#$%^&*()')
# make_symbol_password(5)   # returns 5 random characters from the above
# ```

# In[122]:


import random
random.choices('abc', k=10)


# In[125]:


import random

def make_password_maker(s):
    def make_password(n):
        return ''.join(random.choices(s, k=n))
    return make_password

make_alpha_password = make_password_maker('abcdefg')
make_alpha_password(10)   # returns 10 random characters from 'abcdefg'


# In[126]:


import random

def make_password_maker(s, forbidden=''):
    for one_character in forbidden:
        if one_character in s:
            raise ValueError(f'Pool of character s contains {one_character}')

    def make_password(n):
        return ''.join(random.choices(s, k=n))
    return make_password

make_alpha_password = make_password_maker('abcdefg', forbidden='efg')


# In[127]:


import random

def make_password_maker(s, min_digits=0, min_symbols=0):

    def make_password(n):
        new_password = ''.join(random.choices(s, k=n))
        
        # check digits
        digit_count = 0
        symbol_count = 0
        for one_character in new_password:
            if one_character.isdigit():
                digit_count += 1
            if one_character in '!@#$%':
                symbol_count += 1
                
        if digit_count < min_digits:
            raise ValueError('Illegal password; not enough digits')
            
        if symbol_count < min_symbols:
            raise ValueError('ILlegal password: not enough symbols')
        
    return make_password

make_alpha_password = make_password_maker('abcdefg', forbidden='efg')


# In[128]:


def a():
    return 'A!'

def b():
    return 'B!'

while True:
    s = input('Enter choice: ').strip()
    
    if not s:
        break
        
    elif s == 'a':
        print(a())
        
    elif s == 'b':
        print(b())
        
    else:
        print(f'Unknown {s}')


# In[129]:


def a():
    return 'A!'

def b():
    return 'B!'

# dispatch table
funcs = {'a':a,
         'b':b}

while True:
    s = input('Enter choice: ').strip()
    
    if not s:
        break
        
    elif s in funcs:
        print(funcs[s]())

    else:
        print(f'Unknown {s}')


# # Exercise: Calculator
# 
# 1. Write two functions, `add` and `mul`, that perform addition and multiplications.  Put them in a dispatch table dict.
# 2. Ask the user, repeatedly, to enter a math expression, with two numbers and an operator.
# 3. If the user gives us an empty string, exit.
# 4. Otherwise, look up, and execute, the appropriate function from the dict.
# 
# Example:
# 
#     Enter expression: 2 + 2
#     2 + 2 = 4
#     Enter expression: 10 * 5
#     10 * 5 = 50
#     Enter expression: 10 / 2
#     10 / 2 is not recognized
#     Enter expression: [ENTER]
#     [exits]

# In[132]:


def add(first, second):
    return first + second

def mul(first, second):
    return first * second

funcs = {'+':add,
        '*':mul}

while s := input('Enter expression: ').strip():
        
    if s.count(' ') != 2:
        print('Enter a valid expression!')
        continue

    first, op, second = s.split()  # splits on ' ', \t, \n, \r, \v
    
    if op in funcs:
        result = funcs[op](int(first), int(second))
        
    else:
        result = 'Unsupported'
        
    print(f'{first} {op} {second} = {result}')
        


# # Comprehensions

# In[133]:


numbers = range(10)

squares = []

for one_number in numbers:
    squares.append(one_number ** 2)
    
squares    


# In[135]:


# list comprehension

[one_number ** 2              # SELECT
 for one_number in numbers]   # FROM 


# In[136]:


mylist = ['ab', 'cde', 'fg']

'*'.join(mylist)


# In[137]:


mylist = [10, 20, 30]

'*'.join(mylist)


# In[138]:


'*'.join([str(one_item)
         for one_item in mylist])


# In[139]:


s = 'this is a bunch of words for my python class'

s.title()


# In[140]:


s.capitalize()


# In[143]:


# if I don't have str.title, can I implement it with str.capitalize

' '.join([one_word.capitalize()
 for one_word in s.split()])


# In[144]:


[print(one_word)
for one_word in s.split()]


# # Exercises: List comprehensions
# 
# 1. Ask the user to enter a string with numbers, separated by spaces, and sum them.
#      - If they enter '10 20 30', we print 60.
# 2. Ask the user to enter a sentence. Count the non-whitespace characters in the string.
#     - If they enter 'hello world', we print 10.

# In[145]:


s = input('Enter numbers: ')


# In[151]:


sum([int(one_number)
 for one_number in s.split()])


# In[ ]:


s = input('Enter sentence: ').strip()


# In[155]:


sum([len(one_word)
 for one_word in s.split()])


# In[159]:


# I want a list with all usernames

[one_item.split(':')[0]                  # SELECT
 for one_item in open('/etc/passwd')    # FROM
 if not one_item.startswith('#') ]        # WHERE


# In[160]:


# https://files.lerner.co.il/advanced-exercise-files.zip
# files.lerner.co.il


# In[163]:


get_ipython().system('cat nums.txt')


# # Exercise: Sum the numbers
# 
# Sum the numbers in `nums.txt`.  You can assume that each line contains either no numbers or one number.

# In[164]:


get_ipython().run_line_magic('pwd', '')


# In[174]:


sum([int(one_line)
 for one_line in open('nums.txt')
 if one_line.strip().isdigit()  ])


# In[168]:


int()


# In[169]:


int('5')


# In[170]:


int('     5       ')


# In[171]:


int('')


# In[172]:


int('\n')


# In[ ]:





# # Next up
# 
# 1. Comprehensions with functions
# 2. Set comprehensions
# 3. Dict comprehensions
# 4. Nested comprehensions
# 5. `lambda`
# 6. Modules + packages

# In[175]:


get_ipython().system('head shoe-data.txt')


# # Exercise: Shoe data
# 
# Based on the file `shoe-data.txt`, create a list of dicts. Each line in the file has three columns, separated by `'\t'`: brand, color, and size.
# 
# ```python
# [
#     {'brand':'Adidas', 'color':'orange', 'size':'43'},
#     {'brand':'Nike', 'color':'black', 'size':'41'},
#     ...
# 
# ]
# 
# ```

# In[176]:


# files.lerner.co.il  -- advanced Python files


# In[180]:


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand':brand,
           'color':color,
           'size':size}


[line_to_dict(one_line)
for one_line in open('shoe-data.txt')]


# In[192]:


def line_to_dict(one_line):
    return dict(zip(['brand', 'color', 'size'],
                   one_line.strip().split('\t')))

[line_to_dict(one_line)
for one_line in open('shoe-data.txt')]


# In[182]:


d = {'a':1, 'b':2, 'c':3}


# In[183]:


d.items()


# In[184]:


a = [('a', 1), ('b', 2), ('c', 3)]


# In[185]:


dict(a)


# In[187]:


list(zip('abc', [10, 20, 30]))


# In[191]:


list(zip('abc', [10, 20, 30, 40], strict=True))


# In[193]:


# set

s = {10, 20, 20, 30, 40, 50}
s


# In[194]:


20 in s


# In[196]:


# make sure each result is only once

set([one_number ** 2
 for one_number in range(-5, 5)])


# In[197]:


# set comprehension
{one_number ** 2
 for one_number in range(-5, 5)}


# In[198]:


# add all of the different numbers entered by the user
s = input('Enter numbers: ').strip()


# In[200]:


sum([int(one_number)
 for one_number in s.split()])


# In[201]:


{int(one_number)
 for one_number in s.split()}


# In[202]:


sum({int(one_number)
 for one_number in s.split()})


# In[204]:


get_ipython().system('head -20 linux-etc-passwd.txt')


# # Exercise: Unique shells
# 
# Find the unique (different) shells in `linux-etc-passwd.txt`.

# In[207]:


[one_line
for one_line in open('linux-etc-passwd.txt')
if not one_line.startswith('#') and one_line.strip()]


# In[212]:


{one_line.split(':')[-1].strip()
for one_line in open('linux-etc-passwd.txt')
if not one_line.startswith(('#', '\n'))}


# In[213]:


from collections import Counter

c = Counter([one_line.split(':')[-1].strip()
for one_line in open('linux-etc-passwd.txt')
if not one_line.startswith(('#', '\n'))])


# In[214]:


c.most_common()


# In[215]:


# dict comprehension -- creates one dict

s = 'this is a bunch of words'

{   one_word : len(one_word)
  for one_word in s.split()
}


# In[216]:


d = {'a':1, 'b':2, 'c':3}

{ value : key
 for key, value in d.items() }


# In[217]:


d = {'a':1, 'b':2, 'c':3, 'x':2}

{ value : key
 for key, value in d.items() }


# In[218]:


get_ipython().system('cat myconfig.txt')


# In[219]:


{ one_line.split(':')[0]   :    one_line.split(':')[1].strip()
 for one_line in open('myconfig.txt') }


# In[225]:


{ fields[0]   :   fields[1] 
 for one_line in open('myconfig.txt') 
 if (fields := one_line.strip().split(':')) }


# In[226]:


mylist = [[10, 15, 20],
         [25, 30, 35, 40, 45, 50],
         [60, 70, 80, 85],
         [90, 100, 110, 120, 130, 140, 150]]

mylist


# In[227]:


[one_item
 for one_item in mylist]


# In[228]:


[one_item
 for one_sublist in mylist
 for one_item in one_sublist]


# In[229]:


[one_item
 for one_sublist in mylist
 if len(one_sublist) > 3
 for one_item in one_sublist]


# In[230]:


[one_item
 for one_sublist in mylist
 if len(one_sublist) > 3
 for one_item in one_sublist
 if one_item % 2 ]


# In[231]:


[one_number
 for one_number in range(10)
 if one_number % 2
 if one_number < 5]


# In[232]:


get_ipython().system('head movies.dat')


# # Exercise: Movie categories
# 
# Reading from `movies.dat`, what are the five most popular genres?

# In[233]:


get_ipython().system('file movies.dat')


# In[234]:


f = open('movies.dat', encoding='utf-8')


# In[235]:


s = f.read()


# In[238]:


from collections import Counter

c = Counter([one_genre
 for one_line in open('movies.dat', encoding='utf-8')
 for one_genre in one_line.split('::')[-1].strip().split('|')])

c.most_common(5)


# In[242]:


import random

random.seed(0)
numbers = [random.randint(0, 100)
             for i in range(10)]
numbers


# In[243]:


numbers.sort()  # run the sort method on a list


# In[244]:


numbers   # the list is changed!


# In[245]:


numbers = numbers.sort()   # DO NOT DO THIS!
print(numbers)


# In[246]:


# sorted, builtin function

random.seed(0)
numbers = [random.randint(0, 100)
             for i in range(10)]

sorted(numbers)   # we get a new, sorted list back


# In[247]:


numbers


# In[248]:


numbers = sorted(numbers)
numbers


# In[249]:


sorted(numbers, reverse=True)


# In[251]:


random.seed(0)
numbers = [random.randint(-50, 50)
          for i in range(10)]
numbers


# In[252]:


sorted(numbers)


# In[253]:


# TimSort
# 
# A < B

# cmp(A, B)

# f(A) < f(B)

# The "key" param expects to get  a function
# the function takes *one* argument

sorted(numbers, key=abs)


# In[254]:


words = 'This is a sentence for my Python course'.split()

sorted(words)


# In[255]:


sorted(words, key=str.lower)


# In[256]:


def by_loud_lower(one_word):
    print(f'Now checking {one_word}')
    return one_word.lower()

sorted(words, key=by_loud_lower)


# In[257]:


def line_to_dict(one_line):
    return dict(zip(['brand', 'color', 'size'],
                   one_line.strip().split('\t')))

shoes = [line_to_dict(one_line)
         for one_line in open('shoe-data.txt')]


# In[258]:


shoes


# # Exercise: Sorting shoes
# 
# 1. Sort the shoes by size
# 2. Sort the shoes -- first by brand, then by size
# 3. Ask the user by which field they want to sort (brand, color, size) and sort by that.

# In[259]:


sorted(shoes)


# In[260]:


# sort by size

def by_size(shoe_dict):
    return shoe_dict['size']

sorted(shoes, key=by_size)


# In[261]:


# sort by brand, then size

def by_brand_and_size(shoe_dict):
    return shoe_dict['brand'], shoe_dict['size']
    
sorted(shoes, key=by_brand_and_size)    


# In[262]:


d = {'c':10, 'e':3, 'a':-5, 'b':30, 'd':-2}

for key, value in d.items():
    print(f'{key}: {value}')


# In[263]:


# sort by key

for key, value in sorted(d.items()):
    print(f'{key}: {value}')


# In[264]:


# sort by value

def by_value(t):
    return t[1]

for key, value in sorted(d.items(), key=by_value):
    print(f'{key}: {value}')


# In[267]:


# ask the user how they want to sort

sort_field = input('Enter sort field: ').strip()

def by_user_sort_field(shoe_dict):
    return shoe_dict[sort_field]

sorted(shoes, key=by_user_sort_field)


# In[270]:


# ask the user how they want to sort

sort_field = input('Enter sort field: ').strip()

def by_field(sort_field):
    def by_user_field(shoe_dict):
        return shoe_dict[sort_field]
    return by_user_field

sorted(shoes, key=by_field(sort_field))


# In[ ]:


# sort by value

def by_value(t):
    return t[1]

for key, value in sorted(d.items(), key=by_value):
    print(f'{key}: {value}')


# In[271]:


def square(x):
    return x ** 2


# In[273]:


# anonymous function 

lambda x: x**2


# In[274]:


(lambda x: x**2)(5)


# In[276]:


# sort by value

# lambda in Python:
# (1) only one line
# (2) only one expression
# (3) no assignment, for loops, if-else

for key, value in sorted(d.items(), key=lambda t: t[1]):
    print(f'{key}: {value}')


# In[277]:


import operator

operator.add(5, 3)


# In[278]:


operator.sub(10, 7)


# In[280]:


# itemgetter returns a function that runs [] on its argument

operator.itemgetter(1)


# In[281]:


for key, value in sorted(d.items(), key=operator.itemgetter(1)):
    print(f'{key}: {value}')


# In[284]:


# ask the user how they want to sort

sort_field = input('Enter sort field: ').strip()

def my_itemgetter(index):
    def inner(data):
        return data[index]
    return inner

sorted(shoes, key=my_itemgetter(sort_field))


# In[285]:


# ask the user how they want to sort

sort_fields = input('Enter sort fields: ').split()

def my_itemgetter(*indexes):   # closure   
    def inner(data):
        return [data[one_index]
               for one_index in indexes]
    return inner

sorted(shoes, key=my_itemgetter(*sort_fields))


# In[286]:


by_brand_and_size = my_itemgetter('brand', 'size')


# In[287]:


by_brand_and_size(shoes[0])


# In[288]:


by_brand_and_size(shoes[50])


# In[289]:


sorted(shoes, key=operator.itemgetter(*sort_fields))


# In[290]:


def apply_to_filenames(func, *filenames):
    return [func(one_filename)
           for one_filename in filenames]

def get_file_length(one_filename):
    total = 0
    for one_line in open(one_filename):
        total += len(one_line)
    return total

apply_to_filenames(get_file_length, 
                   '/etc/passwd', 'infile0.txt', 'infile1.txt')


# In[294]:


# map 
list(map(get_file_length, 
         ['/etc/passwd', 'infile0.txt', 'infile1.txt']))


# In[295]:


from functools import reduce

reduce(lambda total, current: total + current,
       [1,2,3], 
       0 )      # total for the first iteration


# In[296]:



reduce(lambda total, current: total * current,
       [1,2,3], 
       1 )      # total for the first iteration


# # Next time
# 
# 1. Modules
# 2. Objects
#     - Class
#     - Attributes
#     - ICPO
#     - Inheritance
#     - Magic methods
#     - Properties
#     - Descriptors
