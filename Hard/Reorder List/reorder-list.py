
#User function Template for python3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


#Back-end complete function Template for Python 3
class Solution:
    def reorderList(self,head):
        l=[]
        temp=head
        while(temp!=None):
            l.append(temp.data)
            temp=temp.next
        p=-1
        pp=0
        kk=[]
        for i in range(len(l)//2):
            kk.append(l[i])
            kk.append(l[-i-1])
        if(len(l)!=len(kk)):
            kk.append(l[len(l)//2])
        temp=head
        for i in range(len(kk)):
            temp.data=kk[i]
            temp=temp.next
        return head
        
        
        
        
        
        # def reverse(head):
        #     p=None
        #     n=None
        #     curr=head
            
        #     while curr:
        #         n=curr.next
        #         curr.next=p
        #         p=curr
        #         curr=n
                
        #     return p
            
        # slow=node(head)
        # fast=node(head)
        # while fast and fast.next:
        #     slow=slow.next
        #     fast=fast.next.next
            
        # temp=node(slow.next)
        # slow.next=None
        # s=node(reverse(temp))
        # f=node(head)
        
        # while f and s:
        #     t1=node(f)
        #     t2=node(s)
        #     f=f.next
        #     s=s.next
        #     t1.next=t2
        #     t2.next=f


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    def printList(self,head):
        tmp = head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        ob=Solution()
        ob.reorderList(head)

        lis.printList(head)

# } Driver Code Ends