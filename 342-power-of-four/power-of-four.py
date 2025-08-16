
class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        sol = (math.log(n)/math.log(4))
        return floor(sol) == sol
        