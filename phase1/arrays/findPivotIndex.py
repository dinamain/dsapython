"""Given an array nums, return the pivot index — 
the index where the sum of all numbers to the left 
equals the sum of all numbers to the right. 
If no such index exists, return -1. 
If there are multiple, return the leftmost one.

Example 1:
Input:  nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: left sum = 1+7+3 = 11, right sum = 5+6 = 11 ✅

Example 2:
Input:  nums = [1, 2, 3]
Output: -1

Example 3:
Input:  nums = [2, 1, -1]
Output: 0
Explanation: left sum = 0 (nothing to left), right sum = 1+(-1) = 0 ✅"""


class Solution:
    def prefixfind(self,nums: list[int]) -> list[int]:
        leftsum=0
        total=sum(nums)
        for i in range(len(nums)):
            right_sum = total - leftsum - nums[i]
            if leftsum==right_sum:
                return i
            leftsum=leftsum+nums[i]
        return -1
if __name__=="__main__":
    nums= [1, 7, 3, 6, 5, 6]
    sol=Solution()
    result=sol.prefixfind(nums)
    print(result)
    
    