import random
from bst import Node, BST
def insert_range(bst: BST, left: int, right: int):
    if left > right:
        return
    mid = (left+right)//2
    bst.put(mid)
    insert_range(bst,left, mid-1)
    insert_range(bst,mid+1,right)


def getRandomNode(lvl: int, node: Node) -> Node:
    nxt = node.left if random.randint(0,1) == 0 else node.right
    if nxt == None or lvl == 0:
        return node
    return getRandomNode(lvl-1, nxt)

def other(node: Node, parent: Node) -> Node:
    if parent.get_left().key == node.key:
        return parent.get_right()
    else:
        return parent.get_left()

def isRight(node: Node, parent: Node) -> Node:
    if parent.left is None:
        return True
    if parent.right is None:
        return False
    return parent.right.key == node.key



def remap(d: dict):
    return {f"{k[0]} {k[1]}":v for k, v in d.items()}



