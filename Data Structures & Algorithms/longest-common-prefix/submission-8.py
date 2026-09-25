class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefixes = list(strs[0])
        
        for s in strs:
            if s == "":
                prefixes.clear()
                break

            for i, w in enumerate(s):
                if i >= len(prefixes) or w != prefixes[i]:
                    prefixes = prefixes[:i]
                    break
            
            if len(s) < len(prefixes):
                prefixes = prefixes[:len(s)]

        
        prefix = "".join(prefixes)

        return prefix