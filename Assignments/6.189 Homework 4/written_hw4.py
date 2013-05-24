# Name: Tyler Brown
# Section:
# written_hw4.py

# **********  Exercise 4.4 ********** 
# For this exercise, describe a generic superclass and at least three
# subclasses of that superclass, listing at least two attributes that
# each class would have. 

class Pizza:
    Attributes: self.crust, self.flour_type

class Cheese(Pizza): # Inherits from Pizza
    Attributes: self.romano, self.mozzarella
    
class Toppings(Pizza): # Inherits from Pizza
    Attributes: self.buffalo_chicken, self.jalapenos
    
class Sauce(Pizza): # Inherits from Pizza
    Attributes: self.tomato_basil, self.chunky_or_not

# **********  Exercise 4.5 **********

# 1. What are the parent and child classes here?
#
#    Parent class: Spell
#    Child classes: Accio, Confundo

# 2. What does the code print out?
#
#   It takes on the attributes of the spell class and
#   inputs the Accio and Confundo parameters 

# 3. Which get_description method is called when 
#    'study_spell(Confundo())' is executed? Why?
#
#    The get_description under the Confundo class is executed
#    because it overrides the one in the Spell class. 

# 4. What do we need to do so that 'print Accio()' will print the 
#    appropriate description ('This charm summons an object to the
#    caster, potentially over a significant distance')? Write down 
#    the code that we need to add and/or change.
#
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
        
    def get_description(self):
        return 'This charm summons an object to the caster,'\
               'potentially over a significant distance'

# **********  Exercise 4.6 **********
# Please help Alyssa implement the CampusAddress class

class Address:
    def __init__(self, street, num):
        self.street_name = street
        self.number = num
        
class CampusAddress(Address):
    def __init__(self, addr):
        street = 'Massachusetts Ave'
        num = 77
        self.street_name = street
        self.number = num
        self.office_number = addr
