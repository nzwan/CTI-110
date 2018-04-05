# Nicholas A. Zwan
# P4HW3
# Display the factorial using loops
# 03/19/18

num = int( input("Please enter a non-negative integer:"))

factorial = 1

for currentNum in range( 1, num + 1 ):
           factorial = factorial * currentNum

print()
print( "The factorial of", num, "is", factorial )
            
