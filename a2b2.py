# -*- coding: UTF-8 -*-
num_input=input("input number")
max_num = int(num_input)
for a in range(max_num * -1, max_num):
    for b in range(max_num * -1, max_num):
        c = a * a + b * b
        if c >= 0and c <= 100:
            print('Found ! a=%d b=%d'%(a,b))
