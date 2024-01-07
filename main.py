import array as arr


# nb print all numbers less than five and thier square roots
# for number in range(0, 5):
#     print(number)
#     print(f"square root of {number} is {number * number}. ")


# using while loop
#
# n = 0
# while n < 5:
#     print(n)
#     n += 1
#


# print a number and all the numbers that is lesser than it
# x = 1
# n = 5
# while x <= n:
#     # print(x, end="")
#     print(x, end=",")
#     x += 1

# you can also use a for loop to achieve this
#
# # getting the second-largest number from a list
# my_list = [1, 10, 5, 2, 9, 3, 8, 7, 4, 6]
# sorted_numbers = sorted(my_list, reverse=True)
# second_largest = sorted_numbers[1]
# print(sorted_numbers)
# print(second_largest)

# using a for loop
# my_list = [1, 10, 5, 2, 9, 3, 8, 7, 4, 6]
# sorting = sorted(my_list)
# print(sorting)
# for number in sorting:
#     second = sorting[-2]
#     print(second, end="")

# using another aproach
# n = int(input()) arr = map(int, input().split())
#
# a_list=list(arr)
#
# max1=a_list[0]
# max2=float('-inf')
#
# for i in range(1, len(a_list)):
#     if a_list[i]>max1:
#         max2=max1
#         max1=a_list[i]
#     elif a_list[i]>max2 and a_list[i]!=max1:
#         max2=a_list[i]
# print(max2)
# 0
#
# # another method again
# n = int(input()) arr = list(map(int, input().split()))
#
# unique_arr = list(set(arr))
# unique_arr.sort()
# if len(unique_arr) >= 2:
#     print(unique_arr[-2])
# else:
#     print("Array doesn't have a second-largest element.")


# store the name of students in a nested list and fid the student with the second high mark
# name = []
# score = []
# final_list = []
# for i in range(int(input())):
#     name = input()
#     score = int(input())
#     final_list.append([name, score])
#
#
# print("ghana")

# collect user input and store in a dictionary


# name_and_marks = {}
# size_of_data = int(input("enter size of data: "))
# for info in range(size_of_data):
#     names = input("enter student name: ")
#     marks = input("enter student marks: ").split(',')
#     name_and_marks[names] = marks
# print(name_and_marks)
# key_in = True
# if names in name_and_marks:
#     print("cant use more than one keys in a dictionary")
#
# else:
#     key_in = False
#     # names = input("enter student name: ")
#     # size_of_marks = int(input("size of marks: "))
#     # for k in range(size_of_marks):
#
#     marks = int(input("enter student marks: "))
#     name_and_marks[names] = marks

# print(name_and_marks)

# using user input to take nested dictionary
# information of abk


# nested_dictionary = {}

# size = int(input("enter the size of nested dictionary: "))
# for x in range(size):
#     dict_name = input("enter the name of nested_dict: ")
#     if dict_name == 'employees':
#         number_of_info = int(input('enter the size of dictionary: '))
#         for y in range(number_of_info):
#             emp_name = input("enter name of employee: ")
#             age = int(input("enter age of employee: "))
#             gender = input("enter employee gender: ")
#             nested_dictionary["name"] = emp_name
#             nested_dictionary["age"] = age
#             nested_dictionary["gender"] = gender
#             print(nested_dictionary)
#
#     elif dict_name == "branches":
#         with open("storeinfo.txt", mode="w") as branches:
#             .write(branches)
#             branch_name = input("name of branch: ")
#             town = input("city located: ")
#             year_established = input("year of establishment: ")
#             nested_dictionary["branch name"] = branch_name
#             nested_dictionary["town"] = town
#             nested_dictionary["established year"] = year_established
#             print(nested_dictionary)
#         branches.close()


# taking user input in a sublist and store it in a main_list

