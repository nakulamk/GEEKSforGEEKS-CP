# A linked list (LL) node 
# to store a queue entry 
'''class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None'''
        
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        self.head=None
        self.tail=None
    
    #Function to push an element into the queue.
    def push(self, item):
        newnode = Node(item)
        if(self.head==None):
            self.head =newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
            
         
         #Add code here
    
    #Function to pop front element from the queue.
    def pop(self):
         if(self.head==None):
             return -1
         else:
             temp=self.head
             self.head=self.head.next
             return temp.data
         #add code here




#{ 
 # Driver Code Starts

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   
# } Driver Code Ends