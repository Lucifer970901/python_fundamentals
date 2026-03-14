class Animal:
    '''def __init__(self,name,species):
        self.name = name
        self.species = species

    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.age = age'''
    def __init__(self,*args):
        if len(args) ==1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.species = args[1]
        elif len(args) ==3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]

    def make_sound(self,sound):
        return f"the animal is {self.name} and says {sound}"


dog = Animal('dog','mammal',14)
print(dog.age)
print(dog.make_sound("woof woof"))