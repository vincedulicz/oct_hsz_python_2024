import re

pattern = r'^Hello'
text = "Hello world!"

match = re.match(pattern, text)

if match:
    print(f"found: {match.group()}")


pattern = r'world'
text = "Hello world!"

search = re.search(pattern, text)

if search:
    print(f"search found: {search.group()}")
else:
    print("no match")



pattern = r"cat"
replacement = "dog"
text = "the cat sat on the cat mat"

result = re.sub(pattern, replacement, text)

print(result)


pattern = r"(\d{4})-(\d{2})-(\d{2})"
text = "today's date is 2024-12-09"

match = re.search(pattern, text)
if match:
    year, month, day = match.groups()
    print(f'year: {year}, month: {month}, day: {day}')



text = "i love cats and dogs."
replacements = {"cats": "kittens", "dogs": "puppies"}

result = re.sub(r"\b(cats|dogs)\b", lambda m: replacements[m.group()], text)
print(result)





class Auto:
    def __init__(self, kerekszam, motor):
        self.kerekszam = Kerek(kerekszam)
        self.motor = Motor(motor)

    def test(self):
        self.motor.kiiars()

new_auto = Auto()
del new_auto

class Kerek:
    pass

class Motor:
    def kiiars(self):
        pss