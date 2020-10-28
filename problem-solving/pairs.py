# https://www.hackerrank.com/challenges/pairs/problem
# Run as PyPy3

def pairs(k, arr):
    arr.sort()
    res = 0
    for i in range(len(arr)):
        for j in range(k+1):
            if(i+j==len(arr)):
                break
            if(arr[i+j]-arr[i] == k):
                res += 1
            elif(arr[i+j]-arr[i] > k):
                break
    return res

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    print(pairs(k, arr))
