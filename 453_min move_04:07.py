# Indeed Coursera

# Take the opposite: decrease once except the minimun one  

# Given a non-empty integer array of size n, find the minimum number of moves 
# required to make all array elements equal, where a move is incrementing 
# n - 1 elements by 1.

# Example:

# Input:
# [1,2,3]

# Output:
# 3

# Explanation:
# Only three moves are needed (remember each move increments two elements):

# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

########################### First Dummy Thought ##########################
class Solution(object):
	def minMoves(self, nums):
		if(len(set(nums)) == 1):
			return 0
		sum = 0
		n = len(nums)
		for number in nums:
			sum += number

		for i in range(1,n+1):
			total = sum + (n-1)*i
			if total%n == 0:
				return i


Test = Solution()
print(Test.minMoves([1,34]))
############################ Solution Below ############################
class Solution(object):
	def minMoves(self, nums):
		return sum(nums) - min(nums) * len(nums)