# main_list = []
# sub_list = []
# no_of_sublist = int(input('how many sub lists would you like to create?  '))
#
# for a_list in range(no_of_sublist):
#     specific_list = int(input("would you like to create a different list?  "))
#     if specific_list == 1:
#         value_size = input("how many values to store:  ")
#
#     for value in value_size:
#         #if len(specific_list) < value_size:
#             sub_list = specific_list
#             values = input("key in values:  ")  # .split(',')
#     #sub_list.append(values)
#     main_list.append(sub_list)
#     print(sub_list)
# print(main_list)

# above code not working as expected
# try a different approach

# declaring the control variables

# main_list = []
# inner_list = []
#
# no_subLists = int(input("number of sub lists:  "))
# for x in range(no_subLists):
#     number_of_values = int(input("number of values in this sub list:  "))
#     for n in range(number_of_values):
#
#         values = input("enter values to inner list: ").split(',')
#
#         inner_list.append(values)
#
#         main_list.append(inner_list)
#
#         print(inner_list)
# print(main_list)


# calculating percentage
# store students name and marks n a dictionary and calculate the average of the marks

# names = ""
# marks = []
# name_and_marks = {}
#
# for x in range(5):
#     names = input("students names: "  )
#     marks = input("students marks:  ").split(',')
#     name_and_marks[names] = marks
#     print(f"{name_and_marks}")
#     for key, value in name_and_marks.items():
#         print(f"{key}: {value}")

# storing values in a list in python trying my hands in sa form of a dictionary
# name, *marks = input('name and marks:  ').split(',')
# print(name, marks)

# now lets d the real coding
# nu_of_iterations = int(input("number of students:  "))
# students_info = {}

# for x in range(nu_of_iterations):
#     name, *line = input("name and corresponding marks:  ").split()
#     marks = list(map(float, line))
#     students_info[name] = marks


# calculating the average percentage
# query_name = input("enter student name:  ")
# count = 0
# lening = 0
#
# for iter_var in students_info:
#     if iter_var == query_name:
#         #for iter_var in students_info[query_name]:
#         count += iter_var
#         lening += 1
#         average = count/lening
# print(average)

# query_name = input()
# if query_name in students_info:
#     average = sum(students_info[query_name])/len(students_info[query_name])
#     print(f'{average:.2f}')
# print(students_info)
#

# dealing with lists
# my_list = []
# my_list.append(1)
# my_list.append(23)
# my_list.append(55)
# my_list.append(100)
# my_list.append(124)
# my_list.append(200)
# print(my_list)
# my_list.insert(3, 50)
# my_list.insert(4, 50)
# my_list.insert(5, 50)
# my_list.insert(6, 50)
# my_list.insert(7, 50)
# print(my_list)
#
# my_list.pop(5)
# print(my_list)
# my_list.pop(2)
# my_list.remove(23)
# print(my_list)
# my_list.pop(1)
# print(my_list)
# my_list.count(100)
# print(my_list)
# my_list.reverse()
# print(my_list)
# my_list.copy()
# print(my_list)
# my_list.clear()
# print(my_list)

# swap case project
# str_to_swap = str("Www.HackerRank.com")
# for x in range(len(str_to_swap)):
#     if str_to_swap[x].islower():
#         str_to_swap[x] == str_to_swap[x].upper()
#     elif str_to_swap[x].isupper():
#         str_to_swap[x] == str_to_swap[x].lower()
# print(str_to_swap)

# # code didnt work lets try this
# s = "Www.HackerRank.com"
# for x in s:
#     if x.lower:
#         x += s
#
#     else:
#         x.isupper
#         x += s
# print(s)
#
# # lets try this
#


#s = input('enter a string to swap:  ')


# def swap_case(s):
#     sequence = list(s)
#     for i in range(len(sequence)):
#         if sequence[i].islower():
#             sequence[i] = sequence[i].upper()
#         elif sequence[i].isupper():
#             sequence[i] = seequence[i].lower()
#     return str(''.join(sequence))

