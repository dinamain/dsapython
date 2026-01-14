"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:
Input: nums = [1,0,1,2]
Output: 3"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset=set(nums)
        max_count = 0
        for num in numset:
            if num-1 not in numset:
                current=num
                count=1
                while current+1 in numset:
                    current+=1
                    count+=1
                max_count = max(max_count, count)
        return max_count

if __name__ == "__main__":
    nums = [0,3,7,2,5,8,4,6,0,1]
    sol = Solution()     # create object
    result = sol.longestConsecutive(nums)
    print("longestConsecutive:", result)