#User function Template for python3
from functools import cmp_to_key
class Solution:

# 	def printLargest(self,arr):
	    # code here
	   # for i,n in enumerate(arr):
    #         arr[i] = str(n)
    #     def compare(n1,n2):
    #         if n1+n2>n2+n1:
    #             return -1
    #         else:
    #             return 1
        
    #     arr=sorted(arr,key=cmp_to_key(compare))
    #     return str(int("".join(arr)))
    
	# def printLargest(self,arr):
 #        return "".join(sorted(arr,reverse=True,key=lambda _:_*18))   
	def printLargest(self,arr):
        for i,n in enumerate(arr):
            arr[i]=str(n)
        if len(arr)<2:
            return "".join(arr)
        def compare(x,y):
            return int(arr[x]+arr[y])> int(arr[y]+arr[x])
        
        for i in range(len(arr)-1):
            j=i+1
            while i<len(arr) and j<len(arr):
                if compare(i,j):
                    pass
                else:
                    arr[j],arr[i]=arr[i],arr[j]
                    # swaping 
                j+=1
        return str(int("".join(arr)))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends
