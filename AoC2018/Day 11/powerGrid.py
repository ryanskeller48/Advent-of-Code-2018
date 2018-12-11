# Ryan Keller
#
# AoC Day 11 Parts 1 and 2
#

serial = 7315 # input

def makeGrid():
    # make a 300x300 grid of Nones.
    # used to store power value of each cell
    grid = []
    for _ in range(301):
        row = [None for _ in range(301)]
        grid.append(row)
    return grid
        
def powerLevel(x, y):
    # check the power level of a given cell
    # using the formula in the probem description
    rackID = x + 10
    power = rackID * y
    power += serial
    power *= rackID
    powerstr = str(power)
    strlen = len(powerstr)
    if (strlen <= 2):
        return -5
    else:
        return int(powerstr[strlen-3]) - 5
    

def power3x3(x, y, grid):
    # calculate the power of a 3x3 square anchored at (x, y)
    xs = range(x, x+3)
    ys = range(y, y+3)
    total_power = 0
    for xcoord in xs:
        for ycoord in ys:
            if (grid[ycoord][xcoord] == None):
                # if power isnt calculated for this cell yet
                power = powerLevel(xcoord, ycoord) 
                grid[ycoord][xcoord] = power # record power of this cell
                total_power += power # add to total
            else:
                # else no need to recalculate, just check the grid
                total_power += grid[ycoord][xcoord] # 2d lists are [row][column]
    return total_power

def powerNxN(x, y, grid):
    # for a given (x, y), calculate the power of the highest power square
    # of size 1 <= n <= 300 anchored at that (x, y)
    # and return the highest power, coordinates of x&y, and size of square.
    # As size increases, we don't need to recalculate the power level --
    # we just need to add the new cells at the edges of the expanding square
    # to the running count.  Thus, each cell is called only once
    # for each (x,y), reducing runtime
    
    best_total = 0 # best running power level
    size = 1 # current size
    best_size = 0 
    coords = ()
    total = 0
    while ((x + size <= 300) & (y + size <= 300)): # while the square still fits in the 300x300 grid
        ycounter = y
        xindex = x + size - 1
        yindex = y + size - 1
        while (ycounter <= yindex - 1): # add the points on the right edge of the expanding square
            if (grid[ycounter][xindex] == None):
                power = powerLevel(xindex, ycounter)
                grid[ycounter][xindex] = power
                total += power
            else:
                total += grid[ycounter][xindex]
            ycounter += 1
        xcounter = x
        while (xcounter <= xindex - 1): # add the points on the bottom edge of the expanding square
            if (grid[yindex][xcounter] == None):
                power = powerLevel(xcounter, yindex)
                grid[yindex][xcounter] = power
                total += power
            else:
                total += grid[yindex][xcounter]
            xcounter += 1
        if (grid[yindex][xindex] == None): # add the point on the bottom right corner of the expanding square
            power = powerLevel(xindex, yindex)
            grid[yindex][xindex] = power
            total += power
        else:
            total += grid[yindex][xindex]
        if (total > best_total): # if this new expanding square has a higher power, record the power, coordinates, and size
            best_total = total
            best_size = size
            coords = (x, y)
        size += 1
    return (best_total, coords, best_size)
            
        
    

def powerGrid3x3():
    grid = makeGrid()
    best_power = 0
    best_coords = ()
    for x in range(1, 299):
        for y in range(1, 299):
            power = power3x3(x, y, grid)
            if (power > best_power):
                best_power = power
                best_coords = (x, y)
    return best_coords

def powerGridNxN():
    grid = makeGrid()
    best_power = 0
    best_coords = ()
    best_size = 0
    for x in range(1, 301):
        for y in range(1, 301):
            power_data = powerNxN(x, y, grid)
            power = power_data[0]
            coords = power_data[1]
            size = power_data[2]
            if (power > best_power):
                best_power = power
                best_coords = (x, y)
                best_size = size
    return (best_coords, best_size)
    

def main():
    #print powerGrid3x3() # PART 1
    print powerGridNxN() # PART 2
    

if __name__ == "__main__":
    main()     
