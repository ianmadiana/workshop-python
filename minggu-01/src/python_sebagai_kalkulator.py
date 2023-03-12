from distributed import _

# numbers
2 + 2
50 - 5*6
(50 - 5*6) / 4
8 / 5  # division always returns a floating point number

17 / 3  # classic division returns a float
17 // 3  # floor division discards the fractional part
17 % 3  # the % operator returns the remainder of the division
5 * 3 + 2  # floored quotient * divisor + remainder

5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7

width = 20
height = 5 * 9
width * height

4 * 3.75 - 1

tax = 12.5 / 100
price = 100.50
price * tax
price + _
round(_, 2)

# Strings
'spam eggs'  # single quotes
'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output
print(s)  # with print(), \n produces a new line

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

3 * 'un' + 'ium'

'Py' 'thon'

text = ('Put several strings within parentheses '
        'to have them joined together.')

prefix = 'Py'
prefix + 'thon'

word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5

word[-1]  # last character
word[-2]  # second-last character
word[-6]

word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)

word[:2] + word[2:]
word[:4] + word[4:]

#Lists
squares = [1, 4, 9, 16, 25]
squares
squares[0]  # indexing returns the item
squares[-1]
squares[-3:]
squares[:]

cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
cubes

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
# now remove them
letters[2:5] = []
letters
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters

letters = ['a', 'b', 'c', 'd']
len(letters)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
    
i = 256*256
print('The value of i is', i)

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b