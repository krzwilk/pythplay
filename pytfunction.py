def computepay(hrs, rate):
    if hrs > 40:
        p = (hrs - 40)*(rate * 1.5) + 40 * rate
    else:
        p = hrs * rate    
    return p
'''
Write a program to prompt the user for hours and rate per hour using
input to compute gross pay. Pay should be the normal rate for hours up 40
and time-and-half for the hourly rate for all hours worked above
40 hours. Put the logic to do the computation of pay in a function
called computepay() and use the function to do the computation.
The function should return a value. You should use input to read a string
and float()to convert the string to a number.
Do not name your varible sum or use the sum() function.
 '''
hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs, rate)
print("Pay", p)