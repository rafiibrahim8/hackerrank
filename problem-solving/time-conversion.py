# https://www.hackerrank.com/challenges/time-conversion/problem
def timeConversion(s):
    if(s[-2:]=='PM'):
        n = int(s[:2]) + 12 if(s[:2] != '12') else 12
        return str(n) + s[2:-2]
    if(s[:2]=='12'):
        return '00' + s[2:-2]
    return s[:-2]
if __name__ == '__main__':
    print(timeConversion(input()))
