#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        #code here
        c=arr[0]
        p=arr[0]
        out=1
        if c==0:
            return -1
        for i in range(1,len(arr)):
            if i==n-1:
                return out
            p=max(p,i+arr[i])
            c=c-1
            if c==0:
                out+=1
                if i>=p:
                    return -1
                c=p-i
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends