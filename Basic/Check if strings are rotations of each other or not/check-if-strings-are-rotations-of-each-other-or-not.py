#User function Template for python3

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,str1,str2):
        #code here
        if len(str1) != len(str2):
            return False
        concatenated_str = str1 + str1
        
        if str2 in concatenated_str:
            return True
        else:
            return False
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s1=str(input())
        s2=str(input())
        if(Solution().areRotations(s1,s2)):
            print(1)
        else:
            print(0)
    
        
# } Driver Code Ends