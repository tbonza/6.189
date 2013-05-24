##Exercise 1.7 - Rock, Paper, Scissors

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

#Get inputs for players

print "Rock, Paper, Scissors...Shoot!"
player1 = raw_input("Player 1?")
player2 = raw_input("Player 2?")


#Select the winner of RPS
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
       
# Notify winner of RPS
print select_winner(player1,player2)
     
        