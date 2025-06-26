class Solution(object):
    def isValid(self, s):

        d = {")":"(", "]":"[", "}":"{"}
        l = []
        for i in s:
            if i in d:
                if len(l) and l.pop() == d[i]:
                    continue
                return False
            else:
                l.append(i)
        if not len(l):
            return True
        return False
            
                