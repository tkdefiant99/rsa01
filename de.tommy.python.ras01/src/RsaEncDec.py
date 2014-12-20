'''
Created on 16.12.2014

@author: Tommy
'''

cypher = [26024, 56, 24754, 23611, 2433, 4440, 24118, 7792, 17313, 3747, 27516, 22205, 10205, 24728, 22989, 964,
          6423, 18587, 10428, 14379, 17054, 23977, 26024, 20371, 26323, 2034, 23032, 13478, 1708, 24642, 25806,
          29218, 1006, 16919, 4064, 6888, 26788, 27516, 4878, 9224, 9197, 31269, 22827, 30498, 7028, 9616, 8802, 30888]

alphabet ={1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m',
           14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

triple = []

def encrypt (m, n, e):
    c = (m ** e) % n
    return c

def decrypt (c, n, d):
    m = (c ** d) % n
    return m

def gettriple(y):
    triple = []
    factor = 2
    while (y != 0):
        triple.append(y // (27 ** factor))
        y = y % (27 ** factor)
        factor = factor - 1
    return triple

for cmember in cypher:
    m = decrypt(cmember, 31313, 6497)
    #print "encrypted " + str(cmember) + " = decrypted " + str(m)
    triple = gettriple(m)
    for t in triple:
        print alphabet[t],

    
    


