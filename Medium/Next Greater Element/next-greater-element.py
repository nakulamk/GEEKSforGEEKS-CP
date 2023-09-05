#User function Template for python3


# class Solution:
#     def nextLargerElement(self,arr,n):
#         #code here
#         # res=[-1]*n
#         st=[]
        
#         # for i in range(n):
#         #     while st and arr[i]
                
#         #     st.append(arr[i])
        
#         # for i in range(n-1):
            
#         #     for j in range(i+1,n):
#         #         if arr[j]>arr[i]:
#         #             st.append(arr[j])
#         #             break
            
#         #     st.append(-1)
            
#         # return st
        

#User function Template for python3


#User function Template for python3

class Solution:
    def nextLargerElement(self, arr, n):
        # Initialize an empty stack to store indices
        stack = []
        # Create an array to store the result, initialized with -1
        result = [-1] * n
        
        # Iterate through the input array
        for i in range(n):
            # While the stack is not empty and the current element is greater than the element at the index stored in the stack
            while stack and arr[i] > arr[stack[-1]]:
                # Pop the index from the stack and update the result at that index with the current element
                result[stack.pop()] = arr[i]
            # Push the current index onto the stack
            stack.append(i)
        
        return result
        
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

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends