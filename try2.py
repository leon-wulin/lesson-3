# -*- coding: UTF-8 -*-
h0=100

time=10000

rate=0.5

#-------------------------------------------------------------------------------
SUM=h0

Hn=h0*rate
for n in range(2, time+1):
    SUM+=2*Hn
    print("No.%3d - Hn=%7.4f - SUM=%10.4f"%(n,Hn,SUM))
    Hn*=rate

print(SUM)
