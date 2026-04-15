"""Given an integer array nums, return an array answer 
where answer[i] is the product of all elements except nums[i].
 You must solve it in O(n) time and without using division.

Example 1:
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Example 2:
Input:  nums = [−1, 1, 0, −3, 3]
Output: [0, 0, 9, 0, 0]"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        answer=[1]*n
        lp=1
        for i in range(n):
            answer[i]=lp
            lp*=nums[i]
        rp=1
        for i in range(n-1, -1, -1):
            answer[i]*=rp
            rp*=nums[i]
        return answer
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    sol = Solution()
    result = sol.productExceptSelf(nums)
    print(result)  # [24, 12, 8, 6]
