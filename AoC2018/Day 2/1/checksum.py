# Ryan Keller
#
# AoC Day 2 Problem 1
#

def checksum(filename):
    fp = open(filename, 'r')
    two = 0 # num of words with two latters
    three = 0 # num words with three letters
    line = fp.readline()
    while (line != ""):
        twoflag = False
        threeflag = False
        letters = {} # letters are counted in a hashmap
        for letter in line:
            if (letter in letters): # if we've seen this letter, increment the count
                letters[letter] += 1
            else: # else add letter to hashmap with count 1
                letters[letter] = 1
        for key in letters.keys():
            if (letters[key] == 3):
                if not threeflag: # check if any letters have count = 3
                    threeflag = True
            elif (letters[key] == 2):
                if not twoflag: # check if any letters have count = 2
                    twoflag = True
            if ((twoflag) & (threeflag)): break # we can stop checking if we find both
        if (twoflag): two += 1
        if (threeflag): three += 1
        line = fp.readline()
    fp.close()
    return (two * three)

def main():
    print checksum("input.txt")

if __name__ == "__main__":
    main()     
            
            
