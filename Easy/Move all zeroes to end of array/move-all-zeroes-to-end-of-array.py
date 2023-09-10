#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr, n):
        # code here
        #n = len(A)
        
        # approach 1
        j = 0
        for i in range(n):
            if arr[i] != 0:
                arr[j], arr[i] = arr[i], arr[j]  # Partitioning the array
                j += 1
        
        
        # approach 2
        a = []
        zcount = 0
        
        for i in arr:
            if i!=0:
                a.append(i)
            else:
                zcount+=1
        while(zcount!=0):
            a.append(0)
            zcount-=1
        for i in range(len(a)):
            arr[i]=a[i]
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends