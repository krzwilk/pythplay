largest_so_far = -1 #sarting number
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :#evaluats number from list to starting number
        largest_so_far = the_num #Assighns new number to starting number
    print(largest_so_far, the_num)

print('After', largest_so_far)