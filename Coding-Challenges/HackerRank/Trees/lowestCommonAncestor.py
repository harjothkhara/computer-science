# Given pointer to the root of a binary search tree and two values (v1,v2).
# return the lowest common ancestor of v1 and v2 in the the binary search tree
# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=trees&isFullScreen=true
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''


# recursive solution
def lca(root, v1, v2):
    # check if both nodes are on the left
    if (v1 < root.info and v2 < root.info):
        # recurse to the left side
        return lca(root.left, v1, v2)
    # check if both nodes are on the right
    if (v1 > root.info and v2 > root.info):
        # recurse the right side
        return lca(root.right, v1, v2)

# if neither nodes are on one side then return root
# this is where the nodes split, to get a lca,
# covers the edge case where v1 is also the ancestor node
    return root


    # iterative solution
def lca(root, v1, v2):
    # set out currunt node
    current = root

    # while current != null
    while (current != None):
        # base case ->
        # one value is on one side, the other is on the other side OR its equal
        # to it(lca is also the ancestor), we've found the lca
        if (v1 <= current.info and v2 >= current.info
                or v2 <= current.info and v1 >= current.info):
            return current

        # how do we know if we want to go left?
        # if both values are less than our node, then move left
        if (v1 < current.info and v2 < current.info):
            current = current.left

        # how do we know if we want to go right?
        # both values are greater than our node
        if (v1 > current.info and v2 > current.info):
            current = current.right
