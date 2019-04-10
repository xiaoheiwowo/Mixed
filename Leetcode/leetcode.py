class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_pos = {}
        left = 0
        ret = 0
        for i in range(len(s)):
            if s[i] in char_pos:
                left = max(left, char_pos[s[i]] + 1)
            ret = max(ret, i - left + 1)
            char_pos[s[i]] = i
        return ret


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(''), 'ans:0')
    print(Solution().lengthOfLongestSubstring(' '), 'ans:1')
    print(Solution().lengthOfLongestSubstring('au'), 'ans:2')
    print(Solution().lengthOfLongestSubstring('abba'), 'ans:2')
    print(Solution().lengthOfLongestSubstring('abcabc'), 'ans:3')
    print(Solution().lengthOfLongestSubstring('tmmasdftttt '), 'ans:6')
    print(Solution().lengthOfLongestSubstring('pwwkew'), 'ans:3')
