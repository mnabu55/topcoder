from typing import List, Tuple, Optional


class EllysPalMulDiv2:
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
        for y in range(1, 1001):
            x_product_y = X * y
            if self.isPalindrome(x_product_y):
                foundPalindrome = True
                break

        if not foundPalindrome:
            y = -1

        return y

ins = EllysPalMulDiv2()
assert ins.getMin(42) == 6, "ERROR x=42, y=6"
assert ins.getMin(121) == 1, "ERROR x=121, y=1"
assert ins.getMin(1337) == 143, "ERROR x=121, y=1"
assert ins.getMin(13) == 38, "ERROR x=121, y=1"
assert ins.getMin(100) == -1, "ERROR x=121, y=1"
assert ins.getMin(39325) == -1, "ERROR x=121, y=1"
