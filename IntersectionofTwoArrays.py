"""Given two integer arrays nums1 and nums2, return an array of 
their intersection. Each element in the result must be unique 
and you may return the result in any order.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted."""
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        num1set=set(nums1)
        num2set=set(nums2) 
        count=0
        inter=[]
        for i in num1set:
            if i in num2set:
                inter.append(i)
        return inter 
if __name__=="__main__":
    nums1 = [1,2,2,1]   # test input
    nums2 = [2,2]
    sol = Solution()     # create object
    result = sol.intersection(nums1,nums2)

    print("intersection:", result) 
    
"""class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))
"""