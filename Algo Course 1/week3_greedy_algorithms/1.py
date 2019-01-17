# Uses python3
import sys

def get_change(n):
    y=n//10
    n=n%10
    x=n//5
    n=n%5
    z=n
    m=x+y+z
    return m

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
