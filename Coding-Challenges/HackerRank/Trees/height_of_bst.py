# The height of a binary search tree is the number of edges between the tree's root and it's furthest leaf.
# return the height of a binary search tree as an integer
# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=trees&isFullScreen=true


# my solution:
def height(root):
    # if there's no further node to left or right return 0
    if (root == None):
        return -1
    # if there's a left node from current node go left
    left_depth = height(root.left)
    # if there's a right node from current node go right
    right_depth = height(root.right)
    # return the max of left and right to find longest height (# of edges)
    return max(left_depth, right_depth) + 1


# technical coaching solution:
def height(root):
    # we could check all of the different paths, and find which one has the largest length
    # recursion -> depth first search
    return heightRecursive(root, 0)


def heightRecursive(node, currentHeight):
    # check if left is None and right is None
    # we've hit the end of this route, so return the height
    if(node == None):
        return currentHeight - 1

    # to go left:
    # leftHeight = call our recursive function and pass in node.left and also the height
    leftHeight = heightRecursive(node.left, currentHeight + 1)
    # to go right
    # rightHeight = call our recursive function and pass in node.right and also the height
    rightHeight = heightRecursive(node.right, currentHeight + 1)
    # return the larger one
    # return max of left and right
    return max(leftHeight, rightHeight)
