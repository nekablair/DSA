// # 1. Two Sum
// # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// # You may assume that each input would have exactly one solution, and you may not use the same element twice.

// # You can return the answer in any order.

// # Example 1:

// # Input: nums = [2,7,11,15], target = 9
// # Output: [0,1]
// # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// # Example 2:

// # Input: nums = [3,2,4], target = 6
// # Output: [1,2]
// # Example 3:

// # Input: nums = [3,3], target = 6
// # Output: [0,1]
 
// # Constraints:

// # 2 <= nums.length <= 104
// # -109 <= nums[i] <= 109
// # -109 <= target <= 109
// # Only one valid answer exists.
 
// # Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

// # prep
// # parameter:array of integers and target
// # return: indices of 2 numbers that add up to target, or a two digit tuple
// # example:nums = [3,2,4], target = 6 --> [0, 1]
// # pseudocode:
// # - iterate over list
// # -compare one element with another to see if they equal the target
// # -once found, add both indices of values to tuple and return

numArr = [3,2,4]
target = 4

function findIndices(numArr, target) {
    // console.log(numArr, target)
    let indexArr = []
    for (let i = 0; i < numArr.length; i++) {
        // console.log(i)
        // console.log(numArr[i])
        for (let j = i + 1; j < numArr.length; j++) {
            // console.log(numArr[i], numArr[j])
            if (numArr[i] + numArr[j] == target) {
                indexArr.push(i,j)
                return indexArr
            }
            
        }
    }
    return indexArr
    
}

console.log(findIndices([1, 8, 3, 0, 9], 9)) // [0, 1]