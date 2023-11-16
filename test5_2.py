lgnum = None
smnum = None
while True:
    inpnum = input('Enter number: ')
    if inpnum == 'done' :
        break
    try :
        valin = int(inpnum)
    except :
        print('Invalid input')
        continue 
    if lgnum is None :
        lgnum = valin
        smnum = valin
    elif valin > lgnum :
        lgnum = valin
    elif valin < smnum :
        smnum = valin
print('Maximum is ', lgnum)
print('Minimum is ', smnum)
