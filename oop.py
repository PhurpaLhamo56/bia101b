class Dog: 
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color

    def say_age(self):
        words_to_say = "I am " + str(self.age) + " years old"
        print(words_to_say)    

    def bark(self):
        print("Woof! Woof!")

    def sleep(self):
        print("Zzzz...")

    def eat(self):
        print("Nom nom nom!")    

dog = Dog('bhutanese', 20, 'black')
petdog = Dog('pug', 10, 'white')

dog.say_age()
petdog.say_age()

#dog.eat()
#dog.sleep()
#dog.bark()