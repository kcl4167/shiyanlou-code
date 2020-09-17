#!/usr/bin/env python3
fobj = open('/tmp/String.txt')
cont = fobj.read()
digits = ''
for char in cont:
    if char.isdigit():
        digits += char
print(digits)


