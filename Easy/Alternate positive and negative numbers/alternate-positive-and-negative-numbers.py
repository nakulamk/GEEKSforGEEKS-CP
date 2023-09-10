#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        posArr=[]
        negArr=[]
        for i in range(n):
            if arr[i]>=0:
                posArr.append(arr[i])
            else:
                negArr.append(arr[i])
        
        i=0
        j=0
        k=0
        while i < len(posArr) and j < len(negArr):
            arr[k] = posArr[i]
            i += 1
            k += 1
            arr[k] = negArr[j]
            j += 1
            k += 1
            
        while i<len(posArr):
            arr[k]=posArr[i]
            i+=1
            k+=1
        
        while j<len(negArr):
            arr[k]=negArr[j]
            j+=1
            k+=1
        
        
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends