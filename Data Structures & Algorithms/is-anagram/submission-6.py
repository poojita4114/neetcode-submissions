class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}
        if len(s)==len(t):
            for char in s:
                if char not in s_dict:
                    s_dict[char]=1
                else:
                    s_dict[char]+=1
            for char in t:
                if char not in t_dict:
                    t_dict[char]=1
                else:
                    t_dict[char]+=1
            for key, val in s_dict.items():
                if key not in t_dict or s_dict[key] != t_dict[key]:
                    return False
            return True
        else:
            return False