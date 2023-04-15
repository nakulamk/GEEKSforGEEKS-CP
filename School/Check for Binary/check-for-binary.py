# Return true if str is binary, else false
def isBinary(str):
    #code here
    x = "01"
    for c in str:
        if c not in x:
            return 0
    return 1
            


#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        if isBinary(str):
            print (1)
        else:
            print (0)
# } Driver Code Ends