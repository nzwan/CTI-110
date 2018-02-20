# Nicholas A. Zwan
# P2HW2
# Calculate sales tax of a meal.
# 02/14/18

foodCost = float( input('Please enter meal price: '))

taxPercentage = 0.07

tipPercentage = 0.18

tipAmount = foodCost * tipPercentage

taxAmount = foodCost * taxPercentage

totalCost = foodCost + tipAmount + taxAmount

print ('The total cost is ',totalCost) 
