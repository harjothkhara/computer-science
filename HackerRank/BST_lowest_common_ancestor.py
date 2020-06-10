# You are given pointer to the root of the binary search tree and two values  and . You need to return the lowest common ancestor (LCA) of  and  in the binary search tree.

# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?isFullScreen=true


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    # your code here.
    node = root
    while(node.info!= None):
        # if v1/v2 is <= to current node and the other is >= current node,
        # then we know our current node is the lca 
        if v1 <= node.info and v2 >= node.info or v1 >= node.info and v2 <= node.info: # split
            return node     
        # if both v1 and v2 < current node, then we step to the left
        if v1 < node.info and v2 < node.info:
            node = node.left
        # if both v1 and v2 and > current node, then we step to the right
        if v1 > node.info and v2 > node.info:
            node = node.right
        # if we find v1 or v2 on same side, then we're at the lca <--first if statement covers it!
        # if node.info == v1 or node.info == v2:
        #     return node