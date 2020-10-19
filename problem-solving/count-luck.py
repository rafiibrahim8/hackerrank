# https://www.hackerrank.com/challenges/count-luck/problem

def findMove(matrix,now,gone):
    x,y = now
    moves = list()
    moves.append((x+1,y)) if(x!=len(matrix)-1 and matrix[x+1][y]!='X' ) else None
    moves.append((x,y+1)) if(y!=len(matrix[0])-1 and matrix[x][y+1]!='X') else None
    moves.append((x-1,y)) if(x!=0 and matrix[x-1][y]!='X') else None
    moves.append((x,y-1)) if(y!=0 and matrix[x][y-1]!='X') else None
    
    for move in moves:
        if(move in gone):
            moves.remove(move)
    
    return moves

def findPath(matrix,now):
    wave=0
    gone = [now]
    stack= []
    moves =[now]
    while(True):
        gone.append(moves[0])
        if(matrix[moves[0][0]][moves[0][1]]=='*'):
            return wave
        moves = findMove(matrix,moves[0],gone)

        if(len(moves)>1):
            wave +=1
            for i in range(1,len(moves)):
                stack.append(moves[i])
        elif(len(moves)<1):
            moves = [stack.pop()]


def countLuck(matrix, k):
    for m in range(len(matrix)):
        if('M' in matrix[m]):
            start = (m,matrix[m].index('M'))
        
    print('Impressed' if findPath(matrix,start)==k else 'Oops!')
    


def main():
    t = int(input())
    for t_itr in range(t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])

        matrix = []
        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())
        countLuck(matrix, k)

if __name__ == '__main__':
    main()
