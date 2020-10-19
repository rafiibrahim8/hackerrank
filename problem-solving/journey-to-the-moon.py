# https://www.hackerrank.com/challenges/journey-to-the-moon/problem
# Run as PyPy3

from itertools import combinations
from sys import setrecursionlimit

visited=set()
class Node:
    def __init__(self,id):
        self.id=id
        self.mates=[]
    def add_mate(self, mate):
        self.mates.append(mate)
    def get_mates(self):
        return self.mates
    def get_id(self):
        return self.id

def xfs(node):
    x=set()
    visited.add(node.get_id())
    x.add(node.get_id())
    for i in node.get_mates():
        if(i.get_id() not in visited):
            x.update(xfs(i))
    return x

def journeyToMoon(n, pairs):
    ids, astronauts = set(range(n)), [Node(i) for i in range(n)]
    country=[]
    pairs_set = set()
    for p in pairs:
        astronauts[p[0]].add_mate(astronauts[p[1]])
        astronauts[p[1]].add_mate(astronauts[p[0]])
        pairs_set.update(p)
    diff = pairs_set.difference(visited)
    while(diff):
        country.append(xfs(astronauts[diff.pop()]))
        diff = pairs_set.difference(visited)
    singles = n-len(pairs_set)
    possible = 0
    for i,j in combinations(country,r=2):
        possible += len(i)*len(j)
    print(possible+singles*len(pairs_set)+singles*(singles-1)//2)

if __name__ == '__main__':
    setrecursionlimit(10000)
    np = input().split()
    n = int(np[0])
    p = int(np[1])
    astronaut = []
    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))
    journeyToMoon(n, astronaut)
