# Uses python3
#import sys

def get_fibonacci_last_digit_naive(n):
    f=[0,1]
    for i in range(2,n+1):
        i=(f[i-1]+f[i-2])%10
        f.append(i)
    return f[n]

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
