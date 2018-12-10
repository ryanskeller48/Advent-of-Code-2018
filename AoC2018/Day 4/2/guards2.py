# Ryan Keller
#
# AoC Day 4 Problem 2
#

def get_info(line):
    linesplit = line.split(" ")
    date = linesplit[0].split("-")
    month = date[1]
    day = date[2]
    time = linesplit[1][:5].split(":")
    hour = time[0]
    minutes = time[1]
    if (linesplit[3][0] == "#"):
        return [month, day, hour, minutes, linesplit[3][1:]]
    elif (linesplit[2] == "falls"):
        return [month, day, hour, minutes, "sleep"]
    else:
        return [month, day, hour, minutes, "wake"]

def read_logs(filename):
    fp = open(filename, 'r')
    line = fp.readline()
    logs = []
    while (line != ""):
        logs = logs + [get_info(line)]
        line = fp.readline()
    fp.close()
    return sorted(logs)

def make_empty_sleep_log():
    d = {}
    for x in range(0, 60):
        d[x] = 0
    return d

def sleep_log(filename):
    logs = read_logs(filename)
    currguard = 0
    sleeptime = 0
    waketime = 0
    sleeplog = {}
    for log in logs:
        minutes = int(log[3])
        key = log[4]
        if (key == "sleep"):
            sleeptime = minutes
        elif (key == "wake"):
            waketime = minutes
            sleeprange = range(sleeptime, waketime)
            if (currguard in sleeplog):
                guardlog = sleeplog[currguard]
                for currminute in sleeprange:
                    guardlog[currminute] += 1
            else:
                guardlog = make_empty_sleep_log()
                for currminute in sleeprange:
                    guardlog[currminute] += 1
                    sleeplog[currguard] = guardlog                   
        else: # (key == guard #)
            currguard = int(key)
    return sleeplog

# instead of finding the guard who's asleep the most,
# now we find the guard who has the best sleep minute
def analyze_sleep_log(filename):
    sleeplog = sleep_log(filename)
    keys = sleeplog.keys()
    sleeplist = []
    maxsleepminute = 0
    bestguard = 0
    bestminute = 0
    for guardnum in keys:
        guardlog = sleeplog[guardnum]
        for minute in range(0, 60):
            minutetotal = guardlog[minute]
            if (minutetotal > maxsleepminute): # if we find a new max sleep minute
                maxsleepminute = minutetotal 
                bestminute = minute # record minute number
                bestguard = guardnum # and guard number
    return (bestminute * bestguard)
            
        
def main():
    logs = analyze_sleep_log("input.txt")
    print logs
    

if __name__ == "__main__":
    main()     