# split and join a string
# my_str = input('enter a string:  ')
# my_str = "ghana is a great nation"
# my_str_split = my_str.split(sep=",")
# print(my_str_split)
# joining = "_".join(my_str_split)
# print(joining)

# # print your first name and last name
# f_name = input("enter your first name: ")
# l_name = input("enter your last name: ")
# full_name = f_name, l_name
# print(f"hell {full_name} you just delve into python")


# using a function to achieve this
# def full_name_func():
#     first = input("enter first name: ")
#     last = input("enter last name: ")
#     full_name = first, last
#     return full_name
#
#
# print(f"hello {full_name_func()} you just delve into python")

# mutation project change a character in a string
# my_string = "ibrahim"
# to_list = list(my_string)
# print(to_list)
# print(to_list[2])
# to_list[3] = 'traore'
# print(to_list)
#

# search for a sub string among a string
# my_string = "i enjoy taking banku with soup and banku with okro stew"
# lists = list(my_string.split(' '))
# for index, string in enumerate(lists):
#     print(index, string, end='=')
#     double = ''
# for x in my_string:
#     if x == double:
#         x += double
#         print(double, end=' ')

# my_string = "i enjoy taking banku with soup and banku with okro stew"
# double = ''
# for word in range(len(my_string)):
#     if double == word:
#         double += my_string
#         print(word)


# def count_substring(string, sub_string):
#     count = 0
#     flag = False
#     for c in range(len(string)):
#         if string[c] == sub_string[0]:
#             flag = True
#             for i in range(len(sub_string)):
#                 if c + i < len(string):
#                     if string[c + i] == sub_string[i] and flag == True:
#                         flag = True
#                     else :
#                         flag = False
#                 else:
#                     flag = False
#         if flag == True:
#             flag = False
#             count = count + 1
#     return count

#
# # matrix in python
#
# # declaring a matrix
# # this is a 4 by 5 matrix
# my_matrix = [[1, 2, 3, 4, 5],
#           [6, 7, 8, 9, 10],
#           [11, 12, 13, 14, 15],
#           [16, 17, 18, 19, 20]]
#
# print(my_matrix[0][4])
# print(my_matrix[0])
#
#
# # taking user input to form a matrix
# row = int(input("enter row: "))
# column = int(input("enter column: "))
# matrix = []
# # for user input
# a for lop for row entries
# for row in range(row):
#     a = []
# # a for loop for column entries
#     for column in range(column):
#         a.append(int(input('enter: ')))
#         matrix.append(a)
# # for printing the matrix
# for row in range(row):
#     for column in range(column):
#         print(matrix[row][column], end='')
#         print()

# # taking multiple inputs at a time
# a, b, c = input("enter three values at a time:").split()
# print('enter your first number', a)
# print('enter your second number', b)
# print('enter your third number:', c)
# print()
#
# # taking students info
#
# x, y, z = input("enter the students info: ").split()
# print("students name :", x)
# print("students class:, ", y)
# print("students gender:", z)
#
#
# # using the building format function in python
# m, n, o = input("enter the students id number: ").split()
# print("students name :", m)
# print("students class:, ", y)
# print("students gender:", z)
#
# print("student id one is {}, student id two is {}, student id three is {}".format(m, n, o))
# row = int(input('enter number of rows: '))
# matrix = []
# count = row
#
# for x in range(row):
#     rows = list(map(int, input('enter elements: ').split()))
#     matrix.append(rows)
#     print(rows)
#
# print(matrix)
#

# using chainmaps in python
# chainmaps is used to link multiple variables in python

