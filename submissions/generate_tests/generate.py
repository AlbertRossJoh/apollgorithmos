import json
import random
import sys
from bst import Node, BST

bst = BST()
AMOUNT_IN_TREE=200000

sys.setrecursionlimit(10**9)

def insert_range(left: int, right: int):
    if left > right:
        return
    mid = (left+right)//2
    bst.put(mid)
    insert_range(left, mid-1)
    insert_range(mid+1,right)

insert_range(0,AMOUNT_IN_TREE)
# allkeys=bst.get_all_keys()
# firstcut=(len(allkeys)//2)
# secondcut=(len(allkeys)-1)
# # print(firstcut, secondcut)
# centerKeys=allkeys[firstcut:secondcut]

# mem={}
# def getNodeLeafCounts(node: Node|None):
#     global mem
#     if node == None:
#         return
#     mem[node.key] = node.get_leaf_count()
#     getNodeLeafCounts(node.left)
#     getNodeLeafCounts(node.right)

# getNodeLeafCounts(bst.root)

# mem={k: v for k, v in mem.items() if v > 100000}
# print(mem)
def getRandomKey(lvl: int, node: Node) -> Node:
    nxt = node.left if random.randint(0,1) == 0 else node.right
    if nxt == None or lvl == 0:
        return node
    return getRandomKey(lvl-1, nxt)

def other(node: Node, parent: Node) -> Node:
    if parent.get_left().key == node.key:
        return parent.get_right()
    else:
        return parent.get_left()

base_elements=set()
recipies={}
def get_recipies(node: Node):
    global recipies, base_elements
    left = node.left
    right = node.right
    if left != None and right != None: 
        left_key = left.key
        right_key = right.key
        key=left_key << 32 | right_key
        key=(left_key,right_key)
        recipies[key]=node.key
        get_recipies(left)
        get_recipies(right)
    else:
        base_elements.add(node.key)



def remap(d: dict):
    return {f"{k[0]} {k[1]}":v for k, v in d.items()}

random_range=random.randint(2,7)
random_node=getRandomKey(random_range, bst.root)
# print(random_node.get_leaf_count())
# print(random_node.key)
# print(random_node.get_subtree_depth())
# print(bst.root.get_subtree_depth())
get_recipies(random_node)
print(len(base_elements))
print(len(recipies))
insert_range(0,AMOUNT_IN_TREE)
# with open("recipies.json", "w") as outfile: 
with open("01.in", "w") as outfile: 
    # json.dump(remap(recipies), outfile)
    basestr=" ".join(list(map(str,base_elements)))+"\n"
    combinations=f"{len(recipies)}\n"

    remapped=remap(recipies)

    outfile.write(basestr)
    outfile.write(combinations)
    for k, v in remapped.items():
        outfile.write(f"{k} {v}\n")
    random_node=getRandomKey(random.randint(1,3), random_node)
    outfile.write(f"{random_node.key}\n")


