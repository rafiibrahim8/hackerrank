# https://www.hackerrank.com/challenges/countingsort4/problem

def countSort(arr:list):
    for i in range(len(arr)//2):
        arr[i][1]='-'
    arr.sort(key=lambda j:int(j[0]))
    print(' '.join(i[1] for i in arr))

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())
    countSort(arr)
