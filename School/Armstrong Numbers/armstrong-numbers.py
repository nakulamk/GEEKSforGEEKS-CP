#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        # code here
        i=0
        NtoS=str(n)
        ToT=(pow(int(NtoS[i]),3)+pow(int(NtoS[i+1]),3)+pow(int(NtoS[i+2]),3))
        if ToT == n:
            return "Yes"
        else:
            return "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends