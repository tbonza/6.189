##Exercise 1.8 - For & While Loops
#1 using a for loop

print "Exercise 1.8.1\n" 

for num in range(2, 11, 1):
    print 1.0 / num
    
print "\nExercise 1.8.2\n"

#user picks a number
choice = input("Pick a number!:")

if(choice > 0):
    for i in reversed(range(0,choice,1)): #loop positive num reverse
        print i
elif(choice < 0):
    for i in reversed(xrange(0, choice,-1)): #loop negative num to 0
        print i
else:
    print"error dude"

print "\nExercise 1.8.3\n"

base = input("Can I have a base number?"
             "This is going to be sweet:")
exp = input("Enter an exponent:")

#write a for loop that counts up the exponents from the base
for i in range(exp):
    print base**i
    
print "\nExercise 1.8.4\n"

#user enters a number
user = input("Choose a number divisible by two:")
check = user % 2.0 #see if number/2 by checking the modulus

#if modulus > 0 then it's not divisible by two
while  check > 0:
    user = input("Shiver me timbers and blow me down!\n"
                 "Unfortunately, your number is not "
                 "divisible by two.\n"
                 "Choose a number divisible by two:\n")
    check = user % 2.0