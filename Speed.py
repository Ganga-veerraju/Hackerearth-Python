t=int(input())
z=[]
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=1
    for i in range(len(l)-1):
        if l[i+1]<l[i]:
            c=c+1
        else:
            l[i+1]=l[i]
    z.append(c)
for i in z:
    print(i)
