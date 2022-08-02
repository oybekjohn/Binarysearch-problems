def palindromic_nums(num):
    """ 
    Given a non-negative integer num, return whether it is a palindrome.
    Bonus: Can you solve it without using strings?
    """
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


print(palindromic_nums(1213121))