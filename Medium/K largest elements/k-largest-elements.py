#User function Template for python3

class Solution:

    def kLargest(self,arr, n, k):
        # code here
        # code here
        # ans = []
        arr.sort()
        arr.reverse()
        # for x in arr[-1:-1:-1]:
        #     ans.append(x)
        # print(ans)
        return arr[0:k]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n=li[0]
    k=li[1]
    li = [int(x) for x in input().strip().split()]
    ob=Solution()
    k_largest_list = ob.kLargest(li,n,k)
    
    for element in k_largest_list:
        print(element, end = ' ')
    print('')
# } Driver Code Ends