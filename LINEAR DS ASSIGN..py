#!/usr/bin/env python
# coding: utf-8

# In[ ]:



 # 1. Delete the elements in an linked list whose sum is equal to zero.
    
    
    class Node():
        def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        h = self.head
          if self.head is None:
            self.head = new_node
            return
    else:
         while h.next!=None:
                h = h.next
                h.next = new_node

    def remove_zeros_from_linkedlist(self, head):
        stack = []
        curr = head
        list = []
         while (curr):
            if curr.data >= 0:
                stack.append(curr)
            else:
                temp = curr
                sum = temp.data
                flag = False
                  while (len(stack) != 0):
                    temp2 = stack.pop()
                    sum += temp2.data
                    if sum == 0:
                        flag = True
                     list = []
            break
                 elif sum > 0:
                     list.append(temp2)
                if not flag:
                    if len(list) > 0:
                        for i in range(len(list)):
                            stack.append(list.pop())
                    stack.append(temp)
            curr = curr.next
        return [i.data for i in stack]

if __name__ == "__main__":
    l = Linkedlist()

    l.append(4)
    l.append(6)
    l.append(-10)
    l.append(8)
    l.append(9)
    l.append(10)
    l.append(-19)
    l.append(10)
    l.append(-18)
    l.append(20)
    l.append(25)
    print(l.remove_zeros_from_linkedlist(l.head))
    
    
    
     # 2. Reverse a linked list in groups of given size.

    
    
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 

    def print(self):
 
        ptr = self
        while ptr:
            print(ptr.data, end=' —> ')
            ptr = ptr.next
 
        print('None')
 
   def reverseInGroups(head, k):
 
    
    if head is None:
        return None
 
    current = head
    prev = None
    count = 0
 
    while current and count < k:
 
        count = count + 1
        next = current.next
        current.next = prev
        prev = current
        current = next
 
    
    head.next = reverseInGroups(current, k)

    return prev
 
 
 if __name__ == '__main__':
 
    head = None
    for i in reversed(range(8)):
        head = Node(i + 1, head)
 
    head = reverseInGroups(head, 3)
    head.print()
 



 # 3. Merge a linked list into another linked list at alternate positions.
    
    
   # A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def printList(msg, head):
 
    print(msg, end='')
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
 
    print('None')
 
 
# Function to construct a linked list by merging alternate nodes of
# two given linked lists using a dummy node
def shuffleMerge(a, b):
 
    dummy = Node()
    tail = dummy
 
    while True:
        # empty list cases
        if a is None:
            tail.next = b
            break
 
        elif b is None:
            tail.next = a
            break
 
        # common case: move two nodes to the tail
        else:
            tail.next = a
            tail = a
            a = a.next
 
            tail.next = b
            tail = b
            b = b.next
 
    return dummy.next
 
 
  if __name__ == '__main__':
 
    a = b = None
    for i in reversed(range(1, 8, 2)):
        a = Node(i, a)
 
    for i in reversed(range(2, 7, 2)):
        b = Node(i, b)
 
    # print both lists
    printList('First List: ', a)
    printList('Second List: ', b)
 
    head = shuffleMerge(a, b)
    printList('After Merge: ', head)
  
    
    
    
    
    
 # 4. In an array, Count Pairs with given sum.


   def findPair(nums, target):
 
    # consider each element except the last
    for i in range(len(nums) - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, len(nums)):
 
            # if the desired sum is found, print it
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
 
    # No pair with the given sum exists in the list
    print('Pair not found')
 
 
    if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)
 


 # 5. Find duplicates in an array.
    
    
    
     def findDuplicate(nums):
 
    # create a visited list of size `n+1`
    # we can also use a dictionary instead of a visited list
    visited = [False] * (len(nums) + 1)
 
    # for each element in the list, mark it as visited and
    # return it if seen before
    for i in nums:
 
       
        if visited[i]:
            return i
           visited[i] = True
            return -1
 
    if __name__ == '__main__':
 
    # input list contains `n` numbers between 1 and `n-1`
    # with one duplicate, where `n = len(nums)`
    nums = [1, 2, 3, 4, 4]
 
    print('The duplicate element is', findDuplicate(nums))
    
    
    
    
 # 6. Find the Kth largest and Kth smallest number in an array.


   # Kth largest number in an array 
    
    def kLargest(arr, k):
    # Sort the given array arr in reverse
    # order.
    arr.sort(reverse = True)
    # Print the first kth largest elements
    for i in range(k):
        print (arr[i], end =" ")
 

   arr = [1, 23, 12, 9, 30, 2, 50]
   # n = len(arr)
   k = 3
    kLargest(arr, k)
    

 # Kth smallest number in an array.
 
 # Function to find the k'th smallest element in a list using max-heap
