# #code
# def custom_sort(arr):
#     freq_dict = {}
    
#     # Count the frequency of each element in the array
#     for num in arr:
#         if num in freq_dict:
#             freq_dict[num] += 1
#         else:
#             freq_dict[num] = 1
    
#     # Sort the array based on frequency and element value
#     def custom_sort_key(elem):
#         return (-freq_dict[elem], elem)
    
#     sorted_arr = sorted(arr, key=custom_sort_key)
    
#     return sorted_arr

# # Example usage

# array_length = int(input())
# arr=[]
# for i in range(array_length):
#     element = int(input())
#     arr.append(element)
# sorted_arr = custom_sort(arr)
# print(sorted_arr)  


a=int(input())
for j in range(a):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    d={}
    for i in range(n):
        if arr[i] in d.keys():
            d[arr[i]]=d[arr[i]]+1
        else:
            d[arr[i]]=1
    l=sorted(d.items(),key=lambda item: item[1],reverse=True)
    for i,j in l:
        for k in range(0,j):
            print(i,end=" ")
    print()