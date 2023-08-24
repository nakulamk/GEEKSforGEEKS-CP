class Solution:
    def overlappedInterval(self, intervals):
        intervals.sort()
       # print(intervals)
        arr=[]
        for ele in intervals:
            if len(arr)==0:
                arr.append(ele)
            else:
                if arr[-1][1]>=ele[0]:
                    arr[-1][1]=max(ele[1],arr[-1][1])
                else:
                    arr.append(ele)
        return arr


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends