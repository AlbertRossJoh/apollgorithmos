groundelms=set(input().split())
combinations=int(input())
revrecipies={}
for _ in range(combinations):
    # fire water steam
    a, b, c = input().split()
    revrecipies[c] = tuple(sorted([a, b]))
def sol(rec: dict[str, tuple[str, str]], curr: str):
    if curr in groundelms:
        return 1
    else:
        a, b = rec[curr]
        return sol(rec, a) + sol(rec, b)

elm=input()
print(sol(revrecipies, elm))

