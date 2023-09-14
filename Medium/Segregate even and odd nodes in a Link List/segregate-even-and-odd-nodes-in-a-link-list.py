# User function Template for Python3

# Following is the structure of node 
# class Node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, N, head):
        # code here
        even=[]
        odd=[]
        temp=head
        while temp is not None:
            if temp.data %2==0:
                even.append(temp.data)
            else:
                odd.append(temp.data)
            
            temp=temp.next
        
        res=even+odd
        temp1=head
        for i in res:
            temp1.data=i
            temp1=temp1.next
        
        return head


#{ 
 # Driver Code Starts
# Initial Template for Python3

# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        ob = Solution()
        newhead = ob.divide(n, list1.head)
        printlist(newhead)


# } Driver Code Ends