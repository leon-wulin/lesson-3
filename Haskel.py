# -*- coding: UTF-8 -*-
max_num = 9
num_input = input('Type an end number:')
max_num = int(num_input)


frame="Haskell.txt"
f=open(frame,'w')

for a in range(1, max_num+1):
    data=''
    for b in range(1, max_num+1):
        c=a*b
        if b>=a :
            print ("%2dx%2d=%4d\t"%(b,a,c), end='')
            data+="%2dx%2d=%4d\t"%(b,a,c)


    print("\n")
    data+='\n'
    f.write(data)

f.close()
