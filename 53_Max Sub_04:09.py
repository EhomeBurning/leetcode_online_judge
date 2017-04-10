# Find the contiguous subarray within an array (containing at least one number) 
# which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# click to show more practice.

# Hide Company Tags LinkedIn Bloomberg Microsoft
# Hide Tags Array Dynamic Programming Divide and Conquer
# Hide Similar Problems (E) Best Time to Buy and Sell Stock (M) Maximum Product Subarray


class Solution(object):
	def maxSubArray(self, nums):
		if not nums:
			return 0

		cur_sum = max_sum = nums[0]
		for num in nums[1:]:
			cur_sum = max(num, cur_sum + num)
			max_sum = max(cur_sum, max_sum)
		return max_sum