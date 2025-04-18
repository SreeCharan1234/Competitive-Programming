class Solution:
    def countAndSay(self, n: int) -> str:
        d={}
        def convert(s):
            if not s:
                return ""
            
            result = ""
            count = 1
            
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    result += str(count) + s[i - 1]
                    count = 1
            
            # Add the last run
            result += str(count) + s[-1]
            return result
        def ans(i):
            if i=="1":
                return "1"
            if i in d:
                return d[i]
            else:
                d[i] =convert(ans(str(int(i)-1)))
            return d[i]
        return ans(str(n))