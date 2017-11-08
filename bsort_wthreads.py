#!/usr/bin/python

import threading
import time
import random


# Define a function for filling the array
def fill(b, a):
    for i in range(a):
        b.append(random.randint(0, a * 8))
    return b


# Define a function for bubble sort arrays
def bsort(c):
    for i in range(len(c) - 1, 0, -1):
        for j in range(i - 1):
            if (c[j] > c[j + 1]):
                d = c[j]
                c[j] = c[j + 1]
                c[j + 1] = d
    return c


# Define a function for merging and sorting two arrays
def merge(a, b, c):
    i = 0
    j = 0
    while i < len(a) - 1 and j < len(b) - 1:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c


# Define a function for starting ans joining all threads in an array
def startjoin_all(thread_array):
    for t in thread_array:
        t.start()

    for t in thread_array:
        t.join()


n = 100000
p = 8
x = [[],[],[],[],[],[],[],[]]
threads = []
start = time.time()
for xi in x:
    threads.append(threading.Thread(target=fill, args=(xi, n / 8,)))

startjoin_all(threads)
threads = []
for xi in x:
    threads.append(threading.Thread(target=bsort, args=(xi,)))

startjoin_all(threads)
ym = [[],[],[],[]]
# Merging
threads = []
for i in range(0,len(x)-1,2):
    threads.append(threading.Thread(target=merge, args=(x[i], x[i+1], ym[i/2])))

startjoin_all(threads)
ymm=[[],[]]
threads = []
for i in range(0,len(ym)-1,2):
    threads.append(threading.Thread(target=merge, args=(ym[i], ym[i+1], ymm[i/2])))

startjoin_all(threads)
y=[]
merge(ymm[0],ymm[1],y)
end = time.time()
print(end - start)
print y