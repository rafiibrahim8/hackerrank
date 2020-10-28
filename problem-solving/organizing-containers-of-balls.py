# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

def getCol(n, container):
    l = []
    for c in container:
        l.append(c[n])
    return l

def getRow(n, container):
    return container[n]

def organizingContainers(container):
    c_sum = []
    r_sum = []
    for i in range(len(container)):
        c_sum.append(sum(getCol(i,container)))
        r_sum.append(sum(getRow(i,container)))
    c_sum.sort()
    r_sum.sort()
    return 'Possible' if(c_sum == r_sum) else 'Impossible'

if __name__ == '__main__':
    for q in range(int(input())):
        n = int(input())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))
        print(organizingContainers(container))

