#User function Template for python3

class Solution:

	def print2largest(self,arr, n):
		# code here
		
		
		list1=list(arr)
		
		max1=max(list1)
		list2=list(set(list1))
		if len(list2) == 1:
		    return -1
		else:
		    list2.remove(max1)
		    max2=max(list2)
		    return max2
		
		

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends