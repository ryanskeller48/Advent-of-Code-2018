# Ryan Keller
#
# AoC Day 2 Problem 2
#

def same_letters(str1, str2): # check if two words are one letter off
    index = 0
    newstr = "" # output is the letters that match
    difference_flag = False
    strlen = len(str1)
    while (index < strlen):
        letter1 = str1[index]
        letter2 = str2[index]
        if (letter1 == letter2):
            newstr = newstr + letter1
        else:
            if (difference_flag): return ""
            # if there are two differences, exit and return a blank string
            else:
            # if this if the first difference, don't add the letters and mark tbe flag True
                difference_flag = True
        index += 1
    return newstr

def get_line(index, filename):
    # get line by directly indexing the input file
    # we know each line is equal length --
    # so instead of reading thru the whole file to compare
    # each word to each other word, we can directly get the word we want in 0(1)
    fp = open(filename, 'r')
    line = fp.readline()
    linesize = len(line)
    if (index == 0):
        fp.close()
        return line
    else:
        fp.seek((linesize * index))
        line = fp.read(linesize)
        fp.close()
        return line

def find_near_match(filename):
    index1 = 0 # index of the word we will compare to all others that come after it on the list
    word1 = get_line(index1, filename) # get word by index
    wordlen = len(word1) # words are all equal len
    while (word1 != ""):
        index2 = index1 + 1 
        word2 = get_line(index2, filename) # words that comes after word1 in input list
        while (word2 != ""):
            match = (same_letters(word1, word2)) 
            if (len(match) == wordlen-1): # if match returns a string of wordlen-1, it is a near match
                return match
            else:
                index2 += 1
                word2 = get_line(index2, filename)
        index1 += 1
        word1 = get_line(index1, filename)
    return "No Match!"

def main():
    print find_near_match("input.txt")

if __name__ == "__main__":
    main()     
                 








        
                
