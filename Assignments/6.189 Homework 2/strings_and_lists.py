# Name: Tyler Brown
# Section:
# strings_and_lists.py

# **********  Exercise 2.7 **********

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])


def cumulative_sum(number_list):
    # number_list is a list of numbers
    count = 0
    sum = 0
    b = number_list[:]
    ##### YOUR CODE HERE #####
    for num in number_list:
        sum += num
        number_list[count] = sum
        count += 1
        
    return number_list, b


# Test Cases
##### YOUR CODE HERE #####

print cumulative_sum([4, 3, 6])
print cumulative_sum([1, 2, 3, 4])

# **********  Exercise 2.8 **********

class_taken = raw_input("\nList the classes you took,"
                            " separated by a comma\n")
grade_earned = input("List the corresponding grade you"
                         " earned, separated by a comma\n")

def report_card(grade_earned):
    ##### YOUR CODE HERE #####
    total = 0
    for num in grade_earned:
        total += num
        
    return total/len(grade_earned)
    
# Test Cases
## In comments, show the output of one run of your function.
print "\nAverage GPA:\n", report_card(grade_earned)

# **********  Exercise 2.9 **********

# Write any helper functions you need here.

def find(str, ch):
    index = 0
    while index < len(str):
        if str[index] == ch:
            return index
        index = index + 1
    return -1

VOWELS = ['a', 'e', 'i', 'o', 'u']

def pig_latin(word):
    # word is a string to convert to pig-latin
    ##### YOUR CODE HERE #####
    #first letter a vowel?
    if (find(VOWELS, word[0]) == True):
    #move first letter to back and append hay
        pig_lat = word[1:] + word[0]
        pig_lat += "hay"
        return pig_lat
    elif len(word) > 0:
    #move first letter to back and append ay
        pig_lat = word[1:] + word[0]
        pig_lat += "ay"
        return pig_lat
    else:
        return "error dude"
  
# Test Cases
##### YOUR CODE HERE #####

print "\nTest cases for Pig Latin"
print "pirates in pig Latin:", pig_latin("pirates")
print "donkey in pig Latin:", pig_latin("donkey")
print "elvis in pig Latin:", pig_latin("elvis")

# **********  Exercise 2.10 **********
# Test Cases
##### YOUR CODE HERE #####

#1. print a list of cubes for the numbers 1-10
s = [x**3 for x in range(1,11)]
print "\n A list of cubes for the numbers 1-10:", s

#2. print out the possible results of two coin flips
toss_a = ['H', 'T']
toss_b = ['h', 't']
t = [(x,y) for x in toss_a for y in toss_b]
print "\n Possible results for two coin flips:", t

#3. A function that takes in a string and uses a list 
#   list comprehension to return all the vowels in the
#   string. 
def find_vowels(str):
    index = 0
    ch = ['a', 'e','i', 'o','u'] #vowels
    vowels = [(x,y) for x in str for y in ch if x == y]
    return vowels

#test 2.10.3
print "\n Find the vowels for pirates", find_vowels("pirates")

#4. Write a nested loop that gives you the same result:
print "\nCalculated using a list comprehension:"
[x+y for x in [10,20,30] for y in [1,2,3]]

print "\nCalculated using nested loops:"
def sum_fun():
    for x in [10,20,30]:
        #now add to y
        for y in [1,2,3]:
            y += x
            print y

print sum_fun()      

# **********  Exercise OPT.1 **********
# If you do any work for this problem, submit it here 
