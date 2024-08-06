def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs: 
            # Letter by index, frequency by value
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1 
            res[tuple(count)].append(s) 