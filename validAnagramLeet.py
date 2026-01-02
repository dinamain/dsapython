"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count={}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        for ch in t:
            if ch not in count:
                return False
            count[ch]-=1
            if count[ch]<0:
                return False
        return True



if __name__ == "__main__":
    s="cat"  # test input
    t="rat"
    sol = Solution()     # create object
    result = sol.isAnagram(s,t)
    print("isAnagram:", result)