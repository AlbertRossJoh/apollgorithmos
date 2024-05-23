from typing import Optional, List

class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def get_right(self) -> 'Node':
        if self.right == None:
            self.right = Node(self.key+1)
        return self.right
    
    def get_left(self) -> 'Node':
        if self.left == None:
            self.left = Node(self.key-1)
        return self.left

class BST:
    def __init__(self):
        self.root: Optional[Node] = None

    def put(self, key: int) -> None:
        self.root = self._put(self.root, key)

    def _put(self, node: Optional[Node], key: int) -> Node:
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._put(node.left, key)
        elif key > node.key:
            node.right = self._put(node.right, key)
        return node

    def __contains__(self, key: int):
        node, _ = self.get(key)
        return node != None

    def get(self, key: int) -> tuple[Optional[Node], Node]:
        return self._get(self.root, None, key)

    def _get(self, node: Optional[Node], parent: Optional[Node], key: int) -> tuple[Optional[Node], Node]:
        if node is None:
            return None, parent
        if key < node.key:
            return self._get(node.left, node, key)
        elif key > node.key:
            return self._get(node.right, node, key)
        else:
            return node, parent

    def get_all_leafs(self) -> List[int]:
        if self.root is None:
            return []
        keys=[]
        self._leafs(self.root, keys)
        return keys

    def _leafs(self, node: Node, keys: List)-> None:
        if node is None:
            return
        if node.left is None and node.right is None:
            keys.append(node.key)
        self._leafs(node.left, keys)
        self._leafs(node.right, keys)
