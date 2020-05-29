t=int(input())
for _ in range(t):
    n,p=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    r=max(b)+1
    s=[]
    for i in range(n):
    	if a[i]<r:
    		c=r-a[i]
    		s.append(c)
    #print(s)
    print(sum(p*s))
