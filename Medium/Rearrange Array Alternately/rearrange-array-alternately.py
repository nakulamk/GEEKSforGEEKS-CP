class Solution:
    # Function to rearrange the array elements alternately.
    def rearrange(self, arr, n):
        l = 0
        r = n - 1
        ls = []
        for i in range(n):
            ls.append(arr[r])
            ls.append(arr[l])
            l += 1
            r -= 1
        for i in range(n):
            arr[i] = ls[i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends