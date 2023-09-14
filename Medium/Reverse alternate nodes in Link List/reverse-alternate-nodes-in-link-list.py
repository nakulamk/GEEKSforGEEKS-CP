
# class Solution:
    # def rearrange(self, head):
    #     # Code here
    #     temp=head
    #     res1=[]
    #     res2=[]
    #     while temp:
    #         res1.append(temp.data)
    #         res2.append(temp.next.data)
    #         temp=temp.next.next
        
        
    #     res2=res2[::-1]
        
    #     res1=res1+res2
        
    #     dummyNode=Node(-1)
    #     cur=dummyNode
        
    #     for i in range(len(res1)):
            
    #         newNode=Node(res1[i])
    #         cur.next=newNode
    #         cur=cur.next
            
    #     temp2=dummyNode.next
    #     return temp2
        
        # while temp2 is not None:
        #     print(temp2.data,end=" ")
        #     temp2=temp2.next
            
"""
  reverse alternate nodes and append at the end
  The input list will have at least one element
  Node is defined as
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

"""
class Solution:
    def rearrange(self, head):
        arr = []
        arr2 =[]
        temp = head
        i = 1
        while temp:
            if i%2==0:
                arr2.append(temp.data)
                i+=1
            else:
                arr.append(temp.data)
                i+=1
            temp = temp.next
        arr2 = arr2[::-1]
        arr = arr + arr2
        i = 0
        temp = head
        while temp:
            temp.data = arr[i]
            i+=1
            temp = temp.next
        return head
        # Code here


#{ 
 # Driver Code Starts
# Node Class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains node object
class LinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Code execution starts here
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
            
        Solution().rearrange(llist.head)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
# } Driver Code Ends