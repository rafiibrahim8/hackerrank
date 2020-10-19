# https://www.hackerrank.com/challenges/almost-sorted/problem

def almostSorted(s):
    culprit = list()
    so = sorted(s)
    for i in range(len(s)):
        if(s[i]!=so[i]):
            culprit.append(i)
    if(len(culprit)==2):
        print('yes\nswap {0} {1}'.format(culprit[0]+1,culprit[1]+1))
    elif(len(culprit)>2):
        arr = s[culprit[0]:culprit[-1]+1]
        arr.reverse()
        for i in range(1,len(arr)):
            if(arr[i-1]>arr[i]):
                print('no')
                return
        print('yes\nreverse {0} {1}'.format(culprit[0]+1,culprit[-1]+1))
    else:
        print('yes\nalready sorted')

n = int(input())
lx = list(map(int, input().rstrip().split()))
almostSorted(lx)
