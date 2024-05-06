#_________________________________________________________________________________Linked List___________________________________________________________________________#

#creating node

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



#creating node by using instance
node1=Node(12)


#print 1st node value
print('1st node value is: ',node1.data)

#print 1st node next that store 2nd node address
print('\nprint 1st node that stored 2nd node address: ',node1.next)

#print current node address
print('\nprint current node, or head of node address',node1)


#now  i want to create more node below
node2=Node(24)
node3=Node(36)
node4=Node(48)

#2nd node  address
print('\n2nd node address ',node2)


#right now we have 4 nodes then next  how to connect 1st to 2nd and others..
print('\nBefore storing 2nd node address we check the 1st node next: ',node1.next)

#now i am storing 2nd node address to the 1st node next
node1.next=node2

print('\nafter storing 2node  to the 1nd node address: ',node1.next)

#similarly we storing other all node address to preivous node

node2.next=node3
node3.next=node4

# printing linkded list
head=node1
while head is not None:
    print(head.data,' ---- ')
    head=head.next

print('None')


#--------------------------------Insertion at beginning of linked list---------------------------------------------------------------#

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


#creating mode
node1=Node(12)
node2=Node(13)
node3=Node(15)


#1st we store node1 address to head 2nd we creating new node by calling Node class 3rd
print('insertion node beginning of the linked list: \n')

head=node1
new_node=Node(16)
new_node.next=head
head=new_node

while head is not None:
 print(head.data,'-----')
 head=head.next