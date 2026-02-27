"""Pattern

Variable Sliding Window + Hash Map

🧠 Core Idea (simple words)

Expand the window by moving right

Track character frequencies

If distinct characters become more than 2,
→ shrink from the left until valid again

Keep updating the maximum window length"""

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        freq={}
        left=0
        maxlen=0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            while len(freq)>2:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen


if __name__ == "__main__":
    #s = "ccaabbb"
    s = "eceba"
    sol = Solution()     # create object
    result = sol.lengthOfLongestSubstringTwoDistinct(s)
    print("lengthOfLongestSubstringTwoDistinct:", result)