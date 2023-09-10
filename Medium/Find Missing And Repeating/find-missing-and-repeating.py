#User function Template for python3

#User function Template for python3

class Solution:
        
    def findTwoElement(self,arr,n):
        hasharray=[]
        for i in range(n+1):
            hasharray.append(0)
        for i in arr:
            hasharray[i]+=1
        
        for i in range(len(hasharray)):
            if hasharray[i]==0:
                missing=i
            if hasharray[i]==2:
                repeated=i
        return repeated,missing



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends