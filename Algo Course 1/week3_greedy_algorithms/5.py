# Uses python3
import sys

def optimal_summands(n):
    temp= []
    i=0
    while(n>0):
        i=i+1
        temp.append(i)
        if n-i not in temp:
            n=n-i
            #temp.append(i)
        else:
            #temp.remove(temp[-1])
            del temp[-1]
            temp.append(n)
            break
    return temp

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
