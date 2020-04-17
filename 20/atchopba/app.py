#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

# human class
class Human(object):
    
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    
    def __str__(self):
        return "<name: {}; sexe: {}>".format(self.name, self.sex)
        

# car class
class Car(metaclass=ABCMeta):
    #
    def __init__(self, brand):
        self.brand = brand
        self.human = None
        
    def setHuman(self, human):
        self.human = human
        
    def __str__(self):
        return "<human: {}  have a car brand {}>".format(self.human, self.brand)
    
    @abstractmethod
    def charging(self):
        pass


# Peugeot308 class
class Peugeot308(Car):
    #
    def __init__(self):
        super().__init__("Peugeot 308")
    #
    def charging(self):
        print("{} charges with diesel".format(self))

        
# Zoe car class
class Zoe(Car):
    #
    def __init__(self):
        super().__init__("Zoe")
        
    #
    def charging(self):
        print("{} charges with electricity".format(self))


# Test of code class
human = Human("sophie", "f")
print(human)
#
peugeot308 = Peugeot308()
peugeot308.setHuman(human)
peugeot308.charging()
#
zoe = Zoe()
zoe.setHuman(human)
zoe.charging()