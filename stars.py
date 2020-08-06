
a = int(input('有幾層'))  
for i in range(1,a+1):
    for n in range(a-i):
        print(' ',end='')
    for y in range(i):
        print('*',end='')
    print('')