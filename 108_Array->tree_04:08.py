# Given an array where elements are sorted in ascending order, 
# convert it to a height balanced BST.

# Hide Company Tags Airbnb
# Hide Tags Tree Depth-first Search
# Hide Similar Problems (M) Convert Sorted List to Binary Search Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def sortedArrayToBST(self, nums):
		"""
		:type nums: List[int]
		:rtype: TreeNode
		"""
		if not nums:
			return None

		mid = len(nums) // 2

		root = TreeNode(nums[mid])
		root.left = self.sortedArrayToBST(nums[:mid])
		root.right = self.sortedArrayToBST(nums[mid+1:])

		return root
