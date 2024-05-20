# Counting all elements in recipies
amountgroundelms=int(input())
groundelms=set(input().split())
combinations=int(input())
revrecipies={}
ctr=0
for _ in range(combinations):
    # fire water steam
    a, b, c = input().split()
    t=sorted([a, b])
    revrecipies[c] = tuple(t)
    ctr+=3

print(ctr)

