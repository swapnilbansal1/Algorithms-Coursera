# Uses python3
import sys

def optimal_summands(n):
    temp= []
    i=1
    k=n
    while(k>0):
        if k<=2*i :
            temp.append(k)
            break
        else :
            temp.append(i)
            k=k-i
        i=i+1
    return temp


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
