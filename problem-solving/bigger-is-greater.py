# https://www.hackerrank.com/challenges/bigger-is-greater/problem

def biggerIsGreater(w):
    w = list(w)
    for i in range(len(w)-2,-1,-1):
        for j in sorted(w[i:]):
            if(j>w[i]):
                x = len(w) - w[::-1].index(j) - 1
                w[i],w[x] = w[x],w[i]
                return ''.join(w[:i+1]) + ''.join(sorted(w[i+1:]))
    return 'no answer'

if __name__ == '__main__':
    for _ in range(int(input())):
        print(biggerIsGreater(input()))
