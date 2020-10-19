# https://www.hackerrank.com/challenges/minimum-loss/problem

def minimumLoss(price):
    min_loss = list()
    price = [(i,j) for i,j in zip(range(len(price)), price)]
    price = sorted(price,key=lambda x: x[1])
    for i in range(len(price)-1):
        if(price[i][0]>price[i+1][0] and price[i][1]<price[i+1][1]):
            min_loss.append(price[i+1][1]-price[i][1])
    min_loss.sort()
    return min_loss[0]

if __name__ == '__main__':
    n = int(input())
    price = list(map(int, input().rstrip().split()))
    print(minimumLoss(price))
