#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].




nums = [2,7,11,15]
target = 9
Minus_dict = {}

def leet_num1():
	if len(nums) <= 1:
		print("Fuck!") 
	for i in range(len(nums)):
		if nums[i] in Minus_dict:
			print([Minus_dict[nums[i]], i])
		else:
			Minus_dict[target - nums[i]] = i

def main():
	leet_num1()

if __name__ == '__main__':
	main()
