'''
Object Oriented Programing
The basics

created by jovillal 5/06/23
'''

class PlayerCharacter:
    membership = True #A class object attribute (static)

    #attributes (accesed via ".")
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #Class methods
    @classmethod
    def adding(cls, *args):     #cls is same as self but used when defining class methods
                                #*args denotes several arguments
        #cls can be used for somthing, even instancing
        #cls("Tedy", args[0]) would create a new class instance
        print(args[0])
        return sum(args)
    
    #Static methods
    @staticmethod
    def minus(*args):           #no access to the class 
                                #*args denotes several arguments
        return -sum(args)
    
    #methods
    def run(self):
        print("Run motherfucker.") 
    
    def shout(self):
        print(f'My name is {self.name}')

player1 = PlayerCharacter("Cindy",44)
print(player1.name) #attributes are accessed using the atribute name
print(player1.age)
player1.run()       #methods use "()"
player1.shout()
player1.membership=False     #class object atributes can be modified for instances
print(player1.membership)
print(PlayerCharacter.membership)
print(PlayerCharacter.adding(1,2,3,4,5)) #use the class method without needing an instance
print(PlayerCharacter.minus(1,2,3,4,5)) #use the static method without needing an instance