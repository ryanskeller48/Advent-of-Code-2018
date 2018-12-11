# Ryan Keller
#
# AoC Day 7 Problem 1
#

from sets import Set

def get_data(line): # get data from txt input
    words = line.split(" ")
    dependency = words[1]
    dependent = words[7]
    return [dependency, dependent]

def make_dependencies(filename):
    # make a hashmap of tasks that require other tasks
    # to finish before they can start.
    # So, if "Task B must finish before Task A can begin,"
    # and "Task C must finish before Task A can begin,"
    # dependents = {A:[B, C]}
    fp = open(filename, 'r')
    line = fp.readline()
    dependents = {}
    values = Set() # contains all task ids we see. there may be
                   # tasks that dont have dependencies, so aren't keys in
                   # dependents. These tasks can start immediately without
                   # relying on other tasks to finish first
    while (line != ""):
        data = get_data(line)
        dependency = data[0]
        dependent = data[1]
        values.add(dependency) # add tasks that arent dependent to values
        if (dependent in dependents):
            # if the dependent task is already in the hashmap,
            # add its new dependency
            dependents[dependent] += [dependency]
        else:
            # else create a new entry
            dependents[dependent] = [dependency]
        line = fp.readline()
    fp.close()
    can_start_now = [] # list of tasks with no dependencies
    for value in values:
        if (value not in dependents):
            can_start_now += [value] # values that are not keys in dependents can start now
    return (dependents, sorted(can_start_now)) # return tasks that can start in alphabetical order

def task_order(filename): # determine run order of tasks bases on dependencies
    data = make_dependencies(filename)
    rules = data[0] # = dependents
    ready = data[1] # = can_start_now
    order = "" # output order of tasks
    while (len(ready) != 0):
        newreadies = [] # tasks that become ready once their dependencies are already complete
        currtask = ready[0]
        order += currtask # add the current task to output
        ready = ready[1:] # take current task off of ready to start list
        for rule in rules: # for each task with dependencies
            dependencies = rules[rule]
            if (currtask in dependencies):
                dependencies.remove(currtask) # if the current task is in the dependencies list, remove it
                if (len(dependencies) == 0):
                    # if that task has no more active dependencies, add it to the ready tasks
                    ready += [rule]
                    newreadies += [rule]
        for n in newreadies:
            if (n in rules):
                # delete tasks that are ready from hashmap (but not while we're iterating thru the keys!)
                del rules[n] 
        ready = sorted(ready) # keep ready tasks in sorted order
    return order
                
                

def main():
    print task_order("input.txt")
    

if __name__ == "__main__":
    main()  
