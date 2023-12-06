'''
Object Oriented Programing
Inheritance

created by jovillal 6/06/23

The idea is to give attributes and methods of a parent class to another class
'''

#This is the parent class

class User():
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print("Logged in,")

#These classes will inherit User methods and attributes

class Wizard(User):
    def __init__(self, name, power): #this overrides the User __init__
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with {self.power} power!!')

class Archer(User):
    def __init__(self, name, arrows, email):  
        #User.__init__(self,email)   #This uses the __init__ from the parent class old school style
        super().__init__(email)     #This uses the __init__ from the parent class new school style. No need to name the class, don't pass self
        self.name = name
        self.arrows = arrows 

    def attack(self):
        if(self.arrows > 0):
            print(f'Attacking with arrows!!')
            self.arrows -=  1
        else:
            print("Out of arrows")

    def run(self):
            print("Ran away faster.")


    def check_arrows(self):
        print(f'You have {self.arrows} arrows left.')

#Multiple inheritance
class HybridBorg(Wizard,Archer):       #inherits everything but only asks for Wizard initialization arguments
    def __init__(self, name, power, arrows,email):  #used to capture Archer initialization
        Archer.__init__(self,name,arrows,email)
        Wizard.__init__(self,name,power)

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 25, 'robin@hood.fr')

wizard1.attack()  #these are examples of polymorphism
archer1.attack()
wizard1.attack()
archer1.attack()

for x in (wizard1,archer1):
    x.attack()

wizard1.sign_in()

#to check if an instance is a particular class or a child of anoter class
#use isinstance(instance, Class)
print(isinstance(wizard1,Wizard))
print(isinstance(wizard1,User))
print(isinstance(wizard1,object)) #object is a parent (base) class of everything in Python

print(archer1.email)

hb1 = HybridBorg("Borgie",60,25,"borgie@st.sp")
hb1.attack()            #How to attack with arrows?
hb1.run()
hb1.check_arrows()
print(HybridBorg.mro())        #this checks the order in which parests are checked to resolve attributes or methods
