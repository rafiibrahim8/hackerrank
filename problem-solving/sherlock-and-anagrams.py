# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

def num_gen(n):
    l = list()
    for i in range(1,n):
        for j in range(n):
            if(j+i>n):
                break
            else:
                l.append((j,i+j))
    return l

def sherlockAndAnagrams(s):
    summ=0
    d = dict()
    n = num_gen(len(s))
    for i in n:
        x = str(sorted(s[i[0]:i[1]]))
        d[x] = d.get(x,0)+1
    
    for a in d:
        summ += (d[a]-1)*d[a] //2
    return summ
        

def main():
    for _ in range(int(input())):
        s = input()
        print(sherlockAndAnagrams(s))

if __name__ == '__main__':
    main()
