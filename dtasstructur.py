# # skip m number of elements delete n number of elements
# def sk_delete(lists):
#     x = lists[0]
#     n = x + 1
#     ll = []
#     i = 0
#     while i < len(lists):
#         if i % n == 0:
#             del lists[i:i+n]
#         else:
#             ll.append(lists[i])
#         i += 1
#     return ll
#
#
# input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# calling = sk_delete(input_list)
# print(calling)
#
# # skip x delete y
#
#
# def x_y(list2):
#     x = list2[0]
#     y = x + 1
#     odd = []
#     while y < len(list2):
#         if y % 2 == 0:
#             del list2[y]
#         else:
#             odd.append(list2[y])
#         y += 1
#     return odd
#
#
# my_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# call = x_y(my_input)
# print(call)
#
# # using linked list skip m delete n
#
# class Lists:
#     def __init__(self, data, next_n):
#         self.data = data
#         self.next_n = next_n
#
#
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#
#     def delt_m(self, m, n):
#         current = self.head
#         count = 0
#         result = 0
#
#         while current is not None and count < m:
#             current = current.next
#             count += 1
#             result.append(current)
#
#         # delete n
#         temp = current.next
#         while count < n:
#             if temp is None:
#                 break
#
#             else:
#                 temp = temp.next
#
#         current.next = temp
#
# # example two
#
#
# # Using linked list: skip m, delete n
#
# class Node:
#     def __init__(self, data=None, next_n=None):
#         self.data = data
#         self.next_n = next_n
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def delete_m_n(self, m, n):
#         current = self.head
#         count_m = 0
#         count_n = 0
#         result = []
#
#         # Traverse m nodes
#         while current is not None and count_m < m:
#             current = current.next_n
#             count_m += 1
#             result.append(current)
#
#         # Delete n nodes
#         temp = current.next_n
#         while count_n < n and temp is not None:
#             temp = temp.next_n
#             count_n += 1
#
#         # Update pointers to skip n nodes
#         current.next_n = temp
#
# # example three
# # skip m delete n
#
#
# class Skip:
#     def __init__(self, data, next_n):
#         self.data = data
#         self.next_n = next_n
#
#
# class Lists:
#     def __init__(self):
#         self.head = None
#
#     def skip_delete(self, m, n):
#         count_m = 0
#         count_n = 0
#         current = self.head
#         results = []
#
#         if current is None:
#             return
#
#         while current and count_m < m:
#             current = current.next_n
#             count_m += 1
#             results.append(current)
#
#         temp = current.next_n
#         while temp and count_n < n:
#             temp = temp.next_n
#
#         current.next = temp
#
#
# # create an instance of the class
# linkedlist = Lists()
# linkedlist.head = Node(1)
# linkedlist.head.next_n = Node(2)
# linkedlist.head.next_n.next_n = Node(3)
# linkedlist.head.next_n.next_n.next_n = Node(4)
# linkedlist.head.next_n.next_n.next_n.next_n = Node(5)
# linkedlist.head.next_n.next_n.next_n.next_n.next_n = Node(6)
#
# # calling
# print("linkedlist before deletion is", linkedlist.head.data)
#
#
# current = linkedlist.head
# while current:
#     print(current.data, end='--->')
#     current = current.next_n
#
#
# print("linked list after deletion is")
# linkedlist.skip_delete(2, 2)
# current = linkedlist.head
# while current:
#     print(current.data, end='--->')
#     current = current.next_n

# find the intersection point of a singly linked list
# first approach

# class Inter:
#     def __init__(self, data, next_n=None):
#         self.data = data
#         self.next_n = next_n
#
#
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#
#     def intersection(self, l1, l2):
#         h1 = self.head
#         h2 = self.head
#
#         if h1 is None:
#             return h2
#
#         if h2 is None:
#             return h1
#
#         while h1:
#             h1 = h2
#
#             while h2 and h1 != h2:
#                 temp = h1
#                 # if both nodes are same
#                 if temp == h2:
#                     return h2
#
#                 temp = temp.next_n
#                 h2 = h2.next_N
#
#             # intersection is not present between the list
#         return None
#
#
# ll1 = Linkedlist()
# ll1.head = Inter(10)
# ll1.head.next_n = Inter(15)
# ll1.head.next_n.next_n = Inter(20)
# ll1.head.next_n.next_n.next_n = Inter(30)
# ll1.head.next_n.next_n.next_n.next_n = Inter(50)
#
# ll2 = Linkedlist()
# ll2.head = Inter(10)
# ll2.head.next_n = Inter(52)
# ll2.head.next_n.next_n = ll1.head.next_n.next_n.next_n
# ll2.head.next_n.next_n.next_n = Inter(12)
# ll2.head.next_n.next_n.next_n.next_n = Inter(15)
#
# # print list before
#
# current1 = ll1
# current2 = ll2
#
# ll1.intersection(l1=current1, l2=current2)
# ll2.intersection(l1=current1, l2=current2)
#
# if not ll1 and ll2:
#     print('no intersection point')
# else:
#     print('intersection found ', ll1, ll2)
#
#
# # it gives error lets try another approach
# # this approach is more time and space saving
#
# class Inters:
#     def __init__(self, data, next_n):
#         self.data = data
#         self.next_n = next_n
#
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#
#     def intersect(self, l1, l2):
#         h1 = l1
#         h2 = l2
#
#         while len(l1) > len(l2):
#             h1 = h1.next
#
#         while len(l2) > len(l1):
#             h2 = h2.next
#
#         while h1 and h2:
#             h1 = h1.ext
#             h2 = h2.next
#
#         if h2 == h1:
#             print("there is intersection in the list")
#         else:
#             print("theres is no intersection in the list")
#
#
# ll1 = Linkedlist()
# ll1.head = Inter(20)
# ll1.head.next_n = Inter(22)
#
# ll2 = Linkedlist(25)
# ll2.head = Inter(50)
# ll2.head.next_n = Inter(45)

