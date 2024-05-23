from typing import Dict, Set, Tuple

def main() -> None:
    amount_ground_elems: int = int(input())
    ground_elems: Set[str] = set(input().split())
    combinations: int = int(input())

    rev_recipes: Dict[str, Tuple[str, str]] = {}
    for _ in range(combinations):
        a, b, c = input().split()
        rev_recipes[c] = tuple(sorted([a, b]))

    mem: Dict[str, int] = {elem: 1 for elem in ground_elems}

    def sol(rec: Dict[str, Tuple[str, str]], curr: str) -> int:
        if curr in mem:
            return mem[curr]
        a, b = rec[curr]
        mem[curr] = sol(rec, a) + sol(rec, b)
        return mem[curr]

    elm: str = input()
    print(sol(rev_recipes, elm) - 1)

if __name__ == "__main__":
    main()
