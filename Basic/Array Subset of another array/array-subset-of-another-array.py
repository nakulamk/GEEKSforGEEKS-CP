#User function Template for python3

def isSubset( a1, a2, n, m):
    
    diction1={}
    for i in a1:
        if i in diction1:
            diction1[i]+=1
        else:
            diction1[i]=1
    
    diction2={}
    for i in a2:
        if i in diction2:
            diction2[i]+=1
        else:
            diction2[i]=1
    
    
    
    for i in diction2:
        if i not in diction1:
            return "No"
        if diction2[i]>diction1[i]:
            return 'No'
    
    return "Yes"
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends