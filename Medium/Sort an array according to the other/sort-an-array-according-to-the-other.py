#User function Template for python3

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort(self,A,n,B,m):
        freq={}
        
        for i in range(n):
            if A[i] not in freq:
                freq[A[i]]=1
            else:
                freq[A[i]]+=1
        
        k=0
        
        for i in range(m):
            if B[i] in freq:
                for j in range(freq[B[i]]):
                    A[k]=B[i]
                    k+=1
                del freq[B[i]]
                
        myKeys=list(freq.keys())
        myKeys.sort()
        
        for key in myKeys:
            for j in range(freq[key]):
                A[k]=key
                k+=1
        
        return A
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends