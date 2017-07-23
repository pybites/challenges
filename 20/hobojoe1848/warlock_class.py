#!python3
#Submission for Pybites Code Challenge 20. Using the character class system in
#World of Warcraft as my example.
#I used this opportunity to learn about class inheritance!

#Define Player Character class
class Player(object):
    def __init__(self, name, race):
        self.name = name
        self.race = race

    def get_race(self):
        return self.race

    def get_name(self):
        return self.name


#Define Human Subclass

class Human(Player):
    def __init__(self, name, ability_spec):
        Player.__init__(self, name, "Human")
        self.ability_spec = ability_spec

    def show_spec(self):
        return self.ability_spec


#Define a Human Warlock Subclass

class H_Warlock(Human):
    def __init__(self, name, race, specialization):
        Human.__init__(self, name, "Warlock")
        self.specialization = specialization

    def lock_spec(self):
        return self.specialization


#Create a Player Character
player1 = Player("Ardy", "Human")


#Create the Human subclass
human1 = Human("Ardy", "Warlock")


#Create a Human Warlock Player with a Specialization
ardy = H_Warlock("Ardy", "Human", "Demonology")

#Print Player1 details
print("{} is a {}.".format(player1.get_name(), player1.get_race()))

#Print Human1 Details
print("{} is a {} {}.".format(human1.get_name(), human1.get_race(), human1.show_spec()))

#Print Ardy Details
print("{} is a {} {} specializing in {}.".format(ardy.get_name(),
                                                ardy.get_race(),
                                                ardy.show_spec(),
                                                ardy.lock_spec()))
