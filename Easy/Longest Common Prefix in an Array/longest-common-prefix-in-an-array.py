#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        size=len(arr)
        if size==0:
            return -1
        if size==1:
            return arr[0]
        
        arr.sort()
        
        mini=min(len(arr[0]),len(arr[size-1]))
        
        i=0
        while i<mini and arr[0][i]==arr[size-1][i]:
            i+=1
        
        if i==0:
            return -1
        else:
            ans=arr[0][0:i]
            return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends