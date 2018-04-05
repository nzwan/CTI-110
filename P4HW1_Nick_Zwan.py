#Nicholas A. Zwan
#03/15/18
#Calculate the distance of a vehicle using while loops
#P4HW1
speed = int( input('What is the speed of the vehicle?'))

time = int(input('What is the number of hours traveled?'))


print ('Hour    Distance Traveled')
print ('-------------------------')


       
for count in range(1, time + 1):
    distance = speed * count
    print (count,"\t", distance)

           
    
    

##while distance < 40:
##             print('The distance is 40')
##while distance < 80:
##             print('The distance is 80')
##while distance < 120:
##             print('The distance is 120')
               
