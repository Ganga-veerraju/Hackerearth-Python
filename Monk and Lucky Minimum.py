t=int(input())
from collections import Counter
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    p=Counter(a)
    l=min(a)
    if p[l]%2==0:
        print("Unlucky")
    else:
        print("Lucky")
