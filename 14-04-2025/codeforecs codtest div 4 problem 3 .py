for i in range(int(input())):
    a=int(input())

    x=[None,]
    for i in range(a):
        if i==0:
            x=x+list(map(int,input().split()))
        else:
            x.append(list(map(int,input().split()))[-1])
    for i in range(1,(2*a)+1):
        if i not in x:
            x[0]=i
            print(*x)
    




