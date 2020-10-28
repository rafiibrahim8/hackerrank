# https://www.hackerrank.com/challenges/absolute-permutation/problem

def absolutePermutation(n, k):
    arr = list(range(1,n+1))
    j = 0
    l = -1
    while(j<n):
        l *= -1
        for _ in range(max([1,k])):
            arr[j] += l*k
            j +=1
            if(j==n):
                break
    return str(arr).replace(',','')[1:-1] if(sorted(arr) == list(range(1,n+1))) else '-1'

if __name__ == '__main__':
    for t in range(int(input())):
        n, k = tuple(map(int, input().rstrip().split()))
        print(absolutePermutation(n, k))
