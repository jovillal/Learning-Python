#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cats = [Cat("Xerxes",12), Cat("Bagheera",11), Cat("Ramona",13)]

# 2 Create a function that finds the oldest cat

def oldestCat(catlist):
    ages = [x.age for x in catlist]
    oldest = ages.index(max(ages))
    return catlist[oldest]

oldcat = oldestCat(cats)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

oldcat = oldestCat(cats)

print(f"Oldest cat is {oldcat.name}, its {oldcat.age} years old.")