# call the function


# write a code to check if a list is a palindrome or not
class Pali:
    def __init__(self, data, next_n=None):
        self.data = data
        self.next_n = next_n


class Linkedlist:
    def __init__(self):
        self.head = None

    def reverse(self):

        prev = None
        current = self.head

#       # perform reverse
        while current:
            next_node = current.next_n
            current.next_n = prev
            prev = current
            current = next_node
        # making previous the current head
        self.head = prev

    def is_palindrome2(self):

        if self.head is None:
            print('empty list is considered a palindrome')
            return

        slow = self.head
        fast = self.head

        while slow.next_n and fast.next_n.next_n:
            slow = slow.next_n
            fast = fast.next_n.next_n

        second_half_head = slow.next_n
        self.reverse()

        # any of these 3 methods is valid because they all represent an instance of the class Linkedlist
        # ll.reverse(second_half_head)

        # when using the second half head instance you dont have to pass in as a parameter
        # second_half_head.reverse()
        # if we had specified a parameter in the reverse function we could do
        second_half_head =
        first_half_head = self.head


        while first_half_head and second_half_head:
            if first_half_head.data != second_half_head.data:
                print("the list is not a palindrome")
                return

            first_half_head = first_half_head.next_n
            second_half_head = second_half_head.next_n

        print("the list is a palindrome")


ll = Linkedlist()
ll.head = Pali(0)
ll.head.next_n = Pali(1)
ll.head.next_n.next_n = Pali(2)
ll.head.next_n.next_n.next_n = Pali(3)
ll.head.next_n.next_n.next_n.next_n = Pali(4)
ll.head.next_n.next_n.next_n.next_n.next_n = Pali(4)
ll.head.next_n.next_n.next_n.next_n.next_n.next_n = Pali(3)
ll.head.next_n.next_n.next_n.next_n.next_n.next_n.next_n = Pali(2)
ll.head.next_n.next_n.next_n.next_n.next_n.next_n.next_n.next_n = Pali(1)
ll.head.next_n.next_n.next_n.next_n.next_n.next_n.next_n.next_n.next_n = Pali(0)

# print list
current = ll.head
while current:
    print(current.data, end='--->')
    current = current.next_n


# calling the function to check if linked list is palindrome
ll.is_palindrome2()
















































# josephus problem
#where n = number of people in the queue k the index position to be executed

# formular =
# josephus(n, k)
# josephusproblem(n-1, k)+k-1)%n+1


