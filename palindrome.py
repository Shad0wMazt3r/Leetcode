def isPalindrome( x ):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)[::-1]
        if str(y) == str(x):
            return True
        else:
            return False


print(isPalindrome(121))
print(isPalindrome(123))
