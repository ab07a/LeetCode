class ProductOfNumbers(object):

    def __init__(self):
        self.l = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not num:
            self.l = [1]
        else:
            self.l.append(self.l[-1]*num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k>=len(self.l):
            return 0
        return (self.l[-1]//self.l[-k-1])
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)