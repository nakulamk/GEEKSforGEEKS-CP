#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        count=0
        arr.sort()
        for i in range(n-1):
            j=i+1
            k=n-1
            while(j<k):
                sumi=arr[i]+arr[j]+arr[k]
                if sumi==0:
                    count+=1
                    return count
                elif sumi<0:
                    j+=1
                else:
                    k-=1
        
        return count

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
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends