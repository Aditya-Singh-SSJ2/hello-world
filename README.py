# hello-world
#test12345
#hi it's AdiTOSH
print("Hey It's python now")
print("ENTER ANY NO.:")
a = int(input())
print ("you Entered - ", a)
#USELESS!!!

#INTRODUCING LINKEDLIST ALL CONCEPTS SO FAR LEARNT:::
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
            
     def insert(self,head,data): 
        
            
        new_node = Node(data)

        if head is None:
            head = new_node
            return head
        last = head
        while(last.next):
            last = last.next
        last.next = new_node
        return head
 
if "_name_" == "_main_":
    mylist= Solution()
    T=int(input())
    head=None
    for i in range(T):
        data=int(input())
        head=mylist.insert(head,data)    
    mylist.display(head); 	  

    #copy pasted from visual studio code from where I made and executed this code, successfully designed linkelist function out of nothing!!!   .....SUCCESS!!!!
