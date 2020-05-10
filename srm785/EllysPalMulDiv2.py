class EllysPalMulDiv2:
    MAX_Y = 1000

    def isPalindrome(self, target):
        target_string = str(target)
        reverse_string = target_string[::-1]
        reverse = int(reverse_string)

        if target == reverse:
            judge = True
        else:
            judge = False

        return judge

    def getMin(self, X):
        foundPalindrome = False

        # 1 <= y <= 1000
        for y in range(1, self.MAX_Y + 1):
            x_product_y = X * y
            if self.isPalindrome(x_product_y):
                foundPalindrome = True
                break

        if not foundPalindrome:
            y = -1

        return y

ins = EllysPalMulDiv2()
assert ins.getMin(42) == 6, "ERROR when x=42, should return 6"
assert ins.getMin(121) == 1, "ERROR when x=121, should return y=1"
assert ins.getMin(1337) == 143, "ERROR when x=121, should return y=1"
assert ins.getMin(13) == 38, "ERROR when x=121, should return y=1"
assert ins.getMin(100) == -1, "ERROR when x=121, should return y=1"
assert ins.getMin(39325) == -1, "ERROR when x=121, should return y=1"
