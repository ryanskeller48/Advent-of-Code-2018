# Ryan Keller
#
# AoC Day 3 Problem 2
#

# helper functions to strip data from txt input
def get_coordinates(line):
    coord = line.split(" ")[2].split(",")
    return [coord[0], coord[1].split(":")[0]]

def get_size(line):
    size = line.split(" ")[3].split("x")
    return [size[0], size[1].split("\n")[0]]

def overlap_check(d, xstart, xend, ystart, yend):
    # using  dictionary of claimed coordinated, check if any of the points in
    # a rectangle claim overlap with previous claims
    for x in range(xstart, xend):
        for y in range (ystart, yend):
            if (d[x][y] == True): return False # if overlap, exit
    return True

# like the previous problem, this function builds a hashmap of claimed and
# overlapped coordinates.  To find the claim with no overlap, we build the hashmap
# and then check each claim again to see if none of its coordinate hashmap
# values are "True", which indicates it collided with another claim.
# this takes two scans of input, which is 0(N) and better than O(N^2)
# of comparing each claim to each other claim

def no_overlap(filename):

    # open file, read first line to start loop
    fp = open(filename, 'r')
    line = fp.readline()

    # this dictionary will store the data about which squares are overlapping
    xdict = {}

    # build dictionary that represents overlap iteratively
    while (line != ""):
        coord = get_coordinates(line) 
        size = get_size(line)
        
        xstart = int(coord[0]); xsize = int(size[0])
        xend = xstart + int(size[0])
        
        ystart = int(coord[1]); ysize = int(size[1])
        yend = ystart + int(size[1])

        # for each cell, check if the cell is already in the dictionary
        for x in range(xstart, xend):
            if (x in xdict):
                ydict = xdict[x]
                for y in range (ystart, yend):
                    if (y in ydict):
                        # if the cell is already in the dictionary
                        if (ydict[y] == False): # and it's not overlapped already
                            ydict[y] = True # mark it as overlapped
                    else:
                        ydict[y] = False # if it's not in, add it
            else:
                newydict = {}
                for y in range (ystart, yend):
                    newydict[y] = False
                xdict[x] = newydict
        
        line = fp.readline()
        
    ############ end while() ###############
    fp.close()
    fp = open(filename, 'r')
    line = fp.readline()
    linenum = 1
    while (line != ""):
        
        coord = get_coordinates(line) 
        size = get_size(line)
        
        xstart = int(coord[0]); xsize = int(size[0])
        xend = xstart + int(size[0])
        
        ystart = int(coord[1]); ysize = int(size[1])
        yend = ystart + int(size[1])
        if (overlap_check(xdict, xstart, xend, ystart, yend)): return linenum
        else:
            linenum += 1
        line = fp.readline()
    fp.close()
    return 0
    
    
    
            
def main():
    print no_overlap("input.txt")
    

if __name__ == "__main__":
    main()     
                              




