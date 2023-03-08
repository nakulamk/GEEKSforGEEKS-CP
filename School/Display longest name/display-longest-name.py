#User function Template for python3

class Solution:
    def longest(self, names, n):
    	# code here
    	
    	big=0
    	for i in range(0,n,+1):
    	    if len(names[i])>big:
    	        big=len(names[i])
    	        indexOfBig=i
    	return (names[indexOfBig])
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	n=int(input())
    	names = []
    	for i in range(n):
    		names.append(input())
    	ob = Solution()
    	print(ob.longest(names, n))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends