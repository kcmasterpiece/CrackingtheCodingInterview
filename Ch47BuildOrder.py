# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project).  All of the project's dependencies must be built before the project is.  Find a build order that will allow the projects to be built.  If there is no valid build order, return an error.

# EXAMPLE

# Input: 
    # projects: a, b, c, d, e, f
    # dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
import string
from pprint import pprint

def findBuildOrder(projects, dependencies):
    pd = {}
    for p in projects:
        pd[p] = []
    for d, p in dependencies:
        pd[p].append(d)
    
    built = []
    while len(pd) > 0:
        for p in list(pd.keys()):
            for d in pd[p]:
                if d in built:
                    del pd[p][pd[p].index(d)]

            if len(pd[p]) == 0:
                built.append(p)
                del pd[p]
    return built
if __name__ == "__main__":

    projects = list(string.ascii_lowercase[0:7]) 
    dependencies = [('f','c'), ('f', 'b'), ('b', 'a'), ('f', 'a'), ('b', 'e'), ('a', 'e'), ('d', 'g')]
    print(findBuildOrder(projects, dependencies))

