

#---------------------------------------------------------------------------Single linkedList -------------------------------------------------------------------------------------#



#data: This is the value contained in the node. It could be anything (integer, string, object, etc.).
# next: This is a pointer to the next node in the list. It starts as None because when a node is created, it might not be linked to another node yet.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



# head: This is the entry point to the linked list. If the list is empty, head is None. If there are nodes, head points to the first node
class LinkedList:
    def __init__(self):
        self.head=None

    #itial head of the list, which is empty at the beginning


     #inserting node  at the beginning of linked list Creating a New Node: A new node is created with the given data.
     # Repointing next: The next attribute of the new node is set to the current head.
     # This effectively "inserts" the node at the beginning, pushing the existing list to the right.
     # Updating head: The head is updated to point to the new node, making it the first node in the list.
    def insert_at_beginning(self,data):
        new_node=Node(data) # creating  a new node with given data
        new_node.next=self.head # Point the new node's next to the current head
        self.head=new_node # Storing new node's reference to the head, make initial node




    #Traversal: Starting from the head, we move through the list using the next pointers.
    # Displaying Data: At each step, we print the data of the current node followed by " -> " to indicate the link.
    # End of List: When current becomes None, we've reached the end of the list, and we print "None" to indicate the end.
    def displaying (self):
        current=self.head # Start from the head
        while current: # Traverse the list  until there are no more node
            print(current.data, end="\n") # Print full linkedlist
            current=current.next # Move to the next node
        print('none') # End of the list



    # inserting node at the end of the list
    # If List is Empty: If self.head is None, it means the list is empty. The new node becomes the head.
    # Traversing the List: If there's at least one node, we traverse the list until we find the last node (where current.next is None).
    # Attaching to End: The new node is linked to the last node by setting the last node's next to the new node.
    def inserting_at_end(self,data):
        new_node=Node(data) # creating new node
        if self.head is None: # check if the list is empty
            self.head=new_node # The new node becomes the head
        else:
            current=self.head # Start from  the head
            while current.next: # Traverse until the last node
                current=current.next # Moving  to the next node
            current.next=new_node # Attach the new node  to the last node's 'next'






            #---------------------------------------------- Deleting node -------------------------------------------------------------#


            # Deleting the First Node (Head)
            # When deleting the head, you want to update the head pointer to point to the next node, effectively removing the first node from the list.
            # Check if List is Empty: If self.head is None, the list is empty, and there's nothing to delete.
            # Move the Head Pointer: If there's at least one node, update the head pointer to the next node (self.head.next). This removes the first node from the list.


    def delete_at_beginning(self):
        if self.head is None:
            print("List is already empty")
        else:
         self.head=self.head.next  # Storing head address to the next node



        # Deleting the Last Node
        # To delete the last node, you need to traverse the list to find the second-to-last node, then set its next pointer to None. This breaks the link to the last node, effectively deleting it.Check if List is Empty: If self.head is None, the list is already empty.
        # Check if Only One Node: If self.head.next is None, it means there's only one node. Setting self.head to None deletes the entire list.
        # Traverse to Second-to-Last Node: You traverse the list, stopping at the second-to-last node by checking current.next.next. If current.next.next is None, you're at the second-to-last node.
        # Break the Link to the Last Node: Set the next pointer of the second-to-last node to None, removing the last node from the list.

    def delete_at_end(self):
       if self.head is None:
           print("List is already empty")
       elif self.head.next is None:
           self.head=None #if the list have only one node so delete the entire list
       else:
         current =self.head
         while current.next.next: # Traverse the list 2nd node  to last node
             current=current.next
         current.next=None # Break the link to the last node






# Accessing class
lkd =LinkedList()
lkd.insert_at_beginning(10)
lkd.insert_at_beginning(8)
lkd.insert_at_beginning(6)
lkd.insert_at_beginning(4)
lkd.delete_at_end()
lkd.insert_at_beginning(2)


lkd.displaying()