#
# # add two numbers representing a linked list
# class Solution:
#     def __init__(self, data, next_node):
#         self.data = data
#         self.next_node = next_node
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#
#     def reverse_list(self, head):
#         prev = None
#         current = head
#         next_n = None
#
#         while current:
#             next_n = current.next
#             current.next = prev
#             prev = current
#             next_n = None
#
#         head = prev
#         return head
#
#     def add_numbers(self, curr1, curr2):
#         self.reverse_list(curr1)
#         self.reverse_list(curr2)
#
#         carry = None
#         summ = None
#         new_node = None
#
#         while curr1 and curr2:
#             summ = curr1 + curr2 + carry
#
#            # carry = (1 if summ >= 10 else 0)
#
#             # create a node to add if one list is longer than the other
#             # if curr1 is none
#             new_node = Node(curr2.data) if curr1 is None else curr1.next
#             curr1.next = new_node
#
#             # if curr2 is none
#             new_node = Node(curr1.data) if curr2 is None else curr2.next
#             if curr2 is not None:
#                 curr1 = new_node
#             else:
#                 curr2.next = new_node
#
#             summ = carry + summ if carry else summ
#             carry = summ // 10
#             summ = summ % 10
#
#             res_node = Node(summ)
#             if summ is not None:
#                 summ.next = res_node
#                 res_node.next curr1 | curr2
#
#             list1 = curr1.next
#             list2 = curr2.next
# # example two
#
# class Solution:
#     def __init__(self, data, next_value=None):
#         self.data = data
#         self.next_value = next_value
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def reverse(self, head):
#
#         previous = None
#         current = head
#         next_node = None
#
#         while current:
#             next_node = current.next
#             current.next = previous
#             previous = current
#             next_node = None
#
#         head = previous
#         return head
#
#     # function to add two numbers represented by linkedlist
#     def add_numbers(self, first, second):
#         # reverse the two lists
#         curr1 = self.reverse(first)
#         curr2 = self.reverse(second)
#
#         # res is the head node of the resultant list
#         summ = 0
#         carry = 0
#         cur1_plus_cur2 = None
#         prev = None
#
#         # while both lists have at least one node
#         while curr1 is not None or curr2 is not None:
#
#             # calculating the sum of the last digits
#             summ = carry + (curr1.data if curr1 else 0) + \
#                    (curr2.data if curr2 else 0)
#
#             # updating carry
#             carry = (1 if summ >= 10 else 0)
#
#             # update sum if it is greater than 10
#             # these code is logically correct but wrong in this context   summ = (summ - 10 if summ >= 10 else summ)
#             # or you can also say
#             summ = summ % 10
#
#             # create a  new node with summ as data
#             temp = Node(summ)
#
#             # if this is the first node then make set it as head of the resultant linked list
#             # else if it is not the first node then connect it to the rest
#
#             if cur1_plus_cur2 is None:
#                 cur1_plus_cur2 = temp
#             else:
#                 prev.next = temp
#
#             # this is equivalent to this code
#             #cur1_plus_cur2 = temp if cur1_plus_cur2 is None else prev.next = temp
#
#             # set previous for next insertion
#             prev = temp
#
#             # move first and second pointers to next node
#             if curr1:
#                 curr1 = curr1.next
#
#             if curr2:
#                 curr2 = curr2.next
#
#         # if carry from prev sum is remaining
#         if carry > 0:
#             temp.next = Node(carry)
#
#             # reverse the resultant answer
#             ans = self.reverse(cur1_plus_cur2)
#             return ans
#
#
# class Node:
#     def __init__(self, data):
#         self.daa = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def insert(self, value):
#
#         if self.head is None:
#             self.head = Node(value)
#
#         else:
#             self.tail.next = Node(value)
#             self.tail = self.tail.next
#
#
# # utility function to print the list
# def printlist(n):
#     while n:
#         print(n.data, end='')
#         n = n.next
#     print()
#
#
# # driver code
# if __name__ == "__main__":
#     arr1 = [7, 5, 9, 4, 6]
#     LL1 = LinkedList()
#     for i in arr1:
#         LL1.insert(i)
#
#     print("first list is ", end='')
#     printlist(LL1.head)
#
#     arr2 = [8, 4]
#     LL2 = LinkedList()
#
#     for i in arr2:
#         LL2.insert(1)
#     print("second list is ", end='')
#
#     # function call
#     curr1_and_curr2 = Solution().addtwolists(LL1.head, LL2.head)
#     print("resultant list is ", end='')
#     print(curr1_and_curr2)



# # rotating around a node in linkedlist
# class Node:
#     def __init__(self, data, next_node=None):
#         self.data = data
#         self.next_node = next_node
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def rotate_around_n(self, key):
#
#         current = self.head
#         last_node = None
#
#         if current is None:
#             return
#
#         while current.next != key:
#             current = current.next
#
#         last_node = current
#         current = None
#
#         last_node.next = self.head
#         self.head = last_node
#
#
# # create instance of the class
# linkedlist = LinkedList()
#
# node1 = Node(5)
# node2 = Node(10)
# node3 = Node(15)
# node4 = Node(20)
# node5 = Node(25)
# node6 = Node(30)
# node7 = Node(35)
#
# node1.next_node = node2
# node2.next_node = node3
# node3.next_node = node4
# node4.next_node = node5
# node5.next_node = node6
# node6.next_node = node7
#
# linkedlist.rotate_around_n(9)
#
# head = node1
# while head:
#     print(head.data)
#     head = head.next_node




















# class Node:
#     def __init__(self, data, next_node):
#         self.data = data
#         self.next_node = next_node
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def rotate_list(self, new_data):
#         current = self.head
#         new_head = None
#         count = 0
#
#         node = Node(new_data)
#
#         if current is None:
#             return
#
#         while current and current.next_node:
#             current = current.next_node
#
#         last_node = current.next_node
#         current.next_node = None
#
#         last_node.next = self.head
#         self.head = last_node
#
#
# linkedlist = LinkedList()
#
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)
# node6 = Node(60)
# node7 = Node(70)
#
# node1.next_node = node2
# node2.next_node = node3
# node3.next_node = node4
# node4.next_node = node5
# node5.next_node = node6
# node6.next_node = node7
#
# linkedlist.rotate_list(4)
# current = linkedlist.head
# while current is not None:
#     print(current.data)
#     head = head.next_node














# # checking palindrome in a linkedlist
# # if it is even
# # if it is odd
# class Node:
#
#     def __init__(self, data, next_value):
#         self.data = data
#         self.next_value = next_value
#
# # if it is even
# class LinkedList:
#     def __init__(self, fast, slow, stack):
#
#     def is_palindrome(self, head, slow):
#
#         fast = head
#         slow = head
#         stack = []
#
#         if fast is None:
#             return
#
#         while fast and fast.next:
#             stack.append(slow.data)
#             slow = slow.nextvalue
#             fast = fast.nextvalue.nextvalue







































