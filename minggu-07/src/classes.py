#Scopes and Namespaces Example
def scope_test():
    def do_local():
        spam = "local spam"  
    def do_nonlocal():
        nonlocal spam 
        spam = "nonlocal spam"  
    def do_global():
        global spam  
        spam = "global spam"  
    spam = "test spam"  
    do_local()  
    print("After local assignment:", spam)  
    do_nonlocal()  
    print("After nonlocal assignment:", spam)  
    do_global()  
    print("After global assignment:", spam)  
scope_test()  
print("In global scope:", spam) 

#Class Objects
class MyClass:  
    """A simple example class""" 
    i = 12345  
    def f(self):  
        return 'hello world'  
    def __init__(self):  
        self.data = []  
class Complex:  
    def __init__(self, realpart, imagpart):  
        self.r = realpart  
        self.i = imagpart  
x = Complex(3.0, -4.5)  
print(x.r, x.i)  

#Instance Objects
x.counter = 1  
while x.counter < 10:  
    x.counter = x.counter * 2  
print(x.counter)  
del x.counter 

#Method Objects
x.f() 
xf = x.f 
while True:
    print(xf()) 

#Class and Instance Variables
class Dog:
    kind = 'canine'         
    def __init__(self, name):
        self.name = name    
d = Dog('Fido')
e = Dog('Buddy')
print(d.kind) 
print(e.kind) 
print(d.name) 
print(e.name) 

class Dog:
    tricks = []             
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)  

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = [] 
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)  
print(e.tricks)  

#Random Remarks
class Warehouse:
    purpose = 'storage'  
    region = 'west' 
w1 = Warehouse()  
print(w1.purpose, w1.region)  
w2 = Warehouse()  
w2.region = 'east'  
print(w2.purpose, w2.region)  
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)
class C:
    f = f1  
    def g(self):
        return 'hello world'
    h = g  
class Bag:
    def __init__(self):
        self.data = []  
    def add(self, x):
        self.data.append(x)  
    def addtwice(self, x):
        self.add(x)  
        self.add(x)  

#Private Variables
class Mapping:
    def __init__(self, iterable):
        self.items_list = []  
        self.__update(iterable)  
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)  
    __update = update  
class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

#Odds and Ends
from dataclasses import dataclass
@dataclass
class Employee:
    name: str
    dept: str
    salary: int
john = Employee('john', 'computer lab', 1000)
print(john.dept)
print(john.salary)

#Iterators
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("D:\SEMESTER 6\WORKSHOP PYTHON\minggu-07\src\myfile.txt"):
    print(line, end='')
s = 'abc'
it = iter(s)
print(it)  
try:
    print(next(it))  
    print(next(it))  
    print(next(it))  
    print(next(it))  
except StopIteration:
    print("Iterator mencapai akhir string")
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)

#Generators
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

#Generator Expressions
sum(i*i for i in range(10))  
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x, y in zip(xvec, yvec))  
unique_words = set(word for line in page for word in line.split())  
valedictorian = max((student.gpa, student.name) for student in graduates)  
data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))





