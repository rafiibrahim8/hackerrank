# https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [a+i for i in apples]
    oranges = [b+i for i in oranges]
    count = 0
    for i in apples:
        if(i>=s and i<=t):
            count +=1
    print(count)

    count = 0
    for i in oranges:
        if(i>=s and i<=t):
            count +=1
    print(count)

if __name__ == '__main__':
    s,t  = tuple(map(int, input().rstrip().split()))
    a,b  = tuple(map(int, input().rstrip().split()))
    _ = input()
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)
