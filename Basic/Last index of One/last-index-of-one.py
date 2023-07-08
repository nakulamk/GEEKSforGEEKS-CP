#User function Template for python3

class Solution:
    def lastIndex(self, s):
        # code here
        arr=list(map(int,s))
        
        for i in range(len(arr)-1,0-1,-1):
            if arr[i]== 1:
                return i
            
        return -1
                
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	s = input()
    	ob = Solution()
    	print(ob.lastIndex(s))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends