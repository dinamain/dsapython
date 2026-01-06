"""Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2"""
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        seen = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in seen:
                count += seen[prefix_sum - k]

            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return count
if __name__ == "__main__":
    nums = [1,1,1]  # test input
    k = 2
    sol = Solution()     # create object
    result = sol.subarraySum(nums,k)
    print("subarraySum:", result)




