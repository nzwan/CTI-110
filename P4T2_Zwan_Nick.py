# Nicholas A. Zwan
# P4T2
# Calculate total number of bugs collected. Initiate accumulator. 
#03/19/18

total = 0

for day in range(1, 8):
    print('Enter the bugs collected on day', day)

    bugs = int(input())

    total = total + bugs

print ('You collected a total of', total, 'bugs.') 

