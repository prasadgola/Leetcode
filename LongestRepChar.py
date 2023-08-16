class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        max_count = 0  # Keep track of the maximum frequency in the window
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_count = max(max_count, count[s[r]])

            # If the window is not valid, shrink it
            while (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1
                # Update max_count since the character count has changed
                max_count = max(count.values())

            res = max(r - l + 1, res)

        return res