class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        org = []
        reverse = []

        for i in range(len(str(s))):
            org.append(s[i])

        for j in range(len(str(s))-1,-1,-1):
            reverse.append(s[j])

        if org == reverse: 
            return True
        return False

