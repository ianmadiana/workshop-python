# Operating System Interface
import os
import shutil
os.getcwd()
os.chdir('/server/accesslogs')
os.system('mkdir today')

dir(os)
help(os)

shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')

# File Wildcards
import glob
glob.glob('*.py')

# Command Line Arguments
import sys
import argparse
print(sys.argv)

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

# Error Output Redirection and Program Termination
sys.stderr.write('Warning, log file not found starting a new one\n')
# output: Warning, log file not found starting a new one

# String Pattern Matching
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'tea for too'.replace('too', 'two')

# Mathematics
import math
print(math.cos(math.pi / 4))
# 0.7071067811865476
print(math.log(1024, 2))
# 10.0
import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))   # sampling without replacement
print(random.random())    # random float
print(random.randrange(6))

# import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
# 1.6071428571428572
print(statistics.median(data))
# 1.25
print(statistics.variance(data))
1.3720238095238095

# Internet Access
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())
# datetime: 2023-06-13T23:59:47.949345+00:00

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()

# Dates and Times
from datetime import date
now = date.today()
print(now)
# 2023-06-14
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# 06-14-23. 14 Jun 2023 is a Wednesday on the 14 day of June.

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)
# 21502

# Data Compression
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
# 41
t = zlib.compress(s)
print(len(t))
# 37
print(zlib.decompress(t))
# b'witch which has which witches wrist watch'
print(zlib.crc32(s))
# 226805979

# Performance Measurement
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# 0.02548810001462698
print(0.02548810001462698)
# 0.54962537085770791

# Quality Control
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
unittest.main()

# Standard Library Part II
# Output Formatting
import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))
# {'a', 'c', 'd', 'e', 'f', 'g', ...}

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
pprint.pprint(t, width=30)
# [[[['black', 'cyan'],
#    'white',
#    ['green', 'red']],
#   [['magenta', 'yellow'],
#    'blue']]]

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))
# The wrap() method is just like fill()
# except that it returns a list of strings
# instead of one big string with newlines
# to separate the wrapped lines.

import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# 'English_United States.1252'
conv = locale.localeconv()
x = 1234567.8
print(locale.format("%d", x, grouping=True))
# '1,234,567'
print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True))
# '$1,234,567.80'

# Templating
t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
print(t.substitute(d))
# Traceback (most recent call last):
# KeyError: 'owner'
print(t.safe_substitute(d))

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
    
# Working with Binary Data Record Layouts
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)
    start += extra_size + comp_size

# Multi-threading
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')
background.join()
print('Main program waited until background was done.')

# Logging
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

# Weak References
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']                # fetch the object if it is still alive
10
del a                       # remove the one reference
gc.collect()                # run garbage collection right a
0
d['primary']

# Tools for Working with Lists
from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
# 26932
print(a[1:3])
# array('H', [10, 700])

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
# Handling task1

unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
        
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)
# [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      
heappush(data, -5)                 
[heappop(data) for i in range(3)]  
# [-5, 0, 1]

# Decimal Floating Point Arithmetic
from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))
# 0.74
print(round(.70 * 1.05, 2))
# 0.73

print(Decimal('1.00') % Decimal('.10'))
# 0.00
print(1.00 % 0.10)
# 0.09999999999999995

print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
# True
print(sum([0.1]*10) == 1.0)
# False

getcontext().prec = 36
print(Decimal(1) / Decimal(7))
# 0.142857142857142857142857142857142857