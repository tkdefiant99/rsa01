'''
Created on 14.12.2014

@author: Tommy
'''
from math import sqrt

def factor(n):
    a = []
    boundary = sqrt(n)
    primsfound = False

    for p in range(3,500000,2):
        if (primsfound):
            break
        if all(p%i!=0 for i in range(2,int(sqrt(p))+1)):
            for q in range(3,500000,2):
                if (primsfound):
                    break
                if all(q%i!=0 for i in range(2,int(sqrt(q))+1)):
                    if (((p*q) == n) and (q < boundary)):
                        primsfound = True
                        a.append(p)
                        a.append(q)
                        break
    return a

def findsecret(p, q, e):
    secretfound = False
    '''
    d = 0
    for k in range(1,1000000,1):
        if (((k * (p - 1) * (q - 1) + 1) % e) == 0):
            d = k * ((p - 1) * (q - 1)) + 1
            break
    return d
    '''
    while secretfound != True:
        for d in range(1,1000000,1):
            if (((e * d) % ((p -1) * (q - 1))) == 1):
                secretfound = True
                break
            if (secretfound):
                break
    return d

prims = factor(3599)
print prims[0],prims[1]
d = findsecret(prims[0],prims[1], 31)
print d

prims = factor(18923)
print prims[0],prims[1]
d = findsecret(prims[0],prims[1], 1261)
print d

prims = factor(31313)
print prims[0],prims[1]
d = findsecret(prims[0],prims[1], 4913)
print d