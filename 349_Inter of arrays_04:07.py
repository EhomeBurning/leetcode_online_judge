# Given two arrays, write a function to compute their intersection.

# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

# Note:
# Each element in the result must be unique.
# The result can be in any order.
# Company Tags Two Sigma
# Tags Binary Search Hash Table Two Pointers Sort
# Similar Problems (E) Intersection of Two Arrays II
class Solution(object):
    def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    for i in nums1:
        if i not in res and i in nums2:
            res.append(i)
    
    return res