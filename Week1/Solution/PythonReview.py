#Data types
# Immutable - int, float, str, tuple
# Mutable - list, dict, set

myList = [1,2,3]
secondList = myList
secondList.append(4)
print(myList)
print(secondList)

#Making a copy
copyList = myList[:]
# copyList = list(myList)
# copyList = myList.copy()
copyList.append(5)
print(myList)
print(copyList)

#Nested data
board = [['a','b', 'c'], ['d','e','f'],['g','h','i']]
print(board[1][1])
python_books = [
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "topics": ["automation", "scripting", "beginner"],
        "year": 2019
    },
    {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "topics": ["basics", "projects", "practice"],
        "year": 2023
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "topics": ["advanced", "performance", "idioms"],
        "year": 2022
    }
]
print(python_books[2]["topics"][1])

#Loops
fruit = ["apple", "bannana", "orange"]

#enumerate returns an iterator of tuples with (index, value)
print(list(enumerate(fruit)))
for item in enumerate(fruit):
  print(item)
  print(item[0])
  print(item[1])


#First Class Functions 
def transformer(num):
  return num*num

def mapAndSquare(foo, list):
  result = []
  for item in list:
    result.append(foo(item))
  return result
print(mapAndSquare(transformer, [2,3,4]))

#List Comprehension
evens = [n for n in [1,2,3,4] if n % 2 == 0]
print(evens)

#Error handling
# Other Exceptions: https://docs.python.org/3/library/exceptions.html
def somefoo(num):
  try:
    int(num)
  except ValueError:
    print(ValueError)
    
somefoo("abc")


#importing libraries
import random as rand

print(rand.randint(1,20))

#Reading in files 
with open("frankenstine.txt") as file:
  lines = file.readlines()
print(lines[0])


#Activity 
# Instructions
# Open the file penguins.csv.
# Read each line from the file.
# Remove extra whitespace and newline characters.
# Store each row in a list.
# Print the data in a readable format like so 'Column Name : Data' for every item in a row