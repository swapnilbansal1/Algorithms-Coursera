# Uses python3
#import sys

#def get_fibonacci_huge_naive(n, m):
#    f=[0,1]
#    x=n%pisano(m)
#    for i in range(2,x+1):
#        i=(f[i-1]+f[i-2])%m
#        f.append(i)
#    return f[x]

def summ(n):
    f=[0,1]
    total=1
    for i in range(2,n+1):
        a=(f[i-1]+f[i-2])%10
        f.append(a)
        total=(total+a)%10
        #print(f)
    return total
    #while n>=0:
    ##    #print(a)
    #    sum=(sum+a)%10
    #    a,b = b,c
    #    n=n-1
    #return sum

if __name__ == '__main__':
    #input = sys.stdin.read();
    n = int(input())
    print(summ(n))
