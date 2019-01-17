# Uses python3
import sys
import math

def binary_search(a, x):
    left = 0
    right = len(a)-1
    key=x
    mid=(left+right)//2
   
    if a[right]<key:
        return -1
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        if mid==0: return -1
        b=a[:mid-1]
        return binary_search(b,x)
    else: #key > a[mid]:
        if mid==0: return -1
        b=a[mid+1:]
        return binary_search(b,x)
    #else:
       # return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
