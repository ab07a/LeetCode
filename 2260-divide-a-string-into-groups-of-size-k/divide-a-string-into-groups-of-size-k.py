class Solution(object):
    def divideString(self, s, k, fill):
        if len(s)%k !=0:
            s+=fill*(k-len(s)%k)
        sol = []
        for i in range(len(s)):
            if i%k == 0:
                sol.append(s[i])
            else:
                sol[-1]+=s[i]
        return sol
        