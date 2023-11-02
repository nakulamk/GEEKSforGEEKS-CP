class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def bottomView(self,root):
        
        # code here
        ans=[]
        if root is None:
            return ans
        mpp={}
        q=deque()
        q.append((root,0))
        
        while q:
            node,line=q.popleft()
            
            mpp[line]=node.data
            
            if node.left:
                q.append((node.left,line-1))
            if node.right:
                q.append((node.right,line+1))
        
        
        for line in sorted(mpp):
            ans.append(mpp[line])
        
        return ans
