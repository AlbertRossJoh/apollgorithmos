import random
from bst import Node, BST

bst = BST()
for _ in range(2000000):
    bst.put(random.randint(0, 4000000))

allkeys=bst.get_all_keys()
firstcut=(len(allkeys)*2)//4
secondcut=(len(allkeys)*3)//4
# print(firstcut, secondcut)
# centerKeys=allkeys[firstcut:secondcut]

mem={}
def getNodeLeafCounts(node: Node|None):
    global mem
    if node == None:
        return
    mem[node.key] = node.get_leaf_count()
    getNodeLeafCounts(node.left)
    getNodeLeafCounts(node.right)

getNodeLeafCounts(bst.root)

mem={k: v for k, v in mem.items() if v > 4000}
print(mem)
def getRandomKey() -> int:
    return random.choice(allkeys)

def other(node: Node, parent: Node) -> Node:
    if parent.get_left().key == node.key:
        return parent.get_right()
    else:
        return parent.get_left()

either, parent = bst.get(getRandomKey())
other = other(either, parent)
print(parent.get_leafs())
print(either.key, other.key, parent.key)