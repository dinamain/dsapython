"""Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]"""
# class Solution:
#     def runningSum(self, nums: list[int]) -> list[int]:
#         sum=0
#         sumlist=[]
#         for i in range(len(nums)):
#             sum=sum+nums[i]
#             sumlist.append(sum)
#         return sumlist
        
# if __name__=="__main__":
#     nums = [1,2,3,4]
#     sol=Solution()
#     result=sol.runningSum(nums)
#     print("Running Sum:",result)

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        running=0
        result=[]
        for num in nums:
            running+=num
            result.append(running)
        return result
        
if __name__=="__main__":
    nums = [1,2,3,4]
    sol=Solution()
    result=sol.runningSum(nums)
    print("Running Sum:",result)

# In-place version (O(1) extra space)
# class Solution:
#     def runningSum(self, nums: list[int]) -> list[int]:
#         for i in range(1, len(nums)):
#             nums[i] += nums[i - 1]
#         return nums


# 🔸 Use this only when asked about space optimization.