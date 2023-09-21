#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        
        # code here
        # odd=[]
        # even=[]
        # for i in range(n):
        #     if i%2==0:
        #         even.append(a[i])
        #     else:
        #         odd.append(a[i])
        
        # oddRes=sum(odd)
        # evenRes=sum(even)
        
        # maxi=max(oddRes,evenRes)
        
        # return maxi
        # if n==0:
        #     return 0
        # even=0
        # odd=0
        # for i in range(n):
        #     if i%2==0:
        #         even+=a[i]
        #     else:
        #         odd+=a[i]
        
        
        
        # maxi=max(odd,even)
        
        # return maxi
        
        if n==0 :
            return 0
        
        rob = a[0]
        skip = 0
        
        for i in range (1,n):
            currRob = skip + a[i]
            currSkip = max(rob,skip)
            
            rob =  currRob
            skip = currSkip
        
        return max(rob,skip)
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends