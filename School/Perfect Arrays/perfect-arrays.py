#User function Template for python3

class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        arrOrg=[]
        for i in range(0,n):
            arrOrg.append(arr[i])
        left=0
        right=len(arr)-1
        while(left<right):
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
        
        i=0
         
        while i!=n:
            if arrOrg[i]==arr[i]:
                i+=1
                
            else:
                return False
        return True
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    if(ob.IsPerfect(arr,n)):
        print("PERFECT")
    else:
        print("NOT PERFECT")
    
# } Driver Code Ends