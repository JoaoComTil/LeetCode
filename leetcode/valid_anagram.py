
# ------------ Minha solução -------------
class Solution(object):
    def isAnagram1(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        
        alfabeto1 = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }
        alfabeto2 = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }

        for i in s:
            alfabeto1[i] += 1
        for i in t:
            alfabeto2[i] += 1

        if alfabeto1 == alfabeto2:
            return True
        else:
            return False

# ------------- Solução oficial ------------------                
    def isAnagram2(self, s, t):

        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        alfabeto = {}

        for c in s:
            if c in alfabeto:
                alfabeto[c] += 1
            else:
                alfabeto[c] = 1

        for c in t:
            if c not in alfabeto:
                return False

            alfabeto[c] -= 1

            if alfabeto[c] < 0:
                return False

        return True
                
s = "racecar"
t = "cararc"  
sol = Solution()
print(sol.isAnagram2(s,t))