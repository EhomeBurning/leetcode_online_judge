# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Example 1:
# Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

# Example 2:
# Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, 
# and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)

# Company Tags LinkedIn
# Tags Depth-first Search
# Similar Problems (M) Nested List Weight Sum II


class Solution(object):
	def depthSum(self, nestedList):
        if len(nestedList) == 0: return 0
        stack = []
        sum = 0
        for n in nestedList:
            stack.append((n, 1))
        while stack:
            next, d = stack.pop(0)
            if next.isInteger():
               sum += d * next.getInteger()
            else:
                for i in next.getList():
                    stack.append((i,d+1))
        return sum





