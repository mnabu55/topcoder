class EllysPalMulDiv2:
    MAX_Y = 1000

    @staticmethod
    def is_palindrome(target):
        target_string = str(target)
        reverse = int(target_string[::-1])
        return True if target == reverse else False

    def getMin(self, X):
        found_palindrome = False

        for y in range(1, self.MAX_Y + 1):  # 1 <= y <= 1000
            x_product_y = X * y
            if self.is_palindrome(x_product_y):
                found_palindrome = True
                break
        if not found_palindrome:
            y = -1

        return y


ins = EllysPalMulDiv2()
assert ins.getMin(42) == 6, "ERROR when x=42, should return 6"
assert ins.getMin(121) == 1, "ERROR when x=121, should return y=1"
assert ins.getMin(1337) == 143, "ERROR when x=121, should return y=1"
assert ins.getMin(13) == 38, "ERROR when x=121, should return y=1"
assert ins.getMin(100) == -1, "ERROR when x=121, should return y=1"
assert ins.getMin(39325) == -1, "ERROR when x=121, should return y=1"
