import sys

T = int(sys.stdin.readline().strip())

def postOrder(preOrder, inOrder):

    if len(preOrder) == 0:
        return

    root = preOrder[0]

    for i in range(len(inOrder)):
        if root == inOrder[i]:
            #print(preOrder[1:i+1], inOrder[:i])
            #print(preOrder[i+1:], inOrder[i+1:])
            postOrder(preOrder[1:i+1], inOrder[:i])
            postOrder(preOrder[i+1:], inOrder[i+1:])

    print(root, end = " ")

for t in range(T):
    N = int(sys.stdin.readline().strip())
    preorder = list(map(int, sys.stdin.readline().strip().split()))
    inorder = list(map(int, sys.stdin.readline().strip().split()))

    postOrder(preorder, inorder)
    print()