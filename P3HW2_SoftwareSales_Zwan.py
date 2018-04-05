# CTI-110
# Software Sales
# Nicholas A. Zwan
# 2/23/18

numberOfPackages = int( input( 'Please enter the number of packages:'))

packagePrice = 99

if numberOfPackages  < 10:
    discount = 0
elif numberOfPackages < 20:
    discount = 0.10
elif numberOfPackages < 50:
    discount = 0.20
elif numberOfPackages < 100:
    discount = 0.30
else:
    discount = 0.40

subTotal = numberOfPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print('Amount of discount:' + str( discountAmount ) )
print('The total price:' + str ( total ) )

input ('Press any key to continue')

