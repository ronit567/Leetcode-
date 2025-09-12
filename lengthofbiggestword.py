class Solution(object):
    def lengthOfLastWord(self, s):
        counter = 0 
        word_length = []
        for i in s:
            if s == "" and counter >= 1:
                word_length.append(counter)
            if s != "":
                counter += 1 

        if not word_length:
            return ""
        
        return max(word_length)
        

            


