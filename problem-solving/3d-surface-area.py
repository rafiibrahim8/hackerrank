# https://www.hackerrank.com/challenges/3d-surface-area/problem

def get_for_it(a,i,j):
    s = 2 # top & bottom
    s += a[i][j] if(i==len(a)-1) else max([0, a[i][j] - a[i+1][j]]) # down
    s += a[i][j] if(i==0) else max([0, a[i][j] - a[i-1][j]]) # up
    s += a[i][j] if(j==0) else max([0, a[i][j] - a[i][j-1]]) # left
    s += a[i][j] if(j==len(a[0])-1) else max([0, a[i][j] - a[i][j+1]]) # right
    return s

def surfaceArea(A):
    _sum = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            _sum += get_for_it(A,i,j)
    return _sum


if __name__ == '__main__':
    H = int(input().split()[0])
    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    print(surfaceArea(A))
