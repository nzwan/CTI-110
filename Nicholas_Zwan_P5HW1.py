# CTI 110

# P5HW1

# Nicholas A. Zwan

# 04/03/18

# Get input from user to display average and grade. 

def calcAverage( score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average

def determineGrade( testScore ):
    if( testScore < 60 ):
        return 'F'
    elif( testScore < 70 ):
        return 'D'
    elif( testScore < 80 ):
        return 'C'
    elif( testScore < 90 ):
        return 'B'
    elif ( testScore < 101 ):
        return 'A'

def getScore():
    score1 = float( input( 'Please enter score 1: ' ) )
    score2 = float( input( 'Please enter score 2: ' ) )
    score3 = float( input( 'Please enter score 3: ' ) )
    score4 = float( input( 'Please enter score 4: ' ) )
    score5 = float( input( 'Please enter score 5: ' ) )

    return score1, score2, score3, score4, score5

def printResultsTable ( score1, score2, score3, score4, score5 ):
    print( 'Score\tLetter Grade' )
    print( str( score1 ) + '\t' + determineGrade( score1 ), \
           str( score2 ) + '\t' + determineGrade( score2 ), \
           str( score3 ) + '\t' + determineGrade( score3 ), \
           str( score4 ) + '\t' + determineGrade( score4 ), \
           str( score5 ) + '\t' + determineGrade( score5 ), sep = '\n')

    print( "Your average is", calcAverage( score1, score2, score3, score4,\
                                           score5 ) )

def main():
    score1, score2, score3, score4, score5 = getScore()
    printResultsTable (score1, score2, score3, score4, score5 )

main()

print ('Press any key to continue')

