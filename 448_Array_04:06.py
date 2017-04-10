# Google 
# same element
# 


# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? 
# You may assume the returned list does not count as extra space.
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [5,6]


# ############################# First dummy Thought ########################################
# class Solution(object):

# 	num = []

# 	def findDisappearedNumbers(self, nums):
# 		full = []
# 		missing = []
# 		# corner case
# 		if len(nums) == 0: 
# 			return []

# 		n = len(nums)
# 		# create full list
# 		for i in range(n):
# 			full.append(i+1)

# 		for i in full:
# 			if i not in nums:
# 				missing.append(i)

# 		return missing


# Test = Solution()
# print(Test.findDisappearedNumbers())
############################### Time Limit Exceed ###########################################

######
class Solution(object):
	def findDisappearedNumbers(self, nums):
		for i in range(len(nums)):
			index = abs(nums[i]) - 1
			nums[index] = - abs(nums[index])

		return [i + 1 for i in range(len(nums)) if nums[i] > 0]
Test = Solution()
print(Test.findDisappearedNumbers([4,1,1,1]))





