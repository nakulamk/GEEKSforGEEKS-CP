#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        temp1=first
        temp2=second
        i=0
        j=0
        count1=0
        count2=0
        arr1=[]
        arr2=[]
        while temp1 is not None:
            count1+=1 
            temp1=temp1.next
        
        while temp2 is not None:
            count2+=1 
            temp2=temp2.next
        
        temp3=first
        while i!=count1:
            arr1.append(temp3.data)
            i+=1
            temp3=temp3.next
        
        temp4=second
        while j!=count2:
            arr2.append(temp4.data)
            j+=1
            temp4=temp4.next
        
        
        result1 =int("".join(map(str, arr1)))
        result2= int("".join(map(str, arr2)))
        
        sums=result1+result2
        arrSum = [int(digit) for digit in str(sums)]
        
        dummyNode=Node(-1)
        cur=dummyNode
        for i in range(len(arrSum)):
            newNode=Node(arrSum[i])
            cur.next=newNode
            cur=cur.next
        
        return dummyNode.next

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        res = Solution().addTwoLists(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends