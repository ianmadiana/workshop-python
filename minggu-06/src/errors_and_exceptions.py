# Syntax Errors
while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')


#Exceptions
10 * (1/0)
output => ZeroDivisionError: division by zero
4 + spam*3
output => NameError: name 'spam' is not defined
'2' + 2
output => TypeError: can only concatenate str (not "int") to str

#Handling Exceptions
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


    except (RuntimeError, TypeError, NameError):
        pass
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    
    print(inst.args)   
    print(inst)
                         
    x, y = inst.args     
    print('x =', x)
    print('y =', y)


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

#Raising Exceptions#
raise NameError('HiThere')

raise ValueError
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

#Exception Chaining
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")
def func():
    raise ConnectionError
try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

#Defining Clean-up Actions#
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

def bool_return():
    try:
        return True
    finally:
        return False
result = bool_return()
print(result)


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
divide(2, 0)
divide("2", "1")


#Predefined Clean-up Actions
for line in open("myfile.txt"):
    print(line, end="")

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

#Raising and Handling Multiple Unrelated Exceptions
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)
f()
try:
    f()
except Exception as e:
    print(f'caught {type(e)}: e')
def f():
    raise ExceptionGroup("group1",
                         [OSError(1),
                          SystemError(2),
                          ExceptionGroup("group2",
                                         [OSError(3), RecursionError(4)])])

try:
    f()
except OSError as e:
    print("There were OSErrors")
except SystemError as e:
    print("There were SystemErrors")
excs = []
for test in tests:
    try:
        test.run()
    except Exception as e:
        excs.append(e)
if excs:
   raise ExceptionGroup("Test Failures", excs)

#Enriching Exceptions with Notes
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise

def f():
    raise OSError('operation failed')
excs = []
for i in range(3):
    try:
        f()
    except Exception as e:
        e.add_note(f'Happened in Iteration {i+1}')
        excs.append(e)
raise ExceptionGroup('We have some problems', excs)