# from collections import ChainMap
# dictionary_1 = {'name': 'kofi', 'age': 20, 'class': 5}
# dictionary_2 = {'letter': 'a', 'word': 'man', 'number': 10}
# dictionary_3 = {'town': 'winneba', 'city': 'accra', 'village': 'nkonya'}
# all_dicts = ChainMap(dictionary_1, dictionary_2, dictionary_3)
# print('printing all dictionaries')
# print(all_dicts)
# print()
#
# # adding a new value to the dictionary by using the .new_child function
# dictionary_4 = {'new': 1, 'new2': 2, 'new3': 3}
# new_all_dicts = all_dicts.new_child(dictionary_4)
# print(" adding a dictionary to the collection of dictionaries")
# print(new_all_dicts)
# print()
#
# # working with reverse function in chainmap
# # dictionary_1.maps = reversed(dictionary_1.maps)
# # print(dictionary_1.maps)
#
#
# # merging the dictionaries with the | operator
# merging = dictionary_1 | dictionary_2
# print("merging two dictionaries into one dictionary")
# print(merging)
# print()
#
# print('printing all dictionary keys and values')
# print(dictionary_1.keys())
# print(dictionary_1.values())
# print()
#

# python set exercises
# 1 given a python list write a program to add all its elements into a given set
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# empty_set = set()
# for x in list_1:
#     empty_set.add(x)
# print(empty_set)
#
# # 2 return a new set of identical items from two given sets
# set_1 = {10, 20, 30, 40, 50, 60}
# set_2 = {50, 60, 70, 80, 90, 100}
# common_members_1 = set_1.intersection(set_2)
# common_members_2 = set_1 & set_2
# print(common_members_1)
# print(common_members_2)
# print()
#
# # 1 get only unique items from two sets
#
# set_1 = {10, 20, 30, 40, 50, 60}
# set_2 = {50, 60, 70, 80, 90, 100)
# diff_1 = set_1-set_2
# diff_2  = set_1.difference(set_2)
# print(diff_1)
# print(diff_2)
# print()


# singly linkedlist in python

#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next_node = None
#
#
# # creating nodes
# node1 = Node("node1")
# node2 = Node("node2")
# node3 = Node("node3")
# node4 = Node("node4")
# node5 = Node("node5")
#
# # connecting nodes
# node1.next_node = node2
# node2.next_node = node3
# node3.next_node = node4
# node4.next_node = node5
#
# # traversing through node
# # printing node data
#
#
# current_node = node1
#
# if current_node is None:
#     print("linked list is empty")
#
# while current_node is not None:
#     print(current_node.data)
#     current_node = current_node.next_node
#
# if current_node is None:
#     print("no more available nodes")

# now lets follow a proper algorithm for traversing through single linked list in python
# define a class

#
# class NodePractices:
#     def __init__(self, data):
#         self.data = data
#         self.reference = None
#
#         class LinkedList():
#             def __init__(self):
#                 self.head = None
#
#             # now lets create a function to traverse through the lists
#             def print_all_linked_data(self):
#
#                 # check if there is dat or not
#                 if self.head is None:
#                     print("linked list is empty")
#
#                 else:
#                     current_list = self.head
#                     while current_list is not None:
#                         print(current_list.data)
#                         current_list = current_list.reference
#
#
# # no lets create a linked list
# l_list1 = NodePractices()
# l_list1.print_all_linked_data()

# creating another example


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.reference = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#         # traversing through the list
#     def print_link_list(self):


# arranging nodes

class Node:
    def __init__(self, data, next_n):
        self.data = data
        self.next_n = next_n


class LinkedList:
    def __init__(self):
        self.head = None

    def arranging(self):
        runner = self.head
        hopper = self.head
        results = []

        if runner is None:
            return

        while runner:
            runner = runner.next_n

            while hopper:
                hopper = hopper.next_n

                if hopper.data < runner.data:
                    results.append(hopper.data)
                hopper = hopper.next_n

        runner = runner.next_n

        return results


# create instance of the class and create a linkedlist
linkedlist = LinkedList()
node1 = Node(3)
node2 = Node(5)
node3 = Node(4)
node4 = Node(1)
node5 = Node(2)

# linking the nodes
node1.next_n = node2
node2.next_n = node3
node3.next_n = node4
node4.next_n = node5

# set the head of the list
linkedlist.head = node1
# calling the function
results = LinkedList.arranging()

# displaying the results
print("arranged list is", results)




































