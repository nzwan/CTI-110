# CTI-110
# P5T2
# Nicholas A. Zwan
# 4/03/18
# Convert feet to inches

INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter a number of feet: '))

    print(feet, '=', feet_to_inches(feet), 'inches.')

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()

input('Press any key to continue')


