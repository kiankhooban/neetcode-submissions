class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        letters = {}

        for i in strs:
            key = "".join(sorted(i))
            if key not in letters:
                letters[key] = []
            letters[key].append(i)
        
        return list(letters.values())