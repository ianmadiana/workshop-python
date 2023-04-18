# Reading and Writing Files
f = open('workfile', 'w', encoding="utf-8")
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
    print(read_data)
    print(f.closed) # output : False
    print(f.close()) # output :None
    f.read()
   
# Methods of File Objects
    f.read()
    f.read()
    f.readline()
    f.readline()
    f.readline()
    for line in f:
        print(line, end='')
    f.write('This is a test\n')
    value = ('the answer', 42)
    s = str(value)
    f.write(s)

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
print(f.seek(5))
print(f.read(1))
print(f.seek(-3, 2))
print(f.read(1))

# Saving structured data with json
import json
x = [1, 'simple', 'list']
print(json.dumps(x))