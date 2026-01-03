"""Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:
Input: s = "abcaaba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        l=0
        r=len(s)-1
        while l<r:
            if s[l] != s[r]:
                return is_pal(l+1, r) or is_pal(l, r-1)
            l+=1
            r-=1
        return True

if __name__=="__main__":
    s="abc"
    sol=Solution()
    result=sol.validPalindrome(s)
    print("isPalindrom:", result)