# Ryan Keller
#
# AoC Day 1 Problem 2
#

def firstduplicate(filename):
    fp = open(filename, 'r')
    total = 0 # running total
    seen = {total : 1} # hashmap of seen numbers (0 is added b/c we start at 0)
    line = fp.readline()
    while (1): # keep reading until a duplicate is found,
               # even if it takes multiple reads of the input
        while (line != ""):
            sign = line[0] 
            rest = line[1:]
            if (sign == "+"):
                total = total + int(rest)
                if (total in seen): # if we repeat a total, we are done
                    fp.close()
                    return total
                else:
                    seen[total] = 1
            elif (sign == "-"):
                total = total - int(rest)
                if (total in seen):
                    fp.close()
                    return total
                else:
                    seen[total] = 1
            else: # if there is a 0, the total repeats
                fp.close()
                return total
            line = fp.readline()
        # if we read the whole input and don't find a duplicate,
        # we need to loop again
        fp.close()
        fp = open(filename, 'r')
        line = fp.readline()

def main():
    print firstduplicate("input.txt")

if __name__ == "__main__":
    main()
        
    
