# Amazon


# Given an array of integers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, 
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2


class Solution(object):
	def twoSum(self, numbers, target):
		dic = {}
		for i, num in enumerate(numbers):
			if target-num in dic:
				print("cao")
				return [dic[target-num]+1, i+1]
		dic[num] = i

Test = Solution()
Test.twoSum((2,7,11,15),9)
######################## Method Two #######################################
class Solution(object):
	def twoSum(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
                
Test = Solution()
Test.twoSum((2,7,11,15),9)