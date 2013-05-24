# Name: Tyler Brown
# Section:
# written_hw3.py

# **********  Exercise 3.7 ********** 

#Mutable: Elements can be modified
 #lists

#Immutable: Elements cannot be modified
 #strings
 #tuples

# **********  Exercise 3.8 **********

#Bugs
 #1. def negate(num)
    #How do you deal with negative numbers or 0?
    # Do some stuff with if, elif, else
 #2. def large_num(num):
    #What value will be returned?
    # return num
 #3. def negate(num)
    #needs a loop if he's going to deal with lists
    #for i in range(len(num)):
     #if num[i] > 0:
       #etc.

# **********  Exercise 3.9 **********

#Mystery Program
 #1
  #if the first letter in the string answer is 'y'
 #2
  #just once if you get it
 #3
  # To ask if mid_n is the right answer
 #4
  #'y'
 #5
  # it should increase the minimum number than
  # therefore change mid_n
 #6
  # min_n: define the min and change mid_n 
  # max_n: define the max and change mid_n
  # mid_n: define the answer, the user just needs
  #        to recognize the answer and they win

# **********  Exercise 3.10 **********

 #1 What is the difference between a local variable and an 
 #  an object's attribute?
 # 
 # An attribute is an item selected from an instance. So
 # an item could be a shoe. One instance of a shoe is the 
 # color red. The attribute of this particular shoe is 
 # that it's red.
 #
 # A local variable applies only to the method/function of
 # which it has been called. This contrasts an attribute
 # which applies to an item which may include several methods/
 # functions. 
 
 #2 What method is called when the object is created?
 #
 # You want an initialization method, __init__, to be called. 
 
 #3 If you have an object instance, obj, and you want to call 
 #  it's do_something() method (assuming it has one), how 
 #  would you do this? (write the line of code you would use)
 #
 # You would use dot notation. obj.do_something()
 
# **********  Exercise 3.11 **********

#1 Write a class called Address that has two attributes: number
# and street_name. 

class Address():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        return True
    
#2 Consider the following code:
 #a What does the code print out? 
 #  5:30
 
 #b Is that what you expected?
 # No, I thought it would be 6:30. It seems like time is passed
 # and that's what changes the defined variable
 
#3 Consider the following code:
 #a What does the code print out?
 #  It doesn't take any arguments
 #
 #b What does this tell you about giving parameters the same 
 #  name as object attributes?
 # You can't do it because it won't be recognized. 
 
#4 Consider the following code:
 #a What does the code print out?
 #
 #  10:30, paris_clock time
 #
 #b Why does it print what it does?
 #
 # boston_clock was set equal to paris_clock and then
 # the attribute to paris_clock was changed to 10:30.
 # Therefore, boston_clock also became 10:30