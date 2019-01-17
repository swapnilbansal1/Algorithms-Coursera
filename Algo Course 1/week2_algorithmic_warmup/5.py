# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    f=[0,1]
    x=n%pisano(m)
    for i in range(2,x+1):
        i=(f[i-1]+f[i-2])%m
        f.append(i)
    return f[x]

def pisano(m):
    a,b=0,1
    for i in range(0,m*m):
        c = (a + b) % m
        a,b = b,c
        if (a == 0) and (b == 1):
            return i + 1

if __name__ == '__main__':
    #input = sys.stdin.read();
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))
