# nums = [2, 7, 11, 15]
# target = 9

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j] == target:
#             print([i, j])
"""If:
nums[i] + nums[j] = target
Then:
nums[j] = target - nums[i]
👉 While looping:
Check if target - current_number already exists"""
# number -> index
# Dictionary lookup is O(1) (very fast)
# We need indices, not just values
def findd(nums,target):
    seen={}
    for i,num in enumerate(nums):
        needed=target-num
        if needed in seen:
            return [seen[needed], i]
        seen[num]=i
"""enumerate(nums) lets you loop over a list and get BOTH:
the index
the value
at the same time.
[2, 7, 11, 15]
into this:(0, 2), (1, 7), (2, 11), (3, 15)"""
       
"""PATTERN YOU JUST LEARNED

✔️ Hashing for lookup
✔️ One-pass solution
✔️ Complement technique"""