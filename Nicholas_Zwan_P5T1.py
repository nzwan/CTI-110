# CTI-110
# P5T1
# Nicholas A. Zwan
# 04/03/18
# Convert the distance travled from Kilometers to miles.

CONVERSION_FACTOR = 0.6214

def main():
    kilometers = float(input('Enter a distance in kilometers: '))

    show_miles(kilometers)

def show_miles (km):
    miles = km * CONVERSION_FACTOR 

    print(km, 'kilometers =', miles, 'miles.')


main()

input('Press any key to continue')
