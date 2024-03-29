#User function Template for python3



'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
# class Solution:
#     #Function to return list containing elements of right view of binary tree.
#     def rightView(self,root):
        
#         # code here
#         ds=[]
#         level=0
#         def fun(root,level):
#             if root is None:
#                 return
#             dsSize=len(ds)
#             if(level==dsSize):
#                 ds.append(node.val)
            
#             fun(node.right,level+1)
#             fun(node.left,level+1)
        
#         return ds
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        
        # code here
        if not root:
            return []
        q=[root]
        rightView=[]
        while q:
            levelSize=len(q)
            for i in range(levelSize):
                current=q.pop(0)
                if i==levelSize-1:
                    rightView.append(current.data)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return rightView


#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
import queue
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

    
# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        result = Solution().rightView(root)
        for value in result:
            print(value, end = " ")
        print()
        
        

# } Driver Code Ends