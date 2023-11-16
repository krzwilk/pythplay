#largest = None
smallest = None
from heapq import nsmallest


num = None
for num in input("Enter a number: "):
   # num = input("Enter a number: ")
    num = float(num)
    if num < num:
        num = nsmallest

    
    largest = num > num 
    if num == "done":
        break
    print(num)

print("Maximum", largest)
print("Minimum" , smallest)