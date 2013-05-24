# Name: Tyler Brown
# Section:
# nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''
#pile
#max_stones
    ## Basic structure of program (feel free to alter as you please):
#    while [pile is not empty]:

    def valid_input(inp):
        '''
        A function to determine if a players input is valid 
        for nims
        '''
        if (inp >= 1 and inp <= max_stones and inp <= pile):
            return True
        else:
            return False
         
    while pile > 0:
        
        #player 1
#            while [player 1's answer is not valid]:
#            [ask player 1]
#            [execute player 1's move]
        
        print "Player1, there are", pile, "stones left"
        player1 = 0
        while not valid_input(player1):
            player1 = input("Player1: How many stones will you take?")
            #legal answer?
            if not valid_input(player1):
                print "You entered too many stones or",\
                      " took more than is in the pile"
                      
        pile -= player1 #remove stones from pile
        if pile == 0:
            print "Congrats Player1...you did it!"
            break
        
        #player 2
#            while [player 2's answer is not valid]:
#            [ask player 2]
#            [execute player 2's move]

        print "Player2, there are", pile, "stones left"
        player2 = 0
        while not valid_input(player2):
            player2 = input("Player2: How many stones will you take?")
            #legal answer?
            if not valid_input(player2):
                print "You entered too many stones or",\
                      " took more than is in the pile" 
                      
        pile -= player2 #remove stones from the pile
        if pile == 0:
            print "Congrats Player2...you did it!"
            break


print "Nim's test with a pile of 20, max stones of 5\n"
play_nims(20,5)
print "\nNim's test with a pile of 100, max stones of 20\n"
play_nims(100,20)
print "\nNim's test with a pile of 100, max stones of 5\n"
play_nims(100,5)
print "\nNim's test have concluded"
