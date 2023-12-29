class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s2t = {}
        t2s = {}
        for i in range(len(s)):
            if s[i] not in s2t:
                if t[i] in t2s:
                    return False
                s2t[s[i]] = t[i]
                t2s[t[i]] = s[i]
            else:
                if s2t[s[i]] != t[i]:
                    return False
        return True
