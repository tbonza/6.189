# Name: Tyler Brown
# Section:
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######
import math #relates to exercises 2.3, 2.5
import random  #relates to exercise 2.4

# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 

# Define your function here
##### YOUR CODE HERE #####

#Create a truth table:

###################################
# Player 1 # Player 2 # Result
# # # # # # # # # # # # # # # # # #
# Rock     # Rock     #  Tie
# Rock     # Scissors #  Player 1
# Rock     # Paper    #  Player 2
# Scissors # Scissors #  Tie
# Scissors # Paper    #  Player 1
# Paper    # Paper    #  Tie
###################################

#Select the winner of RPS using a function call
def select_winner(player1, player2):
    if (player1 == 'Rock' and
        player2 == 'Rock' ):
        return "Tie"
    elif (player1 == 'Rock' and
        player2 == 'Scissors' ):
        return 'Player 1 wins'
    elif (player1 == 'Rock'  and
        player2 == 'Paper' ):
        return 'Player 2 wins'
    elif (player1 == 'Scissors'  and
        player2 == 'Scissors' ):
        return 'Tie'
    elif (player1 == 'Scissors'  and
        player2 == 'Paper' ):
        return 'Player 1 wins'
    elif (player1 == 'Paper'  and 
        player2 == 'Paper' ):
        return "Tie"
    else:
        return "Error dude"
       
# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####

print "\n select_winner test cases "
print select_winner("Paper", "Paper") #Tie

print select_winner("Rock", "Scissors") #Player 1 wins

print select_winner("Rock", "Paper") #Player 2 wins

# ********** Exercise 2.2 ********** 

# Define is_divisible function here
##### YOUR CODE HERE #####

def is_divisible(m,n):
    if m and n > 0:      
        if m % n == 0:
            return True
        elif m % n != 0:
            return False
        else:
            return "error dude"
    else:
        return "hollah"
        

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print "\nis_divisible tests"
print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return?

# Define not_equal function here
##### YOUR CODE HERE #####

def not_equal(x,y):
    if x > y or x < y:
        return "not equal"
    else:
        return "equal"

# Test cases for not_equal
##### YOUR CODE HERE #####

print "\nnot_equal function tests"
print not_equal(3,4)
print not_equal(-3,4)
print not_equal(3,3)

# ********** Exercise 2.3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####

def multadd(a,b,c):
    return a * b + c

print "\n Multadd function tests"
print multadd(1,2,3)
print multadd(4,3,2)
print multadd(10,0,9)

## 2 - Equations
##### YOUR CODE HERE #####

#angle test
multadd(1,math.sin(math.pi/4), math.cos(math.pi/4)/2)

#ceiling test
multadd(2, math.log(12, 7), math.ceil(276/19))

# Test Cases
angle_test = multadd(1,math.sin(math.pi/4), math.cos(math.pi/4)/2)
print "\nsin(pi/4) + cos(pi/4)/2 is:" 
print angle_test

ceiling_test = multadd(2, math.log(12, 7), math.ceil(276/19))
print "\nceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####
def yikes(x):
    return multadd(1, x* math.exp(-x), math.sqrt(1-math.exp(-x)))

             
# Test Cases
x = 5
print "\nyikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####

def rand_divis_3():
    y = random.randint(0,100)  
    if y % 3: #is the random number divisible by 3?
        return True
    else:
        return False

# Test Cases
##### YOUR CODE HERE #####

print "\ntest rand_divis_3()", rand_divis_3()

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####

def roll_dice(sides,num_dice):
    while num_dice > 0:
        print random.randint(1,sides)
        num_dice -= 1
    return "That's all folks!"
    
# Test Cases
##### YOUR CODE HERE ##### 

print "\nroll tha dice mon!", roll_dice(5,3)   
print "and then?\n", roll_dice(4,2)
print "and then??\n", roll_dice(3,6)                        

# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####   

def roots(a,b,c):
    if ((b**2 - 4*a*c) > 0):
        x = (-b + math.sqrt(b**2 - 4*a*c))/2*a
        y = (-b - math.sqrt(b**2 - 4*a*c))/2*a
        return x, y 
    elif ((b**2 - 4*a*c) < 0):    #we cannot take the sqrt of a 
        return "No real roots"  #negative number, so no real roots
    elif ((b**2 - 4*a*c) == 0):
        x = (-b + math.sqrt(b**2 - 4*a*c))/2*a
        return x
    else:
        return "Error dude"
    # Test Cases
##### YOUR CODE HERE ##### 

print "\nTest Cases for Roots Functions"
print roots(1,2,3)
print roots(0,0,4)
print roots(-4,3,2)