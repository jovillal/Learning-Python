"""
Created on Thu Nov 2 12:14:04 2023

@author: jovillal
Regular expresions or regex
check:
	- https://regexlearn.com/learn/regex101, for a tutorial
	- https://regex101.com/, to check regular expressions
	- https://regexone.com/lesson for exercises
"""
import re

#use in to check if a substring can be found inside a string
string = "Hay 2 usuarios que no están en nuestro sistema entonces los agregaremos.\nQuedamos muy pendientes de si para los otros hay algun comentario adicional o podemos dejarlos OK."

print("ent" in string)
print("Ent" in string)

#re.search allows for search within a string
a = re.search("ent",string)
print(a)
print(a.group())
print(a.span())
print(a.start())
print(a.end())
a = re.search("Ent",string)
print(a)

#To search for patterns use compile and search (as a method of the pattern)
pattern = re.compile("ent")
a = pattern.search(string)
print(a)
#compile allows for better searches, one can find all instances
b = pattern.findall(string)
print(b)
#fullmatch checks if the pattern is identical to the string (True or False)
#match checks if the beggining of the string is matched

#one can use raw strings to match
pattern = re.compile(r"([a-zA-Z]).([a])")  #This is any letter, followed by any character and an 'a'
a = pattern.search(string)
print(a)
print(a.group())
b = pattern.findall(string)
print(b)

#here is how to match an email address
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")  #This is a bunch of stuff of any length, followed by @, then practically anything a '.' and whatever
string = 'jovillal.garbage@gmail.com'
a = pattern.search(string)
print(a)
print(a.group())
string = 'not an email address'
a = pattern.search(string)
print(a)