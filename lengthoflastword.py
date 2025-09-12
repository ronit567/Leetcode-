class Solution(object):
    def lengthOfLastWord(self, s):
        counter = 0 
        word_length = []
        for i in s:
            if  i == " " and counter >= 1:
                word_length.append(counter)
                counter = 0
           
            if i != " ":
                counter += 1 
        
        if counter > 0:
            word_length.append(counter)

        if not word_length:
            return ""
        
        return word_length[-1]        

            


