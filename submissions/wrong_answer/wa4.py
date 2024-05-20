# Derive amount of elements from depth
import random


amountgroundelms=int(input())
groundelms=set(input().split())
combinations=int(input())
revrecipies={}
inrecipe=set()
for _ in range(combinations):
    # fire water steam
    a, b, c = input().split()
    t=sorted([a, b])
    revrecipies[c] = tuple(t)
    inrecipe.add(b)
    inrecipe.add(a)

acc=[]
elm=input()
for _ in range(10000):
    ctr=0
    curr=elm
    while True:
        goleft=random.randint(0,1)==1
        left, right = revrecipies[curr]
        currinner=left if goleft else right
        if currinner in groundelms:
            break
        else:
            ctr+=1
            curr=currinner
    if ctr>0:
        acc.append(ctr)
# print(acc)
# print((sum(acc)/len(acc)))
print(int((2**(sum(acc)/len(acc)))*2))
