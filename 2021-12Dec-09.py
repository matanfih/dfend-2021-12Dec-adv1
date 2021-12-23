#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. Data structures
# 2. Functions
# 3. Functional programming
# 4. Modules + packages
# 5. Objects
# 6. Iterator + generators
# 7. Decorators
# 8. Threading, processes, asyncio
# 

# In[1]:


x = None


# In[2]:


type(x)


# In[4]:


if x == None:   # not Pythonic
    print('Yes, it is None!')


# In[5]:


type(None)


# In[7]:


y = type(None)()


# In[8]:


print(y)


# In[9]:


id(x) 


# In[10]:


id(y)


# In[11]:


id(x) == id(y)


# In[12]:


# same as id(x) == id(y)
x is y


# In[13]:


x = 5
y = 5

x == y


# In[14]:


x is y


# In[15]:


x = 5000
y = 5000

x == y


# In[16]:


x is y


# In[17]:


x = 255
y = 255

x is y


# In[19]:


x = 257
y = 257

x is y


# In[20]:


x = 'abcd'
y = 'abcd'

x == y


# In[21]:


x is y


# In[22]:


x = 'abcd' * 10000
y = 'abcd' * 10000

x == y


# In[23]:


x is y


# In[24]:


x = 'a.b'
y = 'a.b'

x == y


# In[25]:


x is y


# In[26]:


from sys import intern
x = intern('a.b')
y = intern('a.b')


# In[27]:


x == y


# In[28]:


x is y


# In[29]:


help(intern)


# In[30]:


x = None

if x:
    print('It is True-ish')
else:
    print('It is False-ish')


# In[31]:


x == False


# Every object in a boolean context is `True`, except for:
# 
# - `False`
# - `None`
# - 0
# - everything empty -- `''`, `[]`, `()`, `{}`

# In[33]:


while True:
    s = input('Enter your name: ').strip()
    
    if not s:
        break
        
    print(f'Hello, {s}!')


# In[34]:


while s = input('Enter your name: ').strip():
    
    print(f'Hello, {s}!')


# In[35]:


# assignment expression -- walrus

while s := input('Enter your name: ').strip():
    
    print(f'Hello, {s}!')


# # Numbers
# 
# - `int`
# - `float`
# - `complex`

# In[36]:


from sys import getsizeof

x = 0


# In[37]:


getsizeof(x)


# In[38]:


x = 1
getsizeof(x)


# In[39]:


x = 1_000
getsizeof(x)


# In[40]:


x = x ** 10000


# In[41]:


getsizeof(x)


# In[43]:


x = x ** 100
getsizeof(x)


# In[44]:


x = 100
y = x

x = 200
y


# In[45]:


s = '123'
int(s)  


# In[46]:


x = 100


# In[47]:


int(s)


# In[48]:


int(s, 16)   # interpret as a hex int


# In[49]:


int('ff', 16)


# In[50]:


0x16


# In[51]:


0b1010


# In[54]:


0O123


# In[55]:


x = 123.456
type(x)


# In[56]:


x = 1.
type(x)


# In[59]:


0.1 + 0.2 


# In[60]:


round(0.1 + 0.2, 2)


# In[61]:


# BCD -- binary coded decimals

from decimal import Decimal
x = Decimal('0.1')
y = Decimal('0.2')

x + y


# In[62]:


x = Decimal(0.1)
y = Decimal(0.2)

x + y


# In[63]:


x


# In[64]:


y


# In[65]:


x = 10+5j
y = 5-3j

x + y


# In[66]:


x * y


# In[67]:


x = 100
y = [10, 20, 30]

print('x = ' + str(x) + ', and y = ' + str(y) + '.')


# In[68]:


'a' + x


# In[71]:


print(f'x = {x}, y = {y}')


# In[72]:


s = 'He\'s very nice.'


# In[73]:


s


# In[75]:


s = "He's very nice."
s


# In[76]:


s = 'She said, "He\'s very nice."'
s


# In[77]:


print(s)


# In[78]:


path = 'c:\abcd\efgh\ijkl'
print(path)


# In[79]:


path = 'c:\\abcd\\efgh\\ijkl'
print(path)


# In[80]:


# raw string  -- auto-double backslashes

path = r'c:\abcd\efgh\ijkl'
print(path)


# In[81]:


path


# In[83]:


print(repr(path))


# In[84]:


