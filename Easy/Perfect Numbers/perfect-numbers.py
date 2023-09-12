#User function Template for python3

# class Solution:
#     def isPerfectNumber(self, N):
#         # code here 
#         factor=[]
        
#         for i in range(1,N+1):
#             if N%i == 0:
#                 factor.append(i)
            
        
#         sums=sum(factor)
        
#         perfect=sums-N
        
#         if perfect==N:
#             return 1
#         else:
#             return 0

#User function Template for python3

import math

class Solution:
    def isPerfectNumber(self, N):
        T = int(math.sqrt(N))
        sum = 0
        for i in range(2, T + 1):
            if N % i == 0:
                sum += i
                if (N // i) != i:
                    sum += N // i
        return 1 if N > 1 and sum + 1 == N else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends