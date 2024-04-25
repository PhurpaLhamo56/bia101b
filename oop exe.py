class Dog:
    def __init__(name, self, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    
    def introduction(self): 
        print("Hi")
        print("I am a " + self.breed + " dog.") 
        print("I am a " + str(self.age) + " years old")
        print(" I am a "+ self.color + " in color")      
    def bark(self):
        print("Woof! Woof!")

    def sleep(self):
        print("Zzzz...")

    def eat(self):
        print("Nom nom nom!")    

dog = Dog('phurpa', 'bhutanese', 20, 'black')
petdog = Dog('lhamo', 'pug', 10, 'white')

dog.say_age()
petdog.say_age()
dog.introduction()
print(introdution)

dog.eat()
dog.sleep()
dog.bark()   
    


