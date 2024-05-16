# Task
# Create a function that always returns True/true for every item in a given list.
# However, if an element is the word 'flick', switch to always returning the opposite boolean value.

# Examples
# ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

# ['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

# ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
# Notes
# "flick" will always be given in lowercase.
# A list may contain multiple flicks.
# Switch the boolean value on the same element as the flick itself.

# PREP 
# parameter:a list
# return:list of booleans
# example: ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]
# pseudocode:
# - iterate over list
# - starting with first item make True
# - once find flick switch to False, all following items same
# - if find another flick switch back to True, all following items same

lst = ['codewars', 'flick', 'code', 'wars']

def bool_list(lst):
    # string_lst = ','.join(lst)
    # print(string_lst)
    # string_lst.replace()
    for i in lst:
        print(i)
        if i == 'flick':
            print(False)
        elif i:
            print(True)
        
        # if i != 'flick':
        #     print(True)


print(bool_list(lst))
# print(bool_list(['burgers', 'fries', 'flick', 'soda']))