# #************************************************************************************************
# # sorting two single linked list
# # nodes needed
# # checker or runner
# # current1 or list 1.head
# # current 2 or list 2.head
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         current1 = self.head
#         current2 = self.head
#         checker = None
#
#         if not current1.next and  not current2.next:
#             current1.data < current2.data
#             current1 = self.head
#             sel f.head.next = current2
#
#             while current1 .data < current2.data:
#                 checker.next = current1
#                 current1 = current1.next
#
#         else:
#             current1.data > current2.data
#             checker.next = current2
#             current2 = current2.next
#
#         checker = checker.next
#
#         current2 = self.head
#         self.head.next = current1
#
#
# linkedlist1 = LinkedList()
# linkedlist2 = LinkedList()
# print(linkedlist1, linkedlist2)
#
#
# # more accurate example
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#
#     def merge_sorted(self, list2):
#         current1 = self.head
#         current2 = list2.head
#         checker = None
#         final = []
#
#         if not current1:
#             return current2
#
#         elif not current2:
#             return current1
#
#         elif not current1 and not current2:
#             return None
#
#         while current1 and current2:
#             if current1.data < current2.data:
#                 checker.next = current1
#                 current1 = current1.next
#                 final.append(current1)
#
#             else:
#                 checker.next = current2
#                 current2 = current2.next
#                 final.append(current2)
#
#             checker = checker.next
#
#             while current1 and or current2:
#                 final.append(current1)
#                 final.append(current2)
#
#             else:
#
#
#
# # final example sort the list before you merge them
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self, ):
#         # sorting before
#
#
#







#*********************************************************************************************

# removing duplicates
# using hashmap
# class Node:
#     def __init__(self, data, next_node):
#         self.data = data
#         self.next_node = next_node
#
#
# class LinkedList:
#     def __init__(self, new_data):
#         self.head = Node(new_data)
#
#     def remove_duplicates(self):
#         current = self.head
#         visited = set()
#
#         if not current and not current.next_node.data:
#             print("linked list is empty")
#             return
#
#         while current:
#             current = current.next_node
#             visited.add(current)
#
#             counter = 0
#             while current in visited:
#                 counter += 1
#                 current = current.next_node.next_node
#                 for value in visited:
#                     if current.next_node.data == value:
#                         print(f"node data {current.next_node.data} is duplicated by {counter} times")
#             else:
#                 current.next_node

#
# linked_list = LinkedList(50)
#
# linked_list.head.next_node = Node(50)
# linked_list.head.next_node.next_node = Node(30)
# linked_list.head.next_node.next_node.next_node = Node(50)
# linked_list.head.next_node.next_node.next_node.next_node = Node(30)
# linked_list.head.next_node.next_node.next_node.next_node.next_node = Node(10)
# linked_list.head.next_node.next_node.next_node.next_node.next_node.next_node = Node(10)
# linked_list.head.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(0)
#
#
# linked_list.remove_duplicates(next_node)

#
# # using selective method
#
#
#     def remove_duplicates(self):
#
#         runner = None
#         current = self.head
#
#         if not current and not runner:
#             return
#
#         while current:
#             runner = current
#
#             duplicates = []
#             while runner.next_node is not None:
#                 runner = runner.next_node
#                 if runner.data == current.data:
#                     duplicates.append(runner.data)
#                     runner.next_node = runner.next_node.next_node
#                     count = count + 1
#                     print(f"duplicate items are {duplicates} " .split(","))
#                     print(f"{count} number of duplicates is detected")
#
#                 else:
#                     runner = runner.next_node
#
#         current = current.next_node
#
#
# linkedlist = LinkedList(40)


# node1 =
# node2 = Node(30)
# node3 = Node(20)
# node4 = Node(30)
# node5 = Node(40)
# node6 = Node(50)
# node7 = Node(40)
# node8 = Node(50)

# node1.next_node = node2
# node2.next_node = node3
# node3.next_node = node4
# node4.next_node = node5
# node5.next_node = node6
# node6.next_node = node7
# node7.next_node = node8
#
# first_node = node1
# while first_node is not None:
#     print(first_node.data, end="--->")
#     first_node.next_node

