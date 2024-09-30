# https://leetcode.com/problems/longest-repeating-character-replacement

# substring 길이 - 최대 갯수 >= k 임을 알았어야 풀 수 있었음.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 딱 k번 바꿀 수 있음.
        
        l = r = 0
        counter = collections.Counter()

        for r in range(0, len(s)) : 
            counter[s[r]] += 1
            max_char, max_char_n = counter.most_common(1)[0]

            if r-l+1 - max_char_n > k :
                counter[s[l]] -= 1
                l += 1

        return r+1-l