print(path)


# In[87]:


print(f'>> {path.upper()} <<')


# In[89]:


d = {'a':100, 'bcde':2, 'fgh':12345678, 'i':99999}

for key, value in d.items():
    print(f'{key:10}{value:10}')


# In[90]:


d = {'a':100, 'bcde':2, 'fgh':12345678, 'i':99999}

for key, value in d.items():
    print(f'{key:*>10}{value:_^10}')


# In[94]:


d = {'a':100, 'bcde':2, 'fgh':12345678, 'i':99999}

for key, value in d.items():

    # *<5 == field of 5 characters, aligned left, fill with *
    # .>8 == field of 8 characters, aligned right, fill with .

    print(f'{key:.<5}{value:.>8}')


# In[96]:


s = '''this is a long string

It takes multiple lines.

It will not work.'''


# In[97]:


s


# In[99]:


x = 100

'''I want to do something here

and document it'''

y = 200


# In[100]:


x = 'abcdefghijkl'

x


# In[101]:


s = 'abcde'
len(s)


# In[102]:


s = 'שלום'
len(s)


# In[103]:


s = '北京'
len(s)


# In[104]:


# bytestring
s = b'abcde'
type(s)


# In[105]:


len(s)


# In[106]:


s = b'שלום'


# In[108]:


s = 'שלום'
b = s.encode()   # return bytes based on string
b


# In[109]:


len(b)


# In[110]:


s = '北京'
b = s.encode()
len(b)


# In[111]:


b


# In[112]:


b.decode()  # get a string from bytes


# In[114]:


b = b'abcdefghij'

b'j' in b


# In[115]:


'j' in b.decode()


# In[116]:


b.decode('utf-8')


# In[117]:


b.decode('latin-1')


# In[120]:


b.decode('cp1251')


# In[122]:


s = 'abcdefghijklmnopqrstuvwxyz'
len(s)


# In[123]:


s[0]  


# In[124]:


s[10:20]   # slice -- start:end+1


# In[125]:


s[:20]    # slice 


# In[126]:


s[20:]


# In[127]:


s[5:20:3]


# In[128]:


s[::-1]


# In[129]:


# strings are immutable


# In[130]:


s[0] = '!'


# In[132]:


s = 'abcd'
print(id(s))
s += 'efgh'
print(id(s))


# In[133]:


# sequence -- string, list, tuple


# How to install Jupyter
# 
# https://www.youtube.com/watch?v=i2zM8OwxZok&t=10s

# In[135]:


s = ''
getsizeof(s)


# In[136]:


s = 'a'
getsizeof(s)


# In[137]:


len(s)


# # Sequences -- they all do the following:
# 
# - `[i]` to retrieve something at index `i`
# - `[start:end:step]` to get a slice
# - `in` to search
# - loop with `for` over the elements
# - `index` and `count` methods
       mutable/immutable         contents
str        immutable               string
list        mutable                anything   -- items of the same type
tuple      immutable               anything   -- items of different types -- record/struct
# In[138]:


mylist = [10, 20, 30]
len(mylist)


# In[139]:


biglist = [mylist, mylist, mylist]
len(biglist)


# In[140]:


biglist


# In[141]:


mylist[0] = '!'


# In[142]:


mylist


# In[143]:


biglist


# In[146]:


mylist = [10, 20, 30] * 3


# In[147]:


mylist


# In[152]:


mylist = [10, 20, 30]

biglist = [mylist * 3]


# In[153]:


biglist


# In[154]:


mylist = []
getsizeof(mylist)


# In[155]:


mylist.append(10)
getsizeof(mylist)


# In[156]:


mylist.append(20)
getsizeof(mylist)


# In[157]:


mylist = []
for i in range(30):
    print(f'{len(mylist)=}, {i=}, {getsizeof(mylist)}')
    mylist.append(i)


# In[158]:


mylist = [10, 20, 30]
mylist.append('abcd')

mylist


# In[159]:


mylist += 'abcd'     # .extend
mylist


# In[160]:


mylist += 5


# In[162]:


mylist.extend([500, 600, 700])
mylist


# In[163]:


mylist.append([500, 600, 700])
mylist


# In[164]:


mylist = [10, 20, 30]
mylist + [40, 50, 60]


# In[165]:


mylist


# In[166]:


mylist = [10, 20, 30]
mylist.append(mylist)

