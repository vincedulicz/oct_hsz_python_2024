# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

teszt = 0 # int
# print(teszt)

teszt = "szöveg" # string - egy soros komment
# komment eleje
# közepe
# komment vége
# print(teszt)

output = None

"""
a

szöveg


itt is

z
"""


"""
Tiltott szavak listája:

False
None
True
and
as
assert
async
await
break
class
continue
def
del
elif
else
except
finally
for
from
global
if
import
in
is
lambda
nonlocal
not
or
pass
raise
return
try
while
with
yield
"""

"""
Változók:

Csak betű, szám, aláhúzás
Nem kezdőthet számmal
Kis & nagybetű számít
Beszédes nevek

output1 = 0
output2 = 0

not_very_long_var = True

def fugg(param):
    Pass

def negyzet_szamolo(param):
    Pass

"""

import keyword

# print(keyword.kwlist)

a_int = 1
b_float = 1.5
c_complex = 3.14j

# print(5 / 2) # py2 csak int-et ad vissza
# print(5 // 2) # egész
# print(7 % 4) # maradék
# print(2 ** 3) # hatvány

# print(type(c_complex))


text = "szöveg"

# print(text[0])
# print(text[0:2])
# print(text[2:])
# print(text[-3:])

# rint(text[0:-1:2])
# print(text[::2])

# print(text[::1])
# print(text[::-1])
# print(text[-1])
# print(text[-2])



# print(f'Érték: {a_int}, típus: {type(a_int)}')

test_integer = 542

test_str = 'dfdfdf'
# print("")
# print('fgfdgfdgfdgfdg')

# print(f'teszt szöveg: {test_integer}, különbség - 2: {test_integer - 2} típus: {type(test_integer)}')

# name = input("Hogy hívnak?")
# print(f'Szia {name}')



# first_number = int(input("Első szám: "))
# second_number = int(input("Második szám: "))


# print(first_number + second_number)


"""import math

print("Mennyi kör sugara?")
sugar = float(input())

print("Kerület = ", 2 * sugar * math.pi)
print("Terület = ", sugar**2 * math.pi)"""

# print(3, 1416)
# print(3.1416)

i = 1
while i <= 10:
    print(i+1)
    i += 1


"""def paros_e(szam):
    return szam % 2 == 0

if paros_e(5):
    print("varázslat")
else:
    print("mér nem páros")

a = 2
b = 2

if a > b:
    print("a > b")
elif b > a:
    print("b > a")
elif b == a:
    print("b egyenlő a")
else:
    print("más")"""

teszt_lista = ["str2", 2, 2, 2, 2, 2j, 3.14, "str2"]
print(teszt_lista)

teszt_lista.append(5)

print(teszt_lista.count("str2"))

print(teszt_lista)










def print_hi(name):
    pass
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    # print_hi('Hello World')
