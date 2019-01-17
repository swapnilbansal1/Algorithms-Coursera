# Uses python3

def calc_fib(n):
    f=[0,1]
    for i in range(2,n+1):
        i=(f[i-1]+f[i-2])
        f.append(i)
    return f[n]

if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
