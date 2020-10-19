# https://www.hackerrank.com/challenges/non-divisible-subset/problem

def nonDivisibleSubset(k, s):
    rem = [0 for _ in range(k)]
    for i in s:
        rem[i%k] += 1
    ans = 0 if(rem[0]==0) else 1
    for i in range(1,len(rem)//2+1):
        if(i != k-i):
            ans += max([rem[i],rem[k-i]])
        else:
            ans += 1
    return ans

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))
    print(nonDivisibleSubset(k, s))
