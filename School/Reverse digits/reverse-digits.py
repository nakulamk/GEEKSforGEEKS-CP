#User function Template for python3

class Solution:
	def reverse_digit(self, n):
	   # int is converted to string
	    strr=str(n)
	   # the strr is reversed using the [::-1]
        arr=strr[::-1]
        # then the reversed string is converd to int and then multiplied by 1 
        res=int(arr)*1;
        return res;
	

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.reverse_digit(n)
		print(ans)
# } Driver Code Ends