len(mylist)


# In[167]:


mylist


# In[168]:


mylist[-1]


# In[169]:


mylist is mylist[-1]


# In[170]:


mylist[-1][-1][-1][0]


# In[171]:


t = (10, 20, 30)
type(t)


# In[172]:


t = (10, 20)
type(t)


# In[177]:


t = (10,)
type(t)


# In[178]:


len(t)


# In[174]:


t = ()
type(t)


# In[175]:


2 + 3 * 4


# In[176]:


(2 + 3) * 4


# In[179]:


(2 + 3,) * 4


# In[180]:


t = ([10, 20, 30],
     [100, 200, 300])

len(t)


# In[181]:


t[0].append(40)
t


# In[182]:


t[0] += [50, 60, 70]


# In[183]:


t


# In[184]:


mylist = [10, 20, 30]
mylist = mylist.append(40)

print(mylist)


# In[185]:


mylist = [10, 20, 30]
mylist.append(40)   


# # Exercise: `firstlast`
# 
# Write a function, `firstlast`, that takes a sequence (string, list, tuple) and returns a new object of the same type, with only the first and last elements.
# 
# Examples:
# 
#     firstlast('abcd')                  # 'ad'
#     firstlast([10, 20, 30, 40, 50])    # [10, 50]
#     firstlast((10, 20))                # (10, 20)
#     firstlast('a')                     # 'aa'
#     

# In[191]:


def firstlast(seq):
    return seq[:1] + seq[-1:]

print(firstlast('abcd'))
print(firstlast([10, 20, 30]))
print(firstlast((100, 200, 300, 400)))


# In[193]:


# tuple unpacking


# In[194]:


mylist = [10, 20, 30]

x = mylist

x


# In[195]:


x,y,z = mylist   # unpacking


# In[196]:


x


# In[197]:


y


# In[198]:


z


# In[200]:


mylist = [10, 20, 30, 40, 50, 60, 70]

x,y,*z = mylist


# In[201]:


x


# In[202]:


y


# In[203]:


z


# In[204]:


x,*y,z = mylist


# In[205]:


x


# In[206]:


y


# In[207]:


z


# In[208]:


x,*_,z = mylist


# In[209]:


_


# In[210]:


x = 100
y = 200

x,y = y,x


# In[211]:


x


# In[212]:


y


# In[213]:


mylist = [10]

x,*y = mylist


# In[214]:


x


# In[215]:


y


# In[216]:


x,*y,z = mylist


# In[217]:


p = ('Reuven', 'Lerner', 46)
p[0]


# In[218]:


p[1]


# In[219]:


p[2]


# In[220]:


from collections import namedtuple

Person = namedtuple('Person', ['first', 'last', 'shoesize'])
p = Person('Reuven', 'Lerner', 46)
p


# In[222]:


p[0]


# In[223]:


p[1]


# In[224]:


p[2]


# In[225]:


p.first


# In[226]:


p.last


# In[227]:


p.shoesize


# In[228]:


p.first = 'asdfsadf'


# In[230]:


getsizeof(Person)


# In[231]:


Person.__bases__


# In[232]:


p._replace(first='asdfad')


# In[233]:


p


# # Exercise: Bookstore
# 
# 1. Create a `Book` class using `namedtuple`: `title`, `author`, `price`
# 2. Create 3-4 instances of `Book`, and put them in a list, `inventory`.
# 3. The user can ask for a book (by title). 
#     - If we carry this book, we print its details and add the price to the total.
#     - If we *don't* carry it, then we tell the user.
#     - If the user enters an empty string, then we stop asking and print the total.

# https://github.com/reuven/dfend-2021-12Dec-adv1
# 
# https://github.com/reuven/
# 

# In[235]:


from collections import namedtuple

Book = namedttwuple('Book', ['title', 'author', 'price'])

b1 = Book('title1', 'author1', 50)
b2 = Book('title2', 'author2', 50)
b3 = Book('title3', 'author3', 50)
b4 = Book('title4', 'author3', 100)

inventory = [b1, b2, b3, b4]
total = 0

while True:
    look_for = input('Enter title: ').strip()
    
    if not look_for:
        break
        
    for one_book in inventory:
        if look_for == one_book.title:
            print(f'Found {one_book}')
            total += one_book.price
            break
            
    else:   # only run this if we did *NOT* get to a break
        print(f'Did not find {look_for}')
            
print(f'{total=}')    


# # Dicts
# 
# - dict
# - set
# - `Counter`, `defaultdict`, `OrderedDict`
# - Functions

# In[236]:


d = {'a':1, 'b':2, 'c':3}


# In[237]:


d['a']


# In[238]:


d['a'] = 10


# In[239]:


'a' in d


# In[240]:


'q' in d


# In[241]:


# Until 3.6

d = {}
d['a'] = 10


# In[242]:


hash('a')


# In[243]:


hash('a') % 8


# In[244]:


d['b'] = 20
hash('b') % 8


# In[245]:


d['c'] = 30
hash('c') % 8


# In[246]:


d = {}


# In[248]:


d['a'] = 10


# In[249]:


hash('a') % 8


# In[250]:


d['b'] = 20
hash('b') % 8


# In[251]:


d['c'] = 30
hash('c') % 8


# In[252]:


for key, value in d.items():
    print(f'{key}: {value}')


# In[253]:


d = {'b':20, 'a':10, 'd':40, 'c':30}

for key, value in d.items():
    print(f'{key}: {value}')


# In[254]:


d.pop('c')

d['c'] = 99

d


# In[255]:


d


# In[256]:


d['a']


# In[257]:


d['x']


# In[258]:


d.get('a')   # either get d['a'] (if it exists) or None


# In[259]:


d.get('x')


# In[260]:


d.get('x', 'No such key x')


# In[262]:


if 'x' in d:
    print(d['x'])
else:
    print('No such key x')


# In[263]:


d.keys()


# In[264]:


d.values()


# In[265]:


d.items()


# In[267]:


for t in d.items():
    print(t)


# In[268]:


for key, value in d.items():
    print(f'{key}: {value}')


# In[269]:


d


# In[270]:


d.setdefault('x', 100)


# In[271]:


d


# In[272]:


d.setdefault('x', 50)


# In[273]:


d


# In[274]:


new_value = d.setdefault('x', 50)

if new_value == 50:
    print('I set it!')
else:
    print('No, it still has the old value')


# # Exercise: Rainfall
# 
# 1. Define `rainfall`, an empty dict.  Cities (strings) will be the keys, and ints will be the values.
# 2. Ask the user, repeatedly, to enter a city name.
# 3. If they give us an empty string, print all cities + rain amounts from the dict. And then exit.
# 4. If they give us a non-empty city name, ask how much rain fell there.
# 5. Add the amount of rain for that city.
# 
# Example:
# 
#     City: Tel Aviv
#     Rain: 5
#     City: Jerusalem
#     Rain: 3
#     City: Tel Aviv
#     Rain: 2
#     City: [ENTER]
#     Tel Aviv: 7
#     Jerusalem 3
#     
#     

# In[279]:


rainfall = {}

while True:
    city_name = input('City: ').strip()
    
    if not city_name:   # empty string? exit
        break
        
    mm_rain = input('Rain: ').strip()

    if mm_rain.isdigit():
        rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)
    else:
        print(f'{mm_rain} is not numeric')
    
for key, value in rainfall.items():
    print(f'{key}: {value}')


# In[280]:


d = {'a':1, 'b':2, 'c':3}

other = {'b':20, 'c':30, 'd':40}

d.update(other)   

d


# In[281]:


d = {'a':1, 'b':2, 'c':3}

other = {'b':20, 'c':30, 'd':40}

# starting with 3.9, we can use |

d | other   # gives me a new dict back


# In[284]:


d ^ other


# In[285]:


# sets

s = {10, 20, 30, 40, 20, 30, 40, 20, 30, 40, 50}
s


# In[286]:


type(s)


# In[287]:


mylist = [10, 20, 30]
d[mylist] = 100


# In[288]:


s


# In[289]:


s.add(40)
s


# In[290]:


s.remove(40)
s


# In[291]:


s = {}
type(s)


# In[292]:


s = set()  # now it's an empty set
type(s)


# In[293]:


s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
s3 = {10, 20}


# In[294]:


s1 & s2


# In[295]:


s1 | s2


# In[297]:


s1 ^ s2   # symmetric difference


# In[298]:


s1 - s2


# In[299]:


s2 - s1 


# In[300]:


s3 < s1   # subset?


# In[301]:


s1 < s1


# In[302]:


s1 <= s1


# In[303]:


set([10, 20, 30, 20, 30, 40, 20, 30, 40])


# In[304]:


s 


# In[306]:


s = {10, 20, 30, 40}

s.add(20)


# In[307]:


# defaultdict

d = {'a':1, 'b':2}
d['c']


# In[308]:


from collections import defaultdict

d = defaultdict(0)

d['a']


# In[309]:


d = defaultdict(int)


# In[310]:


int()


# In[311]:


d['a'] += 5
d['b'] += 10
d['c']


# In[312]:


d


# In[314]:


d = defaultdict(dict)

d['a']['b'] = 100
d['b']['c'] = 200
d['b']['d'] = 300

d


# In[315]:


import time

d = defaultdict(time.time)

d['a']


# In[316]:


d['b']


# In[317]:


d['c']


# In[318]:


d


# In[319]:


d['x']


# In[320]:


d


# In[321]:


from collections import Counter


# In[322]:


c = Counter()
c['a'] += 5
c['b'] += 10
c


# In[323]:


Counter([10, 20, 30, 20, 30, 40, 20, 30, 40, 50])


# In[325]:


Counter('abcbcbbbcbcdefde    ')


# In[326]:


def return_5():
    return 5

d = defaultdict(return_5)


# In[327]:


def return_5_times_x():
    return 5 * x


d = defaultdict(return_5_times_x)


# In[328]:


d['a']


# In[329]:


d = defaultdict(int)


# In[330]:


d['a']    # 'a' is not there, so it runs int(), which gives us 0, then it sets d['a'] = 0


# In[331]:


d


# In[332]:


from collections import OrderedDict


# In[333]:


help(OrderedDict)


# In[334]:


get_ipython().run_line_magic('pinfo2', 'OrderedDict')


# # Functions

# In[335]:


s = 'abcd'
x = len(s)

type(x)


# In[336]:


x


# In[337]:


x = s.upper()

type(x) 


# In[338]:


x


# In[339]:


x = s.upper


# In[340]:


type(x)


# In[341]:


x


# In[342]:


x()


# In[343]:


d = {'a':1, 'b':2, 'c':3}

for key, value in d.items():
    print(f'{key}: {value}')


# In[344]:


d = {'a':1, 'b':2, 'c':3}

for key, value in d.items:
    print(f'{key}: {value}')


# In[345]:


def hello():
    print('Hello!')


# In[346]:


# (1) define a function object
# (2) assigned the function object to "hello"


# In[347]:


type(hello)


# In[348]:


hello()


# In[349]:


hello = 5


# In[350]:


hello()


# In[351]:


def hello():
    print('Hello!')


# In[352]:


x = hello()


# In[353]:


type(x)


# In[354]:


print(x)


# In[355]:


def hello():
    return 'Hello!'


# In[356]:


hello('world')


# In[357]:


# 2 types of arguments

# - positional arguments
# - keyword arguments


# In[358]:


hello.__code__.co_argcount


# In[360]:


def hello(name):
    return f'Hello, {name}!'


# In[361]:


hello('world')


# In[362]:


hello(5)


# In[363]:


hello([10, 20, 30])


# In[364]:


hello(hello)


# In[365]:


hello()


# In[366]:


hello.__code__.co_argcount


# In[367]:


hello.__code__.co_varnames


# In[368]:


def hello(name):
    s =  f'Hello, {name}!'
    return s


# In[369]:


hello.__code__.co_argcount


# In[370]:


hello.__code__.co_varnames


# In[371]:


# params:    name
# args:      'world'

hello('world')


# In[372]:


# params:    name
# args:      'world'  'junk'

hello('world', 'junk')


# In[373]:


def hello(name):
    if type(name) == str:
        s =  f'Hello, {name}!'
        return s
    else:
        raise ValueError('I wanted a string!')


# In[ ]:


# duck typing 

def hello(name):
    if type(name) == str:
        s =  f'Hello, {name}!'
        return s
    else:
        raise ValueError('I wanted a string!')


# In[374]:


# type annotations
def hello(name:str) -> str:
    s =  f'Hello, {name}!'
    return s


# In[375]:


hello.__annotations__


# In[376]:


hello('world')


# In[377]:


hello(5)


# In[378]:


hello([10, 20, 30])


# In[379]:


# duck typing 

def hello(name):
    s =  f'Hello, {name}!'
    return s


# In[380]:


