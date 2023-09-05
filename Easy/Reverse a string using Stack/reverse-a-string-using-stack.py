#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    
    #Add code here
    stack=[]
    s = ''
    for i in S:
        stack.append(i)
    
    while stack:
        s+=stack.pop()
    
    return s
        
        

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends