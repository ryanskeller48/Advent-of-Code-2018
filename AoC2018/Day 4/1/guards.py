# Ryan Keller
#
# AoC Day 4 Problem 1
#

def get_info(line): # take input and transform it into an easier-to-work-with list
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
    # read the input, transform it into list format of dates and important info,
    # and then return those logs sorted by (month, day, hour, minute) to get chronological input
    fp = open(filename, 'r')
    line = fp.readline()
    logs = []
    while (line != ""):
        logs = logs + [get_info(line)]
        line = fp.readline()
    fp.close()
    return sorted(logs)

def make_empty_sleep_log():
    # create an hashmap for a guard to log his asleep minutes
    d = {}
    for x in range(0, 60):
        d[x] = 0
    return d

def sleep_log(filename):
    logs = read_logs(filename) # get data
    currguard = 0 # number of guard on duty
    sleeptime = 0 # minute number guard falls asleep
    waketime = 0 # minute number guard awakes
    sleeplog = {}
    for log in logs:
        minutes = int(log[3])
        key = log[4] # data that tells us which action is happening
        if (key == "sleep"):
            sleeptime = minutes
        elif (key == "wake"): 
            waketime = minutes
            sleeprange = range(sleeptime, waketime) # if the guard wakes up, his sleep minutes start at the last sleeptime
            if (currguard in sleeplog): # if we have this guard in the sleep log
                guardlog = sleeplog[currguard] # find his sleep log
                for currminute in sleeprange: # for each minute he was asleep
                    guardlog[currminute] += 1 # increment his sleep count in his sleep log
            else:
                guardlog = make_empty_sleep_log() # if he doesn't have a sleep log, make one
                for currminute in sleeprange:
                    guardlog[currminute] += 1 # and increment his sleep minutes
                    sleeplog[currguard] = guardlog # and add to the list of guards                  
        else: # (key == guard #)
            currguard = int(key)
    return sleeplog

def analyze_sleep_log(filename):
    sleeplog = sleep_log(filename) # create guard sleep log from input
    keys = sleeplog.keys() # guard numbers
    sleeplist = []
    for guardnum in keys:
        maxsleepminute = 0
        bestminute = 0
        totalsleep = 0
        guardlog = sleeplog[guardnum] # individual guard's sleep log
        for minute in range(0, 60): # check each minute
            minutetotal = guardlog[minute]
            if (minutetotal > maxsleepminute):
                maxsleepminute = minutetotal # keep track of time guard slept most
                bestminute = minute # and the minute number 
            totalsleep += minutetotal # and the total amount of sleep
        sleeplist = sleeplist + [[totalsleep, guardnum, bestminute]] # add guard to list with his sleep stats
    sleeplist = sorted(sleeplist) # sort by which guard slept the most
    topguard = sleeplist[len(sleeplist) - 1] # top sleep is last entry on list
    return (topguard[2] * topguard[1])
            
        
def main():
    logs = analyze_sleep_log("input.txt")
    print logs
    

if __name__ == "__main__":
    main()     

