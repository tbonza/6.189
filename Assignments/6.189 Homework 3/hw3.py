# Name: Tyler Brown
# Section:
# hw3.py

#Libraries used:
import math #Exercise 3.2

##### Template for Homework 3, exercises 3.1 - ######

# **********  Exercise 3.1 ********** 

# Define your function here
##### YOUR CODE HERE #####

def longest_list(x,y): 
    '''
    Determining the longer list helps match 
    lists of unequal length. 
    '''
    long = []
    short = []
    
    if len(x) > len(y):
        long = x
        short = y
    elif len(y) > len(x):
        long = y
        short = x
    elif len(x) == len(y):
        long = x
        short = y
    else:
        return "Error dude"
    
    return long, short

def list_intersection(x,y):
    '''
    Checking elements of the short list
    against the long list. Incrementing
    slice to check out each list element.
    Z is the new list containing matches 
    from x and y.
    '''
    slice = 0
    z = []
    
    long, short = longest_list(x,y)
    
    while slice < len(short):
        if short[slice] in long:
            #Question: What will the time complexity in this algorithm?
            #Example: Is it O(n^2) or O(n)?
            z.append(short[slice])
        slice += 1
    return z

# Test Cases for Exercise 3.1
##### YOUR CODE HERE #####

def test_31():
    '''
    Runs through tests for Exercise 3.1
    '''
    print "Test for longest_list:"
    print longest_list([1,3,5], [5,3,1,6])

    print "\nTest Cases for Exercise 3.1"
    print "Test case 1"
    print list_intersection([1,3,5], [5,3,1])
    print "Test case 2"
    print list_intersection([1,3,6,9], [10,14,3,72,9])
    print "Test case 3"
    print list_intersection([2,3], [3,3,2,10])
    print "Test case 4"
    print list_intersection([2,4,6], [1,3,5])
    print "Tests concluded"
    
print test_31(), "\n"

# **********  Exercise 3.2 **********

# Define your function here
def ball_collide(ball1, ball2):
    '''
    Calculates distance between ball1 & ball2 by
    using the two points to solve for the hypotenuse
    of a triangle. Then subtracting from that hypotenuse
    by the sum of the radii. If sum is <= 0 then ball1
    & ball2 are touching.
    '''
    ##### YOUR CODE HERE #####
    
    #Calculate distance
    x = abs(ball1[0] - ball2[0]) 
    y = abs(ball1[1] - ball2[1])
    
    #Calculate Pythagorean Theorem
    c = x**2 + y**2  # c^2 = x^2 + y^2
    c = math.sqrt(c)
    
    #Calculate distance between ball1, ball2
    t = c - (abs(ball1[2] + ball2[2]))
    
    #Handle touching
    if t <= 0:
        return True
    elif t >= 0:
        return False
    else:
        return "Error dude"    

# Test Cases for Exercise 3.2
def test_32():
    '''
    Runs through tests for Exercise 3.2
    '''
    print "\nTest Cases for Exercise 3.2"
    print ball_collide((0, 0, 1), (3, 3, 1)) # Should be False
    print ball_collide((5, 5, 2), (2, 8, 3)) # Should be True
    print ball_collide((7, 8, 2), (4, 4, 3)) # Should be True
    print "Tests concluded"
    
print test_32(), "\n"

# **********  Exercise 3.3 **********

# Define your dictionary here - populate with classes from last term
my_classes = {'6.123': 'Introduction to Data',
              '7.343': 'Introduction to Stuff',
              '4.683': 'Graduate much?'}

def add_class(class_num, desc):
    ##### YOUR CODE HERE #####
    my_classes[class_num] = desc
    return my_classes

# Here, use add_class to add the classes you're taking next term
add_class('6.189', 'Introduction to Python')

def print_classes(course):
    ##### YOUR CODE HERE #####
    
    #Course numbers from dictionary
    class_numbers = my_classes.keys()
    class_len = len(course)
    
    #Course already listed?
    class_listed = False
    
    #Check class list
    for class_name in class_numbers:
        #Check value key
        if class_name[0:1] == course and class_name[1] == '.':
            
            #Print classes with matching conditions
            print str(class_name)+' - '+my_classes[class_name]
            class_listed = True
            
        # If course_len > 1
        elif class_name[0:class_len] == course:
            print str(class_name)+' - '+my_classes[class_name]
            class_listed = True
            
    # If not classes were listed, notify
    if class_listed == False:
        print str(course)+'was not taken'
        
# Test Cases for Exercise 3.3
##### YOUR CODE HERE #####

def test_33():
    print "Test Cases for Exercise 3.3"
    print print_classes('6') #prints Python course
    print print_classes('8') #returns false 
    print print_classes('4') #prints intro to data
    print "Tests concluded"
    
print test_33(), "\n"


# **********  Exercise 3.4 **********

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
                 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

# Define your functions here

def combine_lists(list_1, list_2):
    comb_dict = {}
    ##### YOUR CODE HERE #####
    for i in range(0, len(list_1)):
        comb_dict[list_1[i]] = list_2[i]
    return comb_dict
 

#Assign combined lists to a dictionary
comb_dict = combine_lists(NAMES, AGES) # Finish this line...

def people(age):
    # Use combined_dict within this function...
    #Store the many people requested
    people_request = []
    
    #loop through ages and add the relevant people
    for person in comb_dict:
        if age == comb_dict[person]:
            people_request.append(person)
    return people_request

# Test Cases for Exercise 3.4 (all should be True)

def test_34():
    print "Tests for Exercise 3.4"
    print 'Dan' in people(18) and 'Cathy' in people(18)
    print 'Ed' in people(19) and 'Helen' in people(19) and\
       'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
    print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)
    print people(21) ==   ['Bob']
    print people(22) ==   ['Kelly']
    print people(23) ==   []
    print "Tests concluded"
    
print test_34(), '\n'

# **********  Exercise 3.5 **********

def zellers(month, day, year):
    ##### YOUR CODE HERE #####
    
    #Dictionary for month order    
    A_month = {'March': 1, 'April':2, 'May':3, 'June':4,'July': 5,
               'August': 6, 'September': 7, 'October':8, 'November':9,
               'December': 10, 'January': 11, 'February': 12}
    
    #calculating the month
    A = A_month[month] # month of the year (March = 1)
    
    #calculating the day
    B = day # day of the month (Day = 1...31)
    
    #calculating the year
    C = str(year) # change year to a string
    C = C[2:4] # year of the century (89 = 1989)
    C = int(C)
    
    #calculating the century
    D = str(year) # the century (19 = 1989)
    D = D[0:2]
    D = int(D)
    
    #Variables to compute day
    
    W = (13 * A - 1) / 5
    X = C / 4
    Y = D / 4
    Z = W + X + Y + B + C - 2*D
    R = Z % 7 #this equals the day of the week
    
    #Use either a list or dictionary to convert the final output
    #of the algorithm to the day of the week. 
    
    A_day = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
             4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    
    Answer = A_day[R]
    
    return Answer
            
# Test Cases for Exercise 3.5
def test_35():
    print "Tests for Exercise 3.5"
    print zellers("March", 10, 1940) == "Sunday" # This should be True
    print zellers("February", 2, 1988) # This should be when I was born
    print "Tests Concluded"
    
print test_35(), "\n"
##### YOUR CODE HERE #####