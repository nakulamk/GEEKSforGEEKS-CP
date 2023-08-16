#function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    # def reverseList(self, head):
    #     # Code here
    #     cur=head
    #     arr=[]
    #     i=0
    #     while cur!=None:
    #         arr[i]=cur.data
    #         i+=1
    #         cur=cur.next
            
        
    #     cur=head
    #     i-=1
    #     while cur!=None:
    #         cur.data=arr[i]
    #         i-=1
    #         cur=cur.next
            
    #     return head
    def reverseList(self, head):
        nex=head
        cur=None
        prev=None
        
        while nex!=None:
            prev=cur
            cur=nex
            nex=nex.next
            cur.next=prev
            
        first=cur
        
        return first



#{ 
 # Driver Code Starts
# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().reverseList(lis.head)
        printList(newHead)

# } Driver Code Ends