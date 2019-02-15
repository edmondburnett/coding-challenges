# Challenge #59 [easy]
# http://redd.it/uh033


def isIn(str1, str2):
    """
    Given two strings, find out if the second string is contained
    somewhere in the first. If it is, return it's position.
    """
    if str2 in str1:
        pos = len(str2)
        for i in range(len(str1)):
            if str1[i:pos] == str2:
                return i
            pos += 1
    else:
        return False


print isIn('Generic String For Testing Purposes', 'ring')
