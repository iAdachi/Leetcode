# Definition for create a binary tree
def add_node(currentNode, val):
    if currentNode is None: return TreeNode(val)
    else: return direction(currentNode, val)

def direction(currentNode, val):
    if currentNode.val > val: currentNode.left = add_node(currentNode.left, val)
    elif currentNode.val < val: currentNode.right = add_node(currentNode.right, val)
    return currentNode

def createTree(elements):
    root = TreeNode(elements[0])
    currentNode = root
    for i in elements[1:]:
        direction(currentNode, i)
    return root

# Print binary tree
def inOrder(root):
    if root.left is not None: inOrder(root.left)
    print(root.val)
    if root.right is not None: inOrder(root.right)

def preOrder(root):
    print(root.val)
    if root.left is not None: preOrder(root.left)
    if root.right is not None: preOrder(root.right)

# Copy binary tree
def copyTree(root, inverseTree):
    if root is None: return inverseTree
    inverseTree.val = root.val
    if root.left is not None: 
        inverseTree.left = TreeNode()
        inverseTree.left = copyTree(root.left, inverseTree.left)
    if root.right is not None: 
        inverseTree.right = TreeNode()
        inverseTree.right = copyTree(root.right, inverseTree.right)
    return inverseTree

# Implementation of solution (preOrder logic)
def invertTree(root, inverseTree):
    if root is None: return root
    inverseTree.val = root.val
    if root.left is not None: 
        inverseTree.right = TreeNode()
        inverseTree.right = invertTree(root.left, inverseTree.right)
    if root.right is not None: 
        inverseTree.left = TreeNode()
        inverseTree.left = invertTree(root.right, inverseTree.left)
    return inverseTree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        inverseTree = TreeNode()
        return invertTree(root, inverseTree)
    
# Use example
root = createTree([4,2,7,1,3,6,9])
current = root
newTree = TreeNode()
sol = invertTree(current, newTree)
