#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        #code here.
        left=-1
        right=-1
        for i in range(0,n,+1):
            if key==a[i]:
                left=i
                break
        
        for i in range(n-1,-1,-1):
            if key == a[i]:
                right=i
                break
            
        return [left, right]

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends