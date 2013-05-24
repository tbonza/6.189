# Name: Tyler Brown
# Section: 
# Date:
# hw1.py

##### Template for Homework 1, exercises 1.2-1.5 ######

print "********** Exercise 1.2 **********"

# Do your work for Exercise 1.2 here

print "  |  |  "
print "--------"
print "  |  |  "
print "--------"
print "  |  |  "

print "********** Exercise 1.3 **********"

# Do your work for Excercise 1.3 here. Hint - how many different
# variables will you need?

a = "  |  |  \n"
b = "--------\n"

print a,b,a,b,a


print "********** Exercise 1.4 **********"
print "********* Part II *************"
import math

print 3*5/(2+3) #1.
print math.sqrt(7+9.0)*2.0 #2
print (4-7)**3 #3
print (-19 + 100)**(1/4.0) #4
print 6 % 4 #5


print "********* Part III *************"

print 4+3*2
print (4+3)*2


print "********** Exercise 1.5 **********"

# input variables
first_name = raw_input("Enter your first name:")
last_name = raw_input("Enter your last name:")
print "Enter your date of birth:"
month = raw_input("Month?")
day = raw_input("Day?")
year = raw_input("Year?")

#sassy output
print first_name,last_name, "was born on", month,day+',',year
