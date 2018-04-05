# CTI 110

# P5HW2

# Nicholas A. Zwan

# 04/05/18

# Create a random number guessing game.

import random

def generateRandomNumber():
    randomNumber = random.randint(1, 100)
    return randomNumber

def askUserForNumber( message = 'Guess the Number: '):
    userNumber = int( input( message ) )
    return userNumber

def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return 'Too High'
    elif userNumber < randomNumber:
        return 'Too Low'
    else:
        return 'Congrats!'

def main():
    playAgain = 'yes'
    
    while playAgain == 'yes':
        userNumberOfGuesses = 0
        randomNumber = generateRandomNumber()
        print( 'For testing purposes, random number: ', randomNumber )
        userNumber = askUserForNumber()
        userNumberOfGuesses += 1
        message = checkUserNumber( userNumber, randomNumber )
        
        while message != 'Congrats!':
            print( message )
            userNumber = askUserForNumber( 'Try again: ' )
            userNumberOfGuesses = userNumberOfGuesses + 1
            message = checkUserNumber( userNumber, randomNumber )
        
        print()
        print( message, 'It took you', userNumberOfGuesses,\
               " attempts to guess correctly\n" )
        playAgain = input( 'Would you like to play again: ' )
    
    print( '\nThanks for playing :) ' )

main()


