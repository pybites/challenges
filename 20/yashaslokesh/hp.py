from collections import namedtuple

class Person(object):

    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

houses = ['gryffindor', 'hufflepuff', 'slytherin', 'ravenclaw']
cores = {'unicorn':'Unicorn Hair', 'dragon': 'Dragon Heartstring', 'phoenix':'Phoenix Feather'}
woods = ('acacia alder apple ash aspen beech blackthorn black-walnut cedar cherry chestnut cypress '
    'dogwood ebony elder elm english-oak fir hawthorn hazel holly hornbeam larch laurel maple '
    'pear pine poplar red-oak redwood rowan silver-lime spruce sycamore vine walnut willow yew').split()
Wand = namedtuple('Wand', 'core length flexibility wood')

class Wizardkind(Person):

    def __init__(self, name):
        super().__init__(name)
        self._house = 'Not set'
        self._wand = 'Not set'
        self._friends = []

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house.lower() in houses:
            self._house = house
        else:
            raise ValueError("Please enter a valid Hogwarts House!")
    
    @property
    def wand(self):
        return self._wand

    @wand.setter
    def wand(self, wand):
        # Can't use backslash in f-strings, so nl = '\n' is used in backslash's place.
        nl = '\n'
        if not isinstance(wand, Wand):
            raise ValueError(f'{wand} is not of type Wand, which is a named tuple')
        if wand.core.lower().strip() not in cores:
            raise ValueError(f'{wand.core} is an invalid type for core, choose from: \n{nl.join(cores)}')
        if wand.wood.lower().strip() not in woods:
            raise ValueError(f'{wand.wood} is an invalid type for wood, choose from: \n{nl.join(woods)}')

        self._wand = wand
    
    @property
    def friends(self):
        return self._friends
    
    @friends.setter
    def friends(self, value):
        self._friends = value
    
    def add_friend(self, friend):
        if isinstance(friend, Person):
            self._friends.append(friend)
        else:
            raise ValueError('Wizardkind can only be friends with another Person')
    
    def remove_friend(self, friend):
        if isinstance(friend, Person):
            self._friends.remove(friend)
        else:
            raise ValueError('Wizardkind can only be friends with another Person')

    def __eq__(self, wizard):
        result = False

        if (self._name == wizard.name and self._house == wizard.house and
           self._wand == wizard.wand and self._friends == wizard.friends):
           result = True

        return result
    
    def __str__(self):
        friends_names = ', '.join(friend.name for friend in self._friends)
        return (f'Name: {self._name}\nHouse: {self._house}\nWand: {self._wand}\n'
                f'Friends: {friends_names}')

def main():
    harry = Wizardkind("Harry Potter")
    print(harry)

    harry.house = "Gryffindor"
    harry_wand = Wand("phoenix", 11, "supple", "holly")
    harry.wand = harry_wand

    assert(harry == harry)
    print(harry)

    hermione = Wizardkind("Hermione Granger")
    hermione.house = "Gryffindor"

    ron = Wizardkind("Ron Weasley")
    ron.house = "Gryffindor"

    hermi_wand = Wand('dragon', 10.75, 'N/A', 'vine')
    ron_wand = Wand('unicorn', 14, 'N/A', 'willow')

    hermione.wand = hermi_wand
    ron.wand = ron_wand

    harry.add_friend(hermione)
    harry.add_friend(ron)

    hermione.add_friend(ron)
    hermione.add_friend(harry)

    ron.add_friend(hermione)
    ron.add_friend(harry)

    print()
    print(harry)
    print()
    print(ron)
    print()
    print(hermione)
    print()

if __name__ == '__main__':
    main()

        

    