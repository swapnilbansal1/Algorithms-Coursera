# Uses python3
#import sys

#def lcm_naive(a, b):
#    for l in range(1, a*b + 1):
#        if l % a == 0 and l % b == 0:
#            return l
#    return a*b

def lcm_fast(a, b):
    return a*b//gcd_fast(a, b)

def gcd_fast(a, b):
    if b==0: return a
    c=a%b
    return (gcd_fast(b,c))

if __name__ == '__main__':
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    #lcm=(a*b/gcd_fast(a, b))
    #print(lcm_naive(a, b))
    print(lcm_fast(a, b))
