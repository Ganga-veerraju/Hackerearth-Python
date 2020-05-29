x, y = map(int, input().split())
n=list(map(int,input().split()))
c=0
k=0
for i in range(len(n)):
    if n[i]<=y and k<2:
        c=c+1
    else:
        k=k+1
        
print(c)