#
# # accurate version
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next_node = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def remove_duplicates(self, new_data):
#         current = self.head
#         runner = None
#
#         if not current and not current.next_node:
#             return
#
#         while current is not None and current.next_node is not None:
#             runner = current
#             count = 0
#
#             while runner:
#                 runner = runner.next_node
#                 if runner.next_node.data == current.data:
#                     count += 1
#                     print(f"duplicate item {runner.next_node.data} found")
#                     runner.next_node = runner.next_node.next_node
#
#                 if count < 0:
#                     print(f"{count} number of duplicates removed from {current.data}")
#
#             else:
#                 runner = runner.next_node
#
#         else:
#             current = current.next_node
#
#     # example usage
#     linkedlist = LinkedList(40)
#     linkedlist.head.next_node = Node(30)
#     linkedlist.head.next_node.next_node = Node(50)
#     linkedlist.head.next_node.next_node.next_node = Node(30)
#     linkedlist.head.next_node.next_node.next_node.next_node = Node(70)
#     linkedlist.head.next_node.next_node.next_node.next_node.next_node = Node(50)
#
#     linkedlist.remove_duplicates()


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next_node = None
#
#
# class LinkedList:
#     def __init__(self, head_value):
#         self.head = Node(head_value)
#
#     def remove_duplicates(self):
#         current = self.head
#
#         while current and current.next_node:
#             runner = current
#             count = 0
#
#             while runner.next_node:
#                 if runner.next_node.value == current.value:
#                     count += 1
#                     print(f"Duplicate item {runner.next_node.value} found.")
#                     runner.next_node = runner.next_node.next_node
#                 else:
#                     runner = runner.next_node
#
#             if count > 0:
#                 print(f"{count} number of duplicates removed for item {current.value}")
#
#             current = current.next_node
#
#
# # Example Usage:
# linkedlist = LinkedList(40)
# linkedlist.head.next_node = Node(30)
# linkedlist.head.next_node.next_node = Node(50)
# linkedlist.head.next_node.next_node.next_node = Node(30)
# linkedlist.head.next_node.next_node.next_node.next_node = Node(70)
# linkedlist.head.next_node.next_node.next_node.next_node.next_node = Node(50)
# linkedlist.head.next_node.next_node.next_node.next_node.next_node.next_node = Node(50)
# linkedlist.head.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(50)
# linkedlist.head.next_node.next_node.next_node.next_node.next_node.next_node.next_node.next_node = Node(50)
#
# linkedlist.remove_duplicates()
































#*********************************************************************************************
# # find a duplicate in a node and delete it
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.data = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
# # 1using hashmap
# # 2 using other method
#     # using hashmap
#     def remove_duplicate(self):
#         current = self.head
#         runner = None
#
#         if current.next is None and current is None:
#             print("linked list is empty")
#
#         while current and current.next:
#             runner = current
#
#             while runner.next:
#                 if runner.next.data == current.data:
#                     runner.next = runner.next.next
#
#                 else:
#                     runner = runner.next
#
#
#         current = current.next

#****************************************************************************************************#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next_value = None
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#       # find the beginning of a loop in python#
#     # find the beginning of a loop in a linked list
#     def loop_beginning(self):
#         fast = self.head
#         slow = self.head
#         if not self.head or not self.head.next:
#             return None
#
#         while fast and fast.next_value:
#             slow = slow.next_value
#             fast = fast.next_value.next_value
#
#             if slow == fast:
#                 print("the loop is detected")
#                 break
#
#             else:
#                 print("three is no loop detected")
#
#                 slow = self.head
#             while slow != fast:
#                 slow = slow.next_value
#                 fast = fast.next_value
#
#                 if slow == fast:
#                     print("the loop or cycle starts from here")
#                     break
# ***********************************************************************************
    # finding a loop in a linked list can be done in three means
# 1 using hashing
# 2 mark visited nodes
# 3 floyds cycle finding algorithm thus the tortoise and hare method

    # checking if there is a cycle in a linked list this means we want to check if a node prints back to the previous
    # node after the looping
#
#     def check_cycle(self):  # , fast, slow):
#
#         if not self.head:
#             print("list is empty there is no cycle in the loop")
#             return
#         fast = self.head
#         slow = self.head
#
#         while fast and fast.next_value: # is not none
#             slow = slow.next_value
#             fast = fast.next_value.next_value
#             if slow == fast:
#                 print("there is a cycle or loop in the list")
#                 return
#             else:
#                 print("there is no cycle in the loop")
#
#         print("there is no cycle in the loop")
#
#
# linked_list = LinkedList()
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)
# node7 = Node(7)
# node8 = Node(8)
# node9 = Node(9)
# node10 = Node(10)
#
#
# linked_list.head = node1
# node1.next_value = node2
# node2.next_value = node3
# node3.next_value = node4
# node4.next_value = node5
# node5.next_value = node6
# node6.next_value = node7
# node7.next_value = node8
# node8.next_value = node9
# node9.next_value = node10
# node10.next_value = node1  # creating a cycle
#
# linked_list.check_cycle()
#
#
# # example 2 check if there is a loop or not
# def check_loop(self):
#     fast = self.head
#     slow = self.head
#
#     if self.head is None:
#         print("linked list is empty there is no loop")
#
#     while fast and fast.next_value is not None:
#         slow = slow.next_value
#         fast = fast.next_value.next_value
#
#         if slow == fast:
#             print("there is no cycle or loop in the linkedlist")
#             return
#         else:
#             print("there is a loop in the linked list")
#
#
#
#
# def check_again(self):
#     fast = self.head
#     slow = self.head
#
#     if not self.head:
#         print("linkedlist is empty is empty there is no loop")
#
#     while fast and fast.next_value:
#         slow = slow.next_value
#         fast = fast.next_value.next_value
#     if fast and fast.next_value :
#             print("there is no loop")
#             return
#         else:
#             print("there is a loop")
#
# print(print("there is not loop"))
#
#
# # detecting and deleting a cycle in a linked list
#
# def detect_and_delete(self):
#     fast = self.head
#     slow = self.head
#
#     while fast and fast.next_value:
#         slow = slow.next_value
#         fast = fast.next_value.next_value
#
#         if slow == fast:
#             fast = self.head
#             self.head.next = slow
#             slow = self.head
#             fast = self.head
#             print("loop was found and is deleted")
#             return
#
#         else:
#             print("there is no loop in the linked list")
#

