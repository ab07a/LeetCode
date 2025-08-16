class Solution(object):
    def maximum69Number (self, num):
        sol = list(str(num))
        for i in range(len(sol)):
            if sol[i]=='6':
                sol[i] = '9'
                break
        return int("".join(sol))
        