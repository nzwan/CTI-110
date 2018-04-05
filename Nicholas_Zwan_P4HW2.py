# Nicholas A. Zwan
# P4HW3
# Accumluate a total using loops
# 03/21/18

def main():
    total = 0
    newNumber = float(input('Enter a number or enter a negative number to quit: ' ))

    while newNumber > -1:
        total = total + newNumber
        newNumber = float(input('Enter a number or enter a negative number to quit: '))

    print ('The total is', total)

main()