def find_kth_smallest(input, k):
 
    # base case
    if not input or len(input) < k:
        exit(-1)
 
    # build a max-heap from the first `k` elements in the list
    pq = MaxHeap(input[0:k])
 
    # do for remaining list elements
    for i in range(k, len(input)):
        # if the current element is less than the root of the heap
        if input[i] < pq.top():
            # replace root with the current element
            pq.replace(input[i])
 
    # return the root of max-heap
    return pq.top()
 
 
 if __name__ == '__main__':
 
    input = [7, 4, 6, 3, 9, 1]
    k = 3
 
    print('k\'th smallest element in the list is', find_kth_smallest(input, k))



 # 7. Move all the negative elements to one side of the array.


 def find(arr):
    # sort array
    arr.sort()

    # print array
    print("Array after moving all the elements to left:", arr)


    array = [1, 3, -1, 4, -3, -5, -6, 3, 7]
 # call function
    find(array)
    

    
 # 8. Reverse a string using a stack data structure.



 from collections import deque
 
 
 # Reverse a string using a stack
    def reverse(s):
    
       stack = deque(s)
      
      return ''.join(stack.pop() for _ in range(len(s)))
 
 
if __name__ == '__main__':
 
    s = 'Reverse me'
    s = reverse(s)
    print(s)
 



 # 9. Evaluate a postfix expression using stack.
    
    
    
    class Evaluate: 
      
    # Constructor to initialize the class variables 
    def __init__(self, capacity): 
        self.top = -1
        self.capacity = capacity 
        # This array is used a stack  
        self.array = [] 
      
    # check if the stack is empty 
    def isEmpty(self): 
        return True if self.top == -1 else False
      
    # Return the value of the top of the stack 
    def peek(self): 
        return self.array[-1] 
      
    # Pop the element from the stack 
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
        # Push the element to the stack 
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
  
  
    # The main function that converts given infix expression 
    # to postfix expression 
    def evaluatePostfix(self, exp): 
          
        # Iterate over the expression for conversion 
        for i in exp: 
              
            # If the scanned character is an operand 
            # (number here) push it to the stack 
            if i.isdigit(): 
                self.push(i) 
  
            # If the scanned character is an operator, 
            # pop two elements from stack and apply it. 
            else: 
                val1 = self.pop() 
                val2 = self.pop() 
                self.push(str(eval(val2 + i + val1))) 
  
        return int(self.pop()) 
                  
    exp = "231*+9-"
obj = Evaluate(len(exp)) 
print "postfix evaluation: %d"%(obj.evaluatePostfix(exp)) 

    
    
 # 10. Implement a queue using the stack data structure.


   from collections import deque
 
 
# Implement a queue using stack
class Queue:
    s = deque()
 
    # Constructor
    def __init__(self):
        self.s = deque()
 
    # Add an item to the queue
    def enqueue(self, data):
        # push item into the first stack
        self.s.append(data)
 
    # Remove an item from the queue
    def dequeue(self):
 
        # if the stack is empty
        if not self.s:
            print('Underflow!!')
            exit(0)
 
        # pop an item from the stack
        top = self.s.pop()
 
        if not self.s:
            return top
 
        item = self.dequeue()
 
        self.s.append(top)
 
        return item
 
 
if __name__ == '__main__':
 
    keys = [1, 2, 3, 4, 5]
    q = Queue()
 
    for key in keys:
        q.enqueue(key)
 
    print(q.dequeue())       
    print(q.dequeue())       


