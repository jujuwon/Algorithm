# baekjoon 트리 순회 (실버1)
import sys

def input():
    return sys.stdin.readline().rstrip()

class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def preOrder(node): #root -> left -> right
    print(node.value, end="")
    if node.left != '.':
        preOrder(tree[node.left])
    if node.right != '.':
        preOrder(tree[node.right])

def inOrder(node):  #left -> root -> rigth
    if node.left != '.':
        inOrder(tree[node.left])
    print(node.value, end="")
    if node.right != '.':
        inOrder(tree[node.right])
    
def postOrder(node):    #left -> right -> root
    if node.left != '.':
        postOrder(tree[node.left])
    if node.right != '.':
        postOrder(tree[node.right])
    print(node.value, end="")

N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().split()
    tree[root] = Node(root, left, right)

preOrder(tree['A'])
print()
inOrder(tree['A'])
print()
postOrder(tree['A'])