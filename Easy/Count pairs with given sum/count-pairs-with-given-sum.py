#User function Template for python3

# class Solution:
#     def getPairsCount(self, arr, n, k):
#         # code here
#         arr.sort()
#         i=0
#         j=n-1
#         count=0
#         while i<=j:
#             if arr[i]+arr[j]<k:
#                 i+=1
#             elif arr[i]+arr[j]>k:
#                 j-=1
#             else:
#                 count+=1
#                 i+=1
#                 j-=1
        
#         return count
class Solution:
    def getPairsCount(self, arr, n, k):
        dic={}   
        count=0
        for i in range(n):
            if k-arr[i] in dic:
                count+=dic[k-arr[i]]  
            if arr[i] in dic:
                dic[arr[i]]+=1  
            else:
                dic[arr[i]]=1
        return count
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends