"""Given an array of integers nums and an integer target, 
return the indices of the two numbers that add up to target.
You may assume exactly one solution exists. 
You cannot use the same element twice.

Example 1:
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Example 2:
Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i, num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return [seen[complement], i]
            seen[num]=i

if __name__=="__main__":
    nums=[2, 7, 11, 15]
    target=9
    sol=Solution()
    result=sol.twoSum(nums, target)
    print("2sum:", result)
        