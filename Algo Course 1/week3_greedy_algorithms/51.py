# Uses python3
import sys

def optimal_summands(n):
    temp= ()
    i=1
    y=n
    if n==2:
        temp=temp+(2,)
        return temp
    while(n>0):
        if n-i not in temp:
            n=n-i
            if n==0:
                temp=temp+(i,)
                break
            if n<0:
                n=i-1+temp[-1]
                temp=temp+(n,)
                temp=temp[:-2]+temp[-1:]
                break
            if n>0:temp=temp+(i,)
        i=i+1
    #print(temp)
    return temp

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
