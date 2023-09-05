#User function Template for python3

class Solution:
    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        stack = []
        # Define a dictionary to store the mapping of opening and closing brackets
        bracket_mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the expression
        for char in x:
            # If the character is an opening bracket, push it onto the stack
            if char in '({[':
                stack.append(char)
            # If the character is a closing bracket
            elif char in ')}]':
                # Check if the stack is empty, or if the top of the stack does not match the current closing bracket
                if not stack or stack[-1] != bracket_mapping[char]:
                    return False
                # If they match, pop the top element from the stack
                stack.pop()
        
        # After iterating through the expression, if the stack is empty, it means all brackets are balanced
        return not stack


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha


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
        #n = int(input())
        #n,k = map(int,imput().strip().split())
        #a = list(map(int,input().strip().split()))
        s = str(input())
        obj = Solution()
        if obj.ispar(s):
            print("balanced")
        else:
            print("not balanced")
# } Driver Code Ends