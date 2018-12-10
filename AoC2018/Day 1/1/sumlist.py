# Ryan Keller
#
# AoC Day 1 Problem 1
#

def sumlist(filename):
    fp = open(filename, 'r')
    total = 0
    line = fp.readline()
    while (line != ""):
        sign = line[0] ## "+" or "-"
        rest = int(line[1:]) ## integer portion
        if (sign == "+"):
            total = total + rest
        elif (sign == "-"):
            total = total - rest
        line = fp.readline()
    fp.close()
    return total

def main():
    print sumlist("input.txt")

if __name__ == "__main__":
    main()
