# https://www.hackerrank.com/challenges/diagonal-difference/problem
def diagonalDifference(arr):
    primary=secondary=0
    for i in range(len(arr)):
        primary += arr[i][i]
        secondary += arr[i][len(arr)-i-1]
    return abs(primary-secondary)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    print(diagonalDifference(arr))