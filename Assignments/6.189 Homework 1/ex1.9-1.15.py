##Exercise 1.9 - Variable Names

#Which of the following are legal Python names?

 #keyword
 and
 
 #starts with number
 1var
 
 #uses an operator
 my-name
 
 #legal
 _and
 var
 var1
 your_name
 COLOR

##Exercise 1.10 - Types

#Which type of value is stored in each variable?

a = False #boolean
b = 3.7 #float
c = 'Alex' #string
d = 7 #integer
e = 'True' #string
f = 17 #integer
g = '17' #string
h = True #boolean
i = '3.14159' #string 

##Exercise 1.11 - Natural Language Processing

#1
 #A girl, a boy, a hill, a telescope
 
#2
 #A girl on a porch with a telescope, a boy on a hill
 
#3
 #A girl named Alice saw a boy on a hill with her telescope
 #A girl named Alice had a telescope in her room in her house
 #that she used to see a boy on a far away hill. 
 
#Think about "prepositional phrase attachment"

##Exercise 1.12 - Boolean operators

#1 b and c
 #False

#2 b or c
 #True
 
#3 not a and b
 #True
 
#4 (a and b) or not c
 #True
 
#5 not b and not (a or c)
 #False
 
##Exercise 1.13 - Conditionals

#1
 # No way
 
#2
 # No 

#3
 # Yes

#4
 # Yes
 
#5
 # No way
 
##Exercise 1.14 - Understanding loops
 
#1 
 # 10,9,8,7,6,5,4
 
#2
 # 0,1,2,3,4
 
#3
 # 10, 9, 8, 7
 
#4
 #Letter # 4 is ! (etc.) (remember it starts at 0)
 
##Exercise 1.15 - Buggy loop (aka Find The Bug!)

#1 n = 10, i = 1,2

#2 
 # I think he was trying to see if ten is divisible by two. If 
 # not then count up from ten until it is divisible by two. 

num = 10

for i in range(num)
    if  (10 % 2 == 0):
        print "sick!"
    elif (10 % 2 > 0):
        num++
    else:
        print "error"
    