# Uses python3
def get_fibonacci_huge_naive(n):
    f=[0,1]
    x=(n+2)%60
    for i in range(2,x+1):
        i=(f[i-1]+f[i-2])%100
        f.append(i)
    return (f[x]-1)%10

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_huge_naive(n))
