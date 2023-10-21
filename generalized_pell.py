from decimal import Decimal, getcontext

def sequenceBuilder(n, i, k):
    mem = [0] * n
    for j in range(i+1):
        mem[j] = 0
    for j in range(i+1, k+1):
        mem[j] = 1
    for j in range(k+1, n):
        mem[j] = 2 * mem[j-1] + mem[j-k-1]
    return mem

def sumBuilder(seq, window):
    sumMem = {}
    for i in range(window-1, len(seq)):
        windowSum = 0
        for j in range(i-window+1, i + 1):
            windowSum += seq[j]
        for j in range(i-window+1, i+1):
            if seq[j] > 2 and windowSum % seq[j] == 0:
                r = int(windowSum / seq[j])
                sumMem[r] = sumMem.get(r, 0) + 1
    for k in sumMem:
        if sumMem[k] > 100:
            print(window, k)
    
def oddWindowFinder(seq):
    for i in range(3, len(seq) // 2, 2):
        sumBuilder(seq, i)

for k in range(100):
    for i in range(k):
        print(i, k)
        pell = sequenceBuilder(1000, i, k)
        oddWindowFinder(pell)