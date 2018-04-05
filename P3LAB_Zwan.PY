# CTI-110
# This program takes a number grade and outputs a letter grade.
# Nicholas A. Zwan
# 02/23/18
# TO DO: define the rest of the scores

score = int( input( 'Enter grade:' ))

A_score = 90
B_score = 80
C_score = 70
D_score = 60
F_score = 50

if score >= A_score:
        print ('Your grade is A' )
elif score >= B_score:
        print ('Your grade is B' )
elif score >= C_score:
        print ('Your grade is C' )
elif score >= D_score:
        print ('Your grade is D' )
elif score >= F_score:
        print ('Your grade is F' )

input('Press any key to continue')
        
