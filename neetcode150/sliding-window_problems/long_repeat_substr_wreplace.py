    """def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        longest = max_freq = L = 0

        for R in range(len(s)):
            window_len = R - L + 1
            while (window_len) - max_freq > k:
                hmap[s[L]] -= 1
                L += 1
            if s[R] not in hmap:
                hmap[s[R]] = 1
            else:
                hmap[s[R]] += 1
                if hmap[s[R]].value() > max_freq:
                    max_freq = hmap[s[R]].value()
            if 
        return longest
    """
