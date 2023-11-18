#User function Template for python3

# def findElement( arr, n):
#     big=arr[0]
#     small=arr[n-1]
#     max=[]
#     min=[]
#     ele=-1
#     for i in range(n):
#         if arr[i]>big:
#             big=arr[i]
#         max[i]=big
    
#     for i in range(n-1,-1,-1):
#         if arr[i]<small:
#             small=arr[i]
#         min[i]=small
    
#     for i in range(n):
#         if i!=0 and i!=n-1:
#             if min[i]==max[i]:
#                 ele=min[i]
#                 break
            
    
#     return ele

# Solution:
#  create 2 arrays namely min and max 
#  store the elements in max array by traversing from left to right
#  store the elements in min array by traversing from right to left 
#  traverse the array from left to right and if min[i] == max[i] then make ele = min[i] and break out of the loop

def findElement( arr, n):
    
    arr1, arr2 = [1]*n, [1]*n
    max = arr[0]
    min = arr[n-1]
    
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
        arr1[i] = max
    
    for i in range(n-1, -1, -1):
        if arr[i] < min:
            min = arr[i]
        arr2[i] = min
    
    for i in range(1, n-1):
        if arr1[i] == arr2[i]:
            return arr1[i]
    
    return -1
        
        
    
    
    






#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(findElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends