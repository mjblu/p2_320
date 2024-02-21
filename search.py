class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.values = []
        self.left = None
        self.right = None

    # def lookup(self, key):
    #     if self.key == key:
    #         return self.values
    #     elif key < self.key and self.left:
    #         return self.left.lookup(key)
    #     elif key > self.key and self.right:
    #         return self.right.lookup(key)
    #     else:
    #         return []

#     def __lt__(self, other):
#         # Handle comparison between different types (int and str)
#         self_key = str(self.key) if isinstance(self.key, (int, float)) else self.key
#         other_key = str(other.key) if isinstance(other.key, (int, float)) else other.key

#         return self_key < other_key
    def compare_keys(self, key, other_key):
        # Handle comparison between different types (int and str)
        key_str = str(key) if isinstance(key, (int, float)) else key
        other_key_str = str(other_key) if isinstance(other_key, (int, float)) else other_key

        return key_str < other_key_str

    # def lookup(self, key):
    #     if self.key == key:
    #         return self.values
    #     elif self.compare_keys(key, self.key) and self.left:
    #         return self.left.lookup(key)
    #     elif not self.compare_keys(key, self.key) and self.right:
    #         return self.right.lookup(key)
    #     else:
    #         return []
        
        
    def lookup(self, key):
        if self.key == key:
            return self.values
        elif key < self.key and self.left != None:
            return self.left.lookup(key)
        elif key>self.key and self.right != None:
            return self.right.lookup(key)
        else:
            return []
        
        
        
    
    def __len__(self):
        size = len(self.values)
        if self.left != None:
            size += len(self.left)
        if self.right != None:
            size += len(self.right)
        return size



        
class BST:
    def __init__(self):
        self.root = None

    def add(self, key, val):
        if self.root is None:
            self.root = Node(key)
            curr = self.root
            # self.root.values.append(val)
        # else:
        curr = self.root
        while True:
            if key < curr.key:
                if curr.left is None:
                    curr.left = Node(key)
                    # print("left")
                    # curr.left.values.append(val)
                curr = curr.left
            elif key > curr.key:
                if curr.right is None:
                    curr.right = Node(key)
                    # print("right")
                    # curr.right.values.append(val)
                curr = curr.right
            else:
                # Key already exists in the tree
                # curr.values.append(val)
                break
        curr.values.append(val)

    def __dump(self, node):
        if node is None:
            return
        self.__dump(node.left)
        print(node.key, ":", node.values)
        self.__dump(node.right)

    def dump(self):
        self.__dump(self.root)
    def count_missing_interest_rates(self):
        return self._count_missing_interest_rates_recursive(self.root)

    def _count_missing_interest_rates_recursive(self, node):
        if node is None:
            return 0

        count = 0
        if node.key == -1:
            count += 1

        count += self._count_missing_interest_rates_recursive(node.left)
        count += self._count_missing_interest_rates_recursive(node.right)

        return count
    def count_key(self, key):
        count = 0
        stack = []  # Use a stack to perform an iterative traversal
        node = self.root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.key == key:
                count += 1
            node = node.right
        return count

    def count_leaf_nodes(self):
        return self._count_leaf_nodes_recursive(self.root)

    def _count_leaf_nodes_recursive(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            # This is a leaf node
            return 1
        left_leaves = self._count_leaf_nodes_recursive(node.left) if node.left else 0
        right_leaves = self._count_leaf_nodes_recursive(node.right) if node.right else 0
        return left_leaves + right_leaves

    
    def find_kth_largest(self, k):
        count = [0]  # To keep track of the count
        result = self._find_kth_largest_recursive(self.root, k, count)
        if result is not None:
            return result[0]
        else:
            return None

    def _find_kth_largest_recursive(self, node, k, count):
        if node is None:
            return None

        # Recurse on the right subtree
        result = self._find_kth_largest_recursive(node.right, k, count)
        if result is not None:
            return result

        # Update count
        count[0] += 1

        # Check if we've found the kth largest node
        if count[0] == k:
            return (node.key, node.values)

        # Recurse on the left subtree
        return self._find_kth_largest_recursive(node.left, k, count)
    
    def __getitem__(self, key):
        return self.root.lookup(key)
