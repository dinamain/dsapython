"""Given a sorted array nums, remove duplicates in-place so each element appears only once. 
Return the number of unique elements. The relative order must be kept.

Example 1:
Input:  nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]

Example 2:
Input:  nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]"""
class Solution:
    def containsDuplicates(self, nums: list[int]) -> bool:             
        #return len(set(nums)) != len(nums)
        setnum=set()
        for num in nums:
            if num in setnum:
                return True
            setnum.add(num)
        return False
    
if __name__=="__main__":
    nums=[1,1,2]
    sol=Solution()
    result=sol.containsDuplicates(nums)
    print(result)