from collections import defaultdict
import json
import random
import sys
import time
from bst import Node, BST
from helpers import *

start_time=time.time()
timer_time=start_time

def log_time():
    global timer_time
    curr=time.time()
    st=f"{(curr-timer_time):.3f} s"
    timer_time=curr
    return st

bst = BST()
AMOUNT_IN_TREE=2000000
sys.setrecursionlimit(10**9)

insert_range(bst,0,AMOUNT_IN_TREE)

print("----TREE GENERATED----: "+log_time())

base_elements=set()
recipies={}
def get_recipies(node: Node):
    global recipies, base_elements
    left = node.left
    right = node.right
    if left != None and right != None: 
        left_key = left.key
        right_key = right.key
        key=(left_key,right_key)
        if key in recipies:
            return
        recipies[key]=node.key
        get_recipies(left)
        get_recipies(right)
    else:
        if node.left is None and node.right is None:
            base_elements.add(node.key)
        elif node.left is None: 
            node.right = None
        else: 
            node.left = None
        base_elements.add(node.key)


# random_range=random.randint(2,7)
# random_node=getRandomNode(random_range, bst.root)
random_node=bst.root

random_subtree_acc=[]
for _ in range(3):
    deep_random_node=getRandomNode(4, random_node)
    deep_random_node, deep_random_parent=bst.get(deep_random_node.key)
    if deep_random_parent.left.key == deep_random_node.key:
        deep_random_parent.left = None
    else:
        deep_random_parent.right = None
    random_subtree_acc.append(deep_random_node)

all_leaf_keys=bst.get_all_leafs()
for _ in range(len(all_leaf_keys)//20):
    rand_node = random.choice(random_subtree_acc)
    rand_leaf = random.choice(all_leaf_keys)
    all_leaf_keys.remove(rand_leaf)
    rand_leaf, rand_leaf_parent = bst.get(rand_leaf)
    if isRight(rand_leaf, rand_leaf_parent):
        rand_leaf_parent.right = rand_node
    else:
        rand_leaf_parent.left = rand_node

print("----SUBTREES SET----: "+log_time())

get_recipies(random_node)
print("----RECIPIES CREATED----: "+log_time())
print(len(base_elements))
print(len(recipies))
count=defaultdict(lambda:0)
for k,v in recipies.items():
    a,b=k
    count[a]+=1
    count[b]+=1
    count[v]+=1

print("----COUNT DONE----: "+log_time())

leftovers=[k for k,c in count.items() if c == 1]
for leftover in leftovers:
    base_elements.add(leftover)

print("----LEFTOVERS ADDED----: "+log_time())

# with open("recipies.json", "w") as outfile: 
with open("03.in", "w") as outfile: 
    # json.dump(remap(recipies), outfile)
    b_e = list(map(str,base_elements))
    basestr=" ".join(b_e)+"\n"
    combinations=f"{len(recipies)}\n"

    remapped=remap(recipies)

    outfile.write(str(len(b_e)))
    outfile.write(basestr)
    outfile.write(combinations)
    for k, v in remapped.items():
        outfile.write(f"{k} {v}\n")
    random_node=getRandomNode(random.randint(1,3), random_node)
    outfile.write(f"{random_node.key}\n")


print(f"----FILE CREATED----: {(time.time()-start_time):.3f} s")