#**************************************************************************************

# reversing a list in python

# two ways of reversing a single linked list

# 1 iterative way
# 2 recursive way

#     def rivers(self, previous_node, current_node, next_node):
#
#         previous_node = None
#         current_node = self.head
#         next_node = None
#
#         while current_node is not None:
#             next_node = current_node.next
#             current_node.next = previous_node
#             previous_node = current_node
#             current_node = next_node
#             self.head = previous_node
#
#
#     def rivals(self, previous, current, next_node):
#         previous = None
#         current = self.head
#         next_node = None
#
#         while current is not None:
#             next_node = current.next
#             current.next = previous
#             previous = current
#             current = next_node
#             self.head = previous
#
#     def rivas(self):
#         previous_node = None
#         current_node = self.head
#         next_node = None
#
#         while current_node is not None:
#             next_node = current_node.next
#             current_node.next = previous_node
#             previous_node = current_node
#             current_node = next_node
#             self.head = previous_node
#
#
#
#
#
# # create three nodes previous node, current node and next node
# # current will be the head node and previous will point to none
# # traverse the linked list while the current pointer is not none
# # store the next node in next node to avoid loosing the reference during the reversal
#
#
#     def reves(self, previous_node, current_node, next_node):
#         current_node = self.head
#         previous_node = None
#
#         while current_node is not None:
#             next_node = current_node.next
#             current_node.next = previous_node
#             previous_node = current_node
#             self.head = previous_node
#
#     def reversing(self, previous_node, current_node):
#         current_node = self.head
#         previous_node = None
#
#         while current_node is not None:
#
#             next_node = current_node.next
#             current_node.next = previous_node
#             previous_node = current_node
#             current_node = next_node
#             self.head = previous_node

# curretnode = self.head
# previous_node = None

# while currentnode is not none
# next_node = currentnode.next
# currentnode.next = previousnode
# previous node = currentnode
# create three nodes previous, current and next node and make current node the head node set previous node to non
# while current node is not empty
# nextnode = currntnode.next
# currentnode = currentnode.next



#*******************************************************************



