hrs = input("Enter Hours:")# input only rads a string
h = float(hrs)# asine new varible and confer string to float (3.5)
rt = input("What is a rate:")
rt = float(rt)
if h > 40.0:
   otrt = rt * 1.5
   oth = h - 40.0
   stanPay = rt * 40.0
   overTimePay = oth * otrt
   print("Your total pay is: ", stanPay + overTimePay)
else:
    print("Your total pay is: ", rt * h)
    #Comma(,) betwin string and anyting else in print function.
print('The End!')
