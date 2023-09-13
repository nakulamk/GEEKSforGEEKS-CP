



class Solution:
    def duplicates(self, arr, n):
        dict = {}
        for i in arr:
            if i not in dict.keys():
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1
        l = []
        for i in dict.keys():
            if dict[i] > 1:
                l.append(i)
        if not l:
            return [-1]
        l = sorted(l)
        return l
    	    
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends