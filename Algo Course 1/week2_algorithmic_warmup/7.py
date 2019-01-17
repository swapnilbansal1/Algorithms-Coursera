# Uses python3
def get_fibo(n,m):
    f=[0,1]
    g=[0,1]
    x=(m+2)%60
    y=(n+1)%60
    for i in range(2,x+1):
        i=(f[i-1]+f[i-2])%100
        f.append(i)
    for j in range(2,y+1):
        j=(g[j-1]+g[j-2])%100
        g.append(j)
    return (f[x]-g[y])%10

if __name__ == '__main__':
    n,m = map(int,input().split())
    print(get_fibo(n,m))
