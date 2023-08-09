from random import randint


class Animal:
    def __init__(self, name, age, voice='groal'):
        self.name = name
        self.age = age
        self.voice = voice

    def make_voice(self):
        print(self.voice)


class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales

    def swim(self):
        print("i'm swimming, oh, it's titan!")


class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print('Bark!')


class Raven(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = name

    def fly_around_corpse(self):
        print('oooh, meat....')


class Fabric:
    def __init__(self, name, age, scales, voice):
        match randint(0, 2):
            case 0:
                self.animal = Fish(name, age, scales, voice)
            case 1:
                self.animal = Dog(name, age, scales, voice)
            case 2:
                self.animal = Raven(name, age, scales, voice)

    def get_animal(self):
        return self.animal


animal = Fabric('Nemo', 2, 'silver', 'bul-bul')
print(animal.get_animal())
animal.get_animal().make_voice()
