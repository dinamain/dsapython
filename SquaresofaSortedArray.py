"""Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]"""

# class Solution:
#     def sortedSquares(self, nums: list[int]) -> list[int]:
#         sq=[]
#         for num in nums:
#             sq.append(num*num)
#             sq.sort()
#         return sq

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1  # fill result from the end

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1

        return result


if __name__ == "__main__":
    nums = [-4,-1,0,3,10]  # test input
    sol = Solution()     # create object
    result = sol.sortedSquares(nums)
    print("sortedSquares:", result)