# # # linked lists
# # # two simple ways of doing it
# # # firstly creating the nodes and linking them
# # class LinkedListNode:
# #     def __init__(self, value, next_node=None):
# #         self.value = value
# #         self.next_node = next_node
# #
# #
# # # creating the nodes
# # node1 = LinkedListNode("node 1 value")
# # node2 = LinkedListNode("node 2 vlue")
# # node3 = LinkedListNode("node 3 value")
# # node4 = LinkedListNode("node 4 value")
# # node5 = LinkedListNode("node 5 value")
# #
# # # linking nodes
# # node1.next_node = node2
# # node2.next_node = node3
# # node3.next_node = node4
# # node4.next_node = node5
# #
# # current_node = node1
# # if current_node is None:
# #     print("linked list is empty")
# #
# # else:
# #     while current_node is not None:
# #         print(current_node.value, end="-->")
# #         current_node = current_node.next_node
# #         if current_node is None:
# #             print('none')
# #
# # # we hve succesfully finished
# # # note that using this method , you dont hve to use the single linked list class and its constructor
# # print("finished")
#
#
# # this is the second method of coding linked list
#
# #
# # class Node:
# #     def __init__(self, data, reference):
# #         self.data = data
# #         self.reference = None
# #
# #
# # # creating the linked list
# # class LinkedList:
# #     def __init__(self):
# #         self.head = None
# #
# #
# # # inserting or adding a node at the beginning
# # # this entails 4 procedures
# #
# # # the function to insert
# # def insert_beginning(self, new_node1):
# #
# #     # 1 create the node and
# #     # 2 put in the data
# #     new_node1 = Node("the data of new node 1")
# #
# #     # 3 make next of new node as head
# #     new_node1.next = self.head
# #     # 4 move the head to point to new node
# #     self.head = new_node1
# #
# #
# # # appending after a node or at a middle
# # def insert_at_middle(self, previous_node, new_node):
# #     # 1 check if the given previous node exist
# #     if previous_node is None:
# #         print("the given previous node does note exist")
# #         return
# #
# #     # 2 create a new node
# #     # 3 and put in the data
# #     new_node = Node("new node data")
# #
# #     # 4 make next of new node as next of previous node
# #     new_node.next = previous_node.next
# #
# #     # 5 make next of previous node as new node
# #     previous_node.next = new_node
# #
# #
# # # appending at the end of the linked list
# # def append_at_end_of_linkedlist(self, new_data):
# #
# #     # 1 create the node
# #     # 2 put in data
# #     # 3 set next as none
# #
# #     new_node3 = Node("new node 3 data")
# #
# #     if self.head is None:
# #
# #         # 4 if the linked list is empty then make the new node as head
# #         self.head = new_node3
# #         return
# #
# #     # 5 else traverse till the last node
# #     last = self.head
# #     while last.next:
# #         last = last.next
# #
# #     # 6 change the next of last node
# #     last.next = new_node3
# #
# # # utility function to print( the linked list)
# #
# #
# # def printlist(self):
# #     temp = self.head
# #     while temp:
# #         print(temp.data)
# #         temp = temp.next
# #
# # # done with everything related to inserting node in linked list
# # # code execution starts here
# #
# #
# # if __name__ == 'main':
# #     # start with the empty list
# #     llist = LinkedList()
# #     # insert 6 so linkedlist becomes 6 --> none
# #     llist.insert_beginning(6)
# #     llist.inser_middle(6)
# #     llist.insert_at_end(10)
# # # left with the data printing
#
#
# # creating the nodes class
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.reference = None
#
#
# # creating the linked list class
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#
# # inserting at the beginning this entails 4 steps
# def insert_beginning(self, new_data):
#
#     # create the node and assign the data
#     new_node = Node("data in node 1")
#
#     # make next of new node as head
#     new_node.next = self.head
#
#     # move the head to point to new node
#     self.head = new_node
#
#
# def insert_before_or_middle(self, previous_node, new_node1):
#
#     # check if previous node is empty or exist
#     if previous_node is None:
#         print("the given previous node does not exist")
#
#         #  2create the node
#         # 3 put in data
#         new_node1 = Node("data of inserting node")
#         new_node1.next = previous_node.next
#         previous_node.next = new_node1
#
#
# def last(self):
#
#     new_node8 = Node("new node")
#     if self.head is None:
#         new_node8 = self.head
#
#     else:
#         last1 = self.head
#         while last1.next:
#             last1 = last1.next
#             new_node8 = last1
#
#
# # method to insert node at last position
#
# def insert_last(self, next_node, last_node):
#     new_node = Node("kofi is a boy")
#
#     if self.head is None:
#         last_node = self.head.next
#         return
#
#     else:
#         next_node = self.head
#         while next_node.next:
#             next_node = next_node.next.next
#
#
# # loop through a node till the end
# def lop(self):
#     if self.head is None:
#         print("node is empty")
#
#     else:
#         current_node = self.head
#         while current_node.next:
#             current_node = current_node.next
#             if current_node.next is None:
#                 current_node = current_node.next
#             print("reached the last node")
#
#
# # self try
# def insert_at_beginning(self, data):
#     self.head = None
#     new_node = Node(data)
#     new_node.next = self.head
#     self.head = new_node
#
#
# def insert_before_a_target_node(self, target_node, current_node):
#     self.head = None
#     new_node = Node("ghana black stars")
#
#     if target_node is self.head:
#         new_node.next = self.head
#         self.head = new_node
#         return
#     current_node = self.head
#     while current_node.next != target_node:
#         current_node = current_node.next
#         if current_node == target_node:
#             new_node.next = current_node.next
#             current_node.next = new_node
#
#
# # trying again
# def add_before(self, current_node, target_node, data):
#     self.head = None
#     insert_node = Node(data)
#
#     if target_node == self.head:
#         insert_node.next = self.head
#         return
#
#     current_node = self.head
#     while current_node.next:
#         current_node = current_node.next
#         if current_node == target_node:
#             insert_node.next = current_node.next
#             current_node.next = insert_node
#
#
# # insert at any position
# def any_position(self, index, data):
#     self.head = None
#     new_node = Node(data)
#
#     # index start s from 0
#     # position must be entered by the user
#     position =
#
# # insert at last
# def insert_last(self, data):
#     self.head = None
#     new_node = Node(data)
#     if self.head is None:
#         new_node = self.head.next
#         self.head.next = new_node
#         return
#
#     else:
#         current_node = self.head
#         while current_node.next:
#             current_node = current_node.next
#             if current_node is None:
#                 last_node = current_node
#                 current_node = last_node
#
#
# def insert_before(self, data, target_node):
#     self.head = None
#
#     new_node = Node(data)
#     if self.head is None:
#         new_node.next = self.head
#         self.head = new_node.next
#         return
#
#     current_node = self.head
#     while current_node.next != target_node:
#         current_node = current_node.next
#         if current_node.next == target_node:
#             current_node = new_node
#
#
# def insert_after(self, data, target_node):
#     self.head = None
#     new_node = Node
#
#     if self.head is not None:
#         current_node = self.head
#         while current_node.next != target_node.next:
#             current_node = current_node.next
#             if current_node == target_node.next:
#                 new_node = target_node.next
#
#     else:
#         if self.head is None:
#             new_node.next = self.head
#             self.head = new_node
#
#
# def insert_at_beginning(self, data):
#     self.head = None
#     new_node = Node(data)
#
#     if self.head is None:
#         new_node.next = self.head
#         self.head = new_node
#     else:
#         print("oom something went wrong")
#
#
# # traversing through a linked list in python
# def retrieve_data(self):
#
#     temp = self.head
#     while temp is not None:
#         print(temp.data)
#         temp = temp.next
#         print()
#
#     else:
#         self.head is None
#         print('linked list is empty')
#
#
# # deleting a node in linked list
# def del_beginning(self, key, previous = None):
#     self.head = None
#
#     # if self .head itself holds the value to be deleted
#     if self.head is not None:
#         if self.head.value == key:
#             self.head = self.head.next
#             self.head = None
#             return
#
#     else:
#         temp = self.head
#         while temp.next.value != key:
#             temp = temp.next.value
#             if temp.next.value == key:
#                 previous = temp.next
#                 temp is None
#
#
# # nb we can delete node at a data field or at a given position
# # lets start with a data field
# # deleting at a data field
# def deleting(self, key):
#     # to delete you need to check two things
#     # 1 check if the node to be  deleted is the head node
#     # 2 check if the node to be deleted is not the head node
#     current_node = self.head
#     if current_node and current_node.data == key:
#         self.head = current_node.next
#         current_node = None
#         return
#
#     # if node to delete is not the head node then loop to find the node
#     previous_node = None
#     while current_node.data != key:
#         previous_node = current_node
#         current_node = current_node.next
#     if current_node is None:
#         previous_node.next = current_node.next
#         current_node is None
#
#
# # deleting at a data field
# def delete_node(self, key):
#     current_node = self.head
#     # check if key to delete is the head node
#     if current_node and current_node.data == key:
#         current_node.next  = self.head
#         self.head = current_node
#         self.head = None
#
#
#     previous_node = None
#     while current_node is not None and current_node.data != key:
#         previous_node = current_node
#         current_node = current_node.next
#     if current_node is None:
#         return
#
#     previous_node.next = current_node.next
#     current_node = None
#
#
#
#
# def delete_before(self):
#     pass
#
#
#
# def delete_after(self):
#     pass
#
# # this contains mistake
# # deleting the last node that is not none
# def delete_at_last(self, ):
#     previous_node = not None
#     current_node = self.head
#     while current_node and current_node.next is not None:
#         previous_node = current_node
#         current_node = current_node.next
#         if current_node is None:
#             previous_node = current_node
#             previous_node = None
#
# # deleting from a specified position
# def delete_nod_at_position(self, target_node):
#     current_node = self.head
#     previous_node = None
#
#     if current_node is not None:
#         current_node.next = self.head
#         self.head = current_node
#         self.head is None
#
#     else:
#         while current_node.next is not None:
#             previous_node = current_node
#             current_node = current_node.next
#             if current_node == target_node:
#                 previous_node.next = current_node.next
#                 current_node = None
#
#
#
# def deleting_at_specific_postion(self, target_node):
#     self.head = None
#     if self.head and self.head is None:
#         self.head.next = self.head
#         self.head is None
#
#
#     else:
#         previous_node = None
#         current_node = self.head
#         while current_node and current_node != target_node:
#             previous_node = current_node
#             current_node = current_node.next
#             if current_node == target_node:
#                 previous_node.next = current_node.next
#                 current_node is None
#
#
#
# # the ai 20 exercises solution
#
# class AiNode:
#     def __init__(self, data, value):
#         self.data = data
#         self.value = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#
#     def insert_beginning(self, data):
#
# # 1 explain the process of inserting a node at the beginning
# # solution
# # create the node
# # 2 put in data
# # 3 make the head node next of the new node
# # 4 make the new node head of the  linked list
#         self.head = None
#         new_node =  Node(data)
#         new_node.next = self.head
#         self.head = new_node.next
#
# # 2 how would you implement the deletion 0f a specific value in a singly linked list
#     # this code contains error
#     def delete_specific_value(self, key, next_node):
#         previous_node = self.head
#
#         if previous_node and previous_node.data == key:
#             next_node = previous_node.next
#             previous_node = None
#
#         else:
#             next_node = self.head
#             while next_node and next_node.data != key:
#                 previous_node = next_node
#                 next_node = next_node.next
#                 if next_node == key:
#                     previous_node.next = next_node.next
#                     next_node = None
# # trying another one delete by data
# def try_delete(self, key):
#     current_node = self.head
#     # in case the key is in the head node
#     if current_node and current_node.data != key:
#         self.head = current_node.next
#         current_node = None
#         return
#
#     else:
#         previous_node = self.head
#         while current_node and current_node.data != key:
#             previous_node = current_node
#             current_node = current_node.next
#
#         if not current_node:
#             print(f"the key {key} is not found")
#
#         previous_node.next = current_node.next
#                 current_node = None
#
#
#
# # this is correct
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def delete_specific_value(self, key):
#         current_node = self.head
#
#         # Case: The key is in the head node
#         if current_node and current_node.data == key:
#             self.head = current_node.next
#             current_node = None
#             return
#
#         previous_node = None
#
#         # Traverse the linked list to find the key
#         while current_node and current_node.data != key:
#             previous_node = current_node
#             current_node = current_node.next
#
#         # Case: The key was not found
#         if not current_node:
#             print(f"The key {key} was not found in the linked list.")
#             return
#
#         # Update the next pointer of the previous node to skip the key
#         previous_node.next = current_node.next
#         current_node = None  # Optional: Free the memory occupied by the current_node















































