#User function Template for python3
class Solution:
    def revStr (ob, S):
        # code here 
        reversedString=S[::-1]
        return reversedString

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        
        ob = Solution()
        print(ob.revStr(S))
# } Driver Code Ends