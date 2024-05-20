amountgroundelms=int(input())
groundelms=set(input().split())
combinations=int(input())
revrecipies={}
for _ in range(combinations):
    # fire water steam
    a, b, c = input().split()
    revrecipies[c] = tuple(sorted([a, b]))

mem={}
for elm in groundelms:
    mem[elm] = 1

def sol(rec: dict[str, tuple[str, str]], curr: str):
    global mem
    if curr in mem:
        return mem[curr]
    else:
        a, b = rec[curr]
        mem[curr] = sol(rec, a) + sol(rec, b)
    return mem[curr]

elm=input()
print(sol(revrecipies, elm))
