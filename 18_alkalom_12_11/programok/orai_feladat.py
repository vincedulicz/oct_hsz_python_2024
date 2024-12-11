from collections.abc import Iterable


def get_length(item):
    if isinstance(item, Iterable):
        return len(item)
    else:
        return "Not iterable"


# print(get_length("Hello"))
# print(get_length([1,2,3]))
# print(get_length(123))


def my_decorator(func):
    def wrapper():
        print("ez van a függvényhívás előtt")
        func()
        print("ez van a függvényhívás után")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

# say_hello()




my_list = [("apple", 50), ("banana", 10), ("cherry", 30)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)


my_list = [1,2,3,4,5,6]
odd_numbers = list(filter(lambda x: x % 2 != 0, my_list))
print(odd_numbers)


new_list = list(map(lambda x: x**2, my_list))
print(new_list)

new_list = [(lambda x: x**2)(x) for x in my_list]
print(new_list)


square = lambda x: x**2
print(square(5))


words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
print(sorted_words)



import re

text = "Python is awesome"
result = re.search(r"Python", text)
print(result.group())



text = "Python is awesome. Python is powerful. Python"
matches = re.findall(r"Python", text)
print(matches)


result = re.match(r"Python", text)
print(result is not None)


result = re.fullmatch(r"Python", text)
print(result is not None)


result = re.sub(r"Python", "Java", text)
print(result)


pattern = re.compile(r"Python")
text = "Python is awesome. Python is powerful. Python"
matches = pattern.findall(text)
print(matches)



email_minta = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email_szoveg = "Az email cím: pelda.elek@mail-server-example.com és info@test.org"

talalatok = re.findall(email_minta, email_szoveg)
print(talalatok)

