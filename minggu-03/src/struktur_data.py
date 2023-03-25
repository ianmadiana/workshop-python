# # List of fruits
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# count(): kembalikan jumlah kemunculan x dalam list
print(fruits.count('apple')) # output: 2
print(fruits.count('tangerine')) # output: 0

# index(): Mengembalikan indeks yang berbasis nol pada daftar dari item pertama yang nilainya sama dengan x
print(fruits.index('banana')) # output: 3
print(fruits.index('banana', 4)) # output: 6

# reverse(): Membalik elemen-elemen pada daftar (list) di tempat (tanpa menggunakan variabel baru).
fruits.reverse()
print(fruits) # output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

# append(): Tambahkan item ke ujung dari sebuah list
fruits.append('grape')
print(fruits) # output: ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

# sort(): Mengurutkan elemen-elemen dari sebuah list secara langsung
fruits.sort()
print(fruits) #output: ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']

# Menghapus item pada posisi yang diberikan dalam daftar, dan mengembalikannya. Jika tidak ada indeks yang ditentukan, a.pop() akan menghapus dan mengembalikan item terakhir dalam daftar.
print(fruits.pop()) #output: pear

# Menggunakan List sebagai Stack (tumpukan)
# Stack digunakan untuk menyimpan sekumpulan data dengan konsep Last-In-First-Out (LIFO). Artinya, data yang terakhir dimasukkan ke dalam stack akan menjadi data yang pertama kali dikeluarkan dari stack.
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack) # output: [3, 4, 5, 6, 7]
# hapus item terakhir (7)
print(stack.pop())
print(stack) # output: [3, 4, 5, 6]

# Menggunakan List sebagai Queues (antrian)
# elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("first-in, first-out")
# impor library
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
queue.popleft()                 # The second to arrive now leaves
print(queue)                    # output: deque(['Michael', 'Terry', 'Graham'])

# List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)
print(squares) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = list(map(lambda x: x**2, range(10)))
print(squares) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# sama saja dengan
squares = [x**2 for x in range(10)] # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
# output: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)
# output: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# membuat daftar baru dengan nilai-nilai yang digandakan
vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec]) # output: [-8, -4, 0, 4, 8]
# filter list untuk mengecualikan angka negatif
print([x for x in vec if x >= 0]) #output: [0, 2, 4]
# menerapkan fungsi absolut (abs()) ke semua elemen
print([abs(x) for x in vec]) #output: [4, 2, 0, 2, 4]
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

print([(x, x**2) for x in range(6)])

print([x, x**2 for x in range(6)])

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])


# Nested List Comprehensions
# contoh berikut dari matriks 3x4 yang diimplementasikan sebagai daftar 3 daftar dengan panjang 4
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

print(list(zip(*matrix)))

# Pernyataan del
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
[1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)
[1, 66.25, 1234.5]
del a[:]
print(a)

# Tuples and Sequences
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
v = ([1, 2, 3], [3, 2, 1])
print(v)

empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)

# Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                              # show that duplicates have been removed
print('orange' in basket)                 # fast membership testing
print('crabgrass' in basket)

# Menunjukkan operasi himpunan pada huruf-huruf unik dari dua kata
a = set('abracadabra')
b = set('alacazam')
print(a) # huruf unik di a

print(a - b) # huruf di a tapi tidak b
print(a | b) # huruf a atau b atau keduanya
print(a & b) # huruf a dan b
print(a ^ b ) # huruf dalam a atau b tetapi tidak keduanya

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)

# Konstruktor dict() membangun kamus secara langsung dari urutan pasangan kunci-nilai:
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# Ketika kunci-kuncinya adalah string yang sederhana, terkadang lebih mudah untuk menentukan pasangan-pasangan tersebut menggunakan argumen kata kunci:
print(dict(sape=4139, guido=4127, jack=4098))

# Looping Techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
    
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
    
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    
for i in reversed(range(1, 10, 2)):
    print(i)
    
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
    
for f in sorted(set(basket)):
    print(f)
    
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

# More on Conditions
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)