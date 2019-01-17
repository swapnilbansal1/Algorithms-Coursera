#! /usr/bin/python3
# Uses python3
import math


def optimal_summands(n):
    y = int(((-1+math.sqrt(1+8*n))//2)-1)
    #print(y)
    sum1=int((y*(y+1))/2)
    z=n-sum1
    print(y+1)
    for i in range(1,y+1):
        print(i,end =' ')
    print(z)
    #return True

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    optimal_summands(n)
    #print(len(summands))
    #for x in summands:
    #    print(x, end=' ')
