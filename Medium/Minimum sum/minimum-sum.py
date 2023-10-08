#User function Template for python3

class Solution:
    def solve(self, arr, n):
        # code here
        if len(arr)==1:
            return arr[0]
        arr.sort()
        num1 =''
        num2 =''
        
        for i in range(0,n,2):
            num1+=str(arr[i])
            
        for i in range(1,n,2):
            num2+=str(arr[i])
            
        return int(num1)+int(num2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends