num = 0
tot = 0
while True:
    sval = input('Enter number:')
    if sval == 'done' :
        break
    try :
        fval = float(sval)
    except :
        print('Invalid number')
        continue
    tot=tot+fval
    num=num+1
print(tot, num, tot/num)
