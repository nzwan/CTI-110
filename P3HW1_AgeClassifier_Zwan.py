# CTI 110
# P3HW1 - Age Classifier
# Nicholas A. Zwan
# 02/22-18

age= int(input('Please enter your age'))

if age <= 1:
    print ('You are an Infant' )
elif age < 13:
    print ('You are a child' )
elif age < 20:
    print ('You are a teenager' )
elif age >= 20:
    print ('You are an adult' )
