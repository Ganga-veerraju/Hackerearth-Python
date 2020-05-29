t=int(input())
for i in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    p.remove(p[0])
    q=list(map(int,input().split()))
    q.remove(q[0])
    r=set(p+q)
    if len(r)==n:
        print("YES")
    else:
        print("NO")
