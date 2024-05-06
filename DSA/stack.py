



#-------------------------------------------------------------------------- Stack ---------------------------------------------------------------------------------#

#A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack,
 # a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.

# The functions associated with stack are:
# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

stack=[1,3,5,7,9]
print('print stack \n',stack)

# insert new element in stack
stack.append(11)
print('inset element in stack at the end \n',stack)

  # remove  the element in the stack
stack.pop()
print('print the stack after removing element \n',stack)

# Get size of stack
print("print the size of stack\n",len(stack))
