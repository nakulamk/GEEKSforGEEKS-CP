#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code her
        res = {}
        for i in A:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1

        max_count = max(res.values())
        if max_count > (N // 2):
            for i in res:
                if res[i] == max_count:
                    return i
        
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends