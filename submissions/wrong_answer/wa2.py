# Counting all ground elements
amountgroundelms=int(input())
groundelms=set(input().split())
combinations=int(input())
revrecipies={}
for _ in range(combinations):
    # fire water steam
    a, b, c = input().split()
    t=sorted([a, b])
    revrecipies[c] = tuple(t)

print(amountgroundelms)
