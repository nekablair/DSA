# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


# prep
# parameter:array of integers and target
# return: indices of 2 numbers that add up to target, or a two digit tuple
# example:nums = [3,2,4], target = 6 --> [0, 1]
# pseudocode:
# - iterate over list
# -compare one element with another to see if they equal the target
# -once found, add both indices of values to tuple and return

nums = nums = [2,7,11,15]
target = 9

# class Solution:
def twoSum(nums, target):
    result = []
    for i in range(len(nums)):
            # print(i)
        for j in range(i+1, len(nums)):
                # print(j, item)
                # print(nums[i], nums[j])
            if nums[i] + nums[j] == target:
                result.extend([i, j])
    return result
    
print(twoSum(nums, target)) #--> [0,1]
