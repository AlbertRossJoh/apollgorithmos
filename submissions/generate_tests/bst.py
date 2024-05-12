from typing import Optional, List, Dict

class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
    
    def get_subtree_depth(self) -> int:
        return _get_subtree_depth(self)
    def _get_subtree_depth(self, max_depth: int) -> int:
        if self.left == None and self.right == None:
            return max_depth

        max_depth += 1
        if self.left != None:
            tmp = self.left._get_subtree_depth(max_depth)
            if tmp > max_depth:
                max_depth = tmp
        if self.right != None:
            tmp = self.right._get_subtree_depth(max_depth)
            if tmp > max_depth:
                max_depth = tmp
        return max_depth


    def get_right(self) -> 'Node':
        if self.right == None:
            self.right = Node(self.key+1)
        return self.right
    
    def get_left(self) -> 'Node':
        if self.left == None:
            self.left = Node(self.key-1)
        return self.left
    
    def get_leaf_count(self) -> int:
        return self._get_leaf_count()
        
    def _get_leaf_count(self ) -> int:
        if self.left is None and self.right is None:
            return 1
        ctr = 0
        if self.left is not None:
            ctr += self.left._get_leaf_count()
        if self.right is not None:
            ctr += self.right._get_leaf_count()
        return ctr

    def get_leafs(self) -> List['Node']:
        leafs: List['Node'] = []
        self._get_leafs(leafs)
        return leafs

    def _get_leafs(self, leafs: List['Node']) -> None:
        if self.left is None and self.right is None:
            leafs.append(self)
        if self.left is not None:
            self.left._get_leafs(leafs)
        if self.right is not None:
            self.right._get_leafs(leafs)

def _get_subtree_depth(node: Node|None) -> int:
    if node == None:
        return 0
    left = _get_subtree_depth(node.left)
    right = _get_subtree_depth(node.right)
    return max(left, right) + 1

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

    def delete(self, key: int) -> None:
        if self.root is None:
            raise ValueError("the tree is empty")
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[Node], key: int) -> Optional[Node]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right

            tmp = node
            node = self._min(tmp.right)
            node.right = self._delete_min(tmp.right)
            node.left = tmp.left
        return node

    def _min(self, node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node

    def delete_min(self) -> None:
        if self.root is None:
            raise ValueError("the tree is empty")
        self.root = self._delete_min(self.root)

    def _delete_min(self, node: Node) -> Optional[Node]:
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        return node

    def get_all_keys(self) -> List[int]:
        if self.root is None:
            return []
        keys: List[int] = []
        self._keys(self.root, keys)
        return keys

    def _keys(self, node: Node, keys: List[int]) -> None:
        if node is None:
            return
        self._keys(node.left, keys)
        keys.append(node.key)
        self._keys(node.right, keys)

    def is_empty(self) -> bool:
        return self.root is None

    def min(self) -> int:
        if self.root is None:
            raise ValueError("the tree is empty")
        return self._min(self.root).key

    def _min(self, node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node

    def max(self) -> int:
        if self.root is None:
            raise ValueError("the tree is empty")
        return self._max(self.root).key

    def _max(self, node: Node) -> Node:
        while node.right is not None:
            node = node.right
        return node