# params  name
# args   'world'

hello(name='world')   # keyword argument 


# In[381]:


hello(stuff='world')


# In[382]:


def add(first, second):
    return first + second


# In[383]:


# params: first second
# args:    10    3

add(10, 3)


# In[384]:


add(first=10, second=3)


# In[385]:


add(second=3, first=10)


# In[386]:


# positional before keyword!
add(10, second=3)


# In[387]:




add(second=3, 10)


# In[388]:


add(3, first=10)


# In[389]:


# default argument 
def add(first, second=10):
    return first + second
    


# In[391]:


# params: first second
# args:    2     3

add(2, 3)


# In[392]:


# params: first second
# args:    2

add(2)


# In[393]:


add.__defaults__


# In[394]:


def add_one(x):
    x.append(1)
    return x

mylist = [10, 20, 30]
add_one(mylist)
mylist


# In[395]:


def add_one(x=[]):   # don't use mutable defaults
    x.append(1)
    return x

add_one()


# In[396]:


add_one()


# In[397]:


add_one()


# In[398]:


add_one.__defaults__


# In[399]:


def add_one(x=None):
    if x is None:
        x = []
    
    x.append(1)
    return x

add_one()


# In[400]:


add_one()


# In[401]:


sum([10, 20, 30])


# In[402]:


def mysum(numbers):
    total = 0
    
    for one_number in numbers:
        total += one_number
        
    return total


# In[403]:


mysum([10, 20, 30])


# In[404]:


mysum(10, 20, 30)


# In[405]:


def mysum(a=0, b=0, c=0, d=0):
    return a + b + c + d


# In[406]:


mysum(10, 20, 30)


# In[407]:


mysum(10, 20, 30, 40)


# In[408]:


mysum(10, 20, 30, 40, 50)


# In[409]:


def mysum(*numbers):    # splat-args  
    total = 0
    
    for one_number in numbers:
        total += one_number
        
    return total


# In[410]:


mysum(10, 20, 30)


# In[411]:


mysum.__code__.co_argcount


# In[412]:


mysum.__code__.co_varnames


# In[414]:


bin(mysum.__code__.co_flags)


# In[415]:


import dis
dis.show_code(mysum)


# In[416]:


def myfunc(a, b, *args):
    x = 1234
    return f'{a=}, {b=}, {args=}, {x=}'


# In[418]:


myfunc(10, 20, 30, 40, 50, 60, 70)


# In[419]:


myfunc.__code__.co_argcount


# In[420]:


dis.show_code(myfunc)


# In[421]:


def myfunc(a, b=99, *args):
    x = 1234
    return f'{a=}, {b=}, {args=}, {x=}'


# In[422]:


myfunc(10, 20, 30, 40, 50)


# In[423]:


myfunc(10)


# In[424]:





# In[ ]:




def myfunc(a, b=99, *args):
    x = 1234
    return f'{a=}, {b=}, {args=}, {x=}'


# # Parameter types
# 
# 1. Regular (mandatory) parameters, can be positional or keyword
# 2. Optional parameters, can be positional or keyword
# 3. `*args`, taking all unclaimed positional

# # Exercise: `all_lines`
# 
# Write a function, `all_lines`, that takes a first argument, a string, a filename into which we'll write data.
# 
# The rest of the (positional) arguments will also be strings, filenames, from which we'll take input.
# 
# The function, when called, should write all lines (in order) from all input files, into the output file.
# 
# ```python
# all_lines('output.txt', 'input1.txt', 'input2.txt')  # output.txt == input1.txt + input2.txt
# ```

# In[434]:


def all_lines(outfilename, *args):
    print(f'{outfilename=}, {args=}')
    with open(outfilename, 'w') as outfile:
        for one_filename in args:
            for one_line in open(one_filename):
                outfile.write(one_line)


# In[426]:


for i in range(5):
    with open(f'infile{i}.txt', 'w') as f:
        for j in range(5):
            f.write(f'{j}abcdefg\n')


# In[427]:


get_ipython().system('ls ')


# In[428]:


all_lines('outfile.txt', 'infile0.txt', 'infile1.txt', 'infile2.txt')


# In[429]:


get_ipython().system('cat outfile.txt')


# In[431]:


import glob
glob.glob('in*.txt')


# In[436]:


all_lines('outfile.txt', glob.glob('in*.txt'))


# In[ ]:




