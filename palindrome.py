class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        zero = 0
        while x > zero:
            zero = (zero * 10) + (x%10)
            x = x//10
        return x == zero or x == zero //10