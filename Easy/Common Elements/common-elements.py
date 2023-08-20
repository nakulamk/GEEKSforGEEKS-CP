#User function Template for python3

class Solution:
    def common_element(self,v1,v2):
        #code here
        diction={}
        a=[]
        for i in v1:
            if i in diction:
                diction[i]+=1
            else:
                diction[i]=1
        
        for i in v2:
            if i in diction:
                if diction[i]!=0:
                    a.append(i)
                    diction[i]-=1
        
        return sorted(a)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        v1=list(map(int,input().split()))
        m=int(input())
        v2=list(map(int,input().split()))
        ob=Solution()
        ans=ob.common_element(v1, v2);
        for i in ans:
            print(i,end = " ")
        print()
# } Driver Code Ends