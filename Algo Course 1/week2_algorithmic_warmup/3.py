# Uses python3
#import sys

#def gcd_naive(a, b):
#    current_gcd = 1
#    for d in range(2, min(a, b) + 1):
#        if a % d == 0 and b % d == 0:
#            if d > current_gcd:
#                current_gcd = d
#    return current_gcd

def gcd_fast(a, b):
#    if a>b:
    if b==0: return a
    c=a%b
    return (gcd_fast(b,c))
#    else:
#        if a==0: return b
#        c=b%a
#        return (gcd_fast(b,c))
if __name__ == "__main__":
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    #print(gcd_naive(a, b))
    print(gcd_fast(a, b))
