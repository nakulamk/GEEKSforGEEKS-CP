"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    # def reverse(self,head, k):
    #     # Code here
    #     temp=head
    #     i=1
    #     r=None
    #     q=None
    #     p=head
        
    #     while i<=k:
    #         r=q
    #         q=p
    #         p=p.next
    #         q.next=r
    #         i+=1
    #     head=q
        
    #     nex=q.next
    #     cur=None
    #     prev=None
        
    #     while nex!=None:
    #         prev=cur
    #         cur=nex
    #         nex=nex.next
    #         cur.next=prev
    #     temp.next=cur
        
    #     return head
    
    def reverse(self,head, k):
        ans=[]
        i= head
        while (i.next != None ):
            ans.append(i.data)
            i= i.next
        ans.append(i.data)
        j=0
        while j<len(ans):
            ans[j:j+k]= ans[j:j+k][::-1]
            j+=k 
        new_head= None
        new_tail= None
        cur=0
        while cur < len(ans):
            node= Node( ans[cur])
            if new_head==None:
                new_head= node
                new_tail= node
            else:
                new_tail.next= node
                new_tail= node
            cur+=1
        return new_head

#{ 
 # Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends