# Ryan Keller
#
# AoC Day 3 Problem 1
#


# helper functions to strip data from txt input
def get_coordinates(line):
    coord = line.split(" ")[2].split(",")
    return [coord[0], coord[1].split(":")[0]]

def get_size(line):
    size = line.split(" ")[3].split("x")
    return [size[0], size[1].split("\n")[0]]
    
# instead of building an array of size(x=max(xvalue), y=max(yvalue)) and marking each claimed square, which would require at
# least two parses of the input to build the array then mark each claimed square and space of O(xmax*ymax), we can build a
# hashmap of size = numcoordinates and still address each coordinate directly in O(1) time.  Thus, we can solve in one
# stream of the input in O(N*(xsize*ysize)) where xsize and ysize are the size of the biggest claim

def overlap(filename):
    fp = open(filename, 'r')
    line = fp.readline()
    xdict = {} # hashmap of x coordinates that are read in.
               # values are a hashmap of associated y values (forming coordinates)
    count = 0 # count of overlapped spots
    while (line != ""):
        
        coord = get_coordinates(line) # get data with helper functions
        size = get_size(line)
        xstart = int(coord[0]) # start coordinates are where the rectangle claim is anchored
        ystart = int(coord[1])
        xend = xstart + int(size[0]) # end coordinates define the corners of the rectangle claim
        yend = ystart + int(size[1])
        
        for x in range(xstart, xend): # for all x coordinates in rectangle claim
            if (x in xdict): # if we've already seen this x coordinate
                ydict = xdict[x] # get the corresponding y coordinate dictionary
                for y in range (ystart, yend): # corresponding y coordinates for x coordinate in rectangle
                    if (y in ydict): # if we've seen this y coordinate before
                        if (ydict[y] == False): # but it's not already overlapped
                            ydict[y] = True # mark it as overlapped
                            count += 1 # and add to the overlapped count
                        # else: if it's already overlapped we don't do anything
                    else: # if we haven't seen the y coordinate
                        ydict[y] = False # add it to the hashmap as not overlapped
            else: # if we haven't seen this x coordinate, we need to create a coordinate hashmap
                newydict = {}
                for y in range (ystart, yend):
                    newydict[y] = False # add each y coordinate as not overlapped
                xdict[x] = newydict
        line = fp.readline()
    fp.close()
    return count
            
def main():
    print overlap("input.txt")
    

if __name__ == "__main__":
    main()     
                              



