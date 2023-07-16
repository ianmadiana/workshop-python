#!/usr/bin/env python
# coding: utf-8

# In[47]:


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple')


# In[48]:


fruits.count('tangerine')


# In[49]:


fruits.index('banana')


# In[50]:


fruits.index('banana', 4)


# In[51]:


fruits.reverse()
fruits


# In[52]:


fruits.append('grape')
fruits


# In[53]:


fruits.sort()
fruits


# In[54]:


fruits.pop()


# In[55]:


#List


# In[56]:


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack


# In[57]:


stack.pop()


# In[58]:


stack


# In[59]:


stack.pop()


# In[60]:


stack.pop()


# In[61]:


stack


# In[62]:


#Using Lists as Queues


# In[63]:


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()         


# In[64]:


queue.popleft()


# In[65]:


queue                           


# In[66]:


# List Comprehensions


# In[67]:


squares = []
for x in range(10):
    squares.append(x**2)
    
squares


# In[68]:


squares = list(map(lambda x: x**2, range(10)))


# In[69]:


squares = [x**2 for x in range(10)]


# In[70]:


[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# In[71]:


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs


# In[72]:


vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]


# In[73]:


# filter the list to exclude negative numbers
[x for x in vec if x >= 0]


# In[74]:


# apply a function to all the elements
[abs(x) for x in vec]


# In[75]:


# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]


# In[76]:


# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]


# In[77]:


# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]


# In[78]:


from math import pi
[str(round(pi, i)) for i in range(1, 6)]


# In[79]:


# Nested List Comprehensions


# In[80]:


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


# In[81]:


[[row[i] for row in matrix] for i in range(4)]


# In[82]:


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed


# In[83]:


transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed


# In[84]:


list(zip(*matrix))


# In[85]:


# The del statement


# In[86]:


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a


# In[87]:


del a[2:4]
a


# In[88]:


del a[:]
a


# In[89]:


del a


# In[90]:


# Tuples and Sequences


# In[91]:


t = 12345, 54321, 'hello!'
t[0]


# In[92]:


t


# In[93]:


# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u


# In[94]:


# Tuples are immutable:
t[0] = 88888


# In[95]:


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v


# In[96]:


empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)


# In[97]:


empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)


# In[98]:


singleton


# In[99]:


# Sets


# In[100]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) 


# In[101]:


'orange' in basket 


# In[103]:


'crabgrass' in basket


# In[104]:


# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a     


# In[105]:


a - b 


# In[106]:


a | b


# In[107]:


a & b


# In[108]:


a ^ b 


# In[109]:


a = {x for x in 'abracadabra' if x not in 'abc'}
a


# In[110]:


# Dictionaries


# In[111]:


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel


# In[112]:


tel['jack']


# In[113]:


del tel['sape']
tel['irv'] = 4127
tel


# In[114]:


list(tel)


# In[115]:


sorted(tel)


# In[117]:


'guido' in tel


# In[118]:


'jack' not in tel


# In[119]:


dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


# In[120]:


{x: x**2 for x in (2, 4, 6)}


# In[121]:


dict(sape=4139, guido=4127, jack=4098)


# In[122]:


# Looping Techniques


# In[123]:


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)


# In[124]:


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# In[125]:


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# In[126]:


for i in reversed(range(1, 10, 2)):
    print(i)


# In[127]:


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)


# In[128]:


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)


# In[129]:


# More on Conditions


# In[130]:


string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null

