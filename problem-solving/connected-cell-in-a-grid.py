# https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

def findMove(matrix,now,stack):
    x,y = now
    moves = list()
    matrix[x][y]='X'
    moves.append((x+1,y)) if(x!=len(matrix)-1 and matrix[x+1][y] not in 'X0' ) else None
    moves.append((x,y+1)) if(y!=len(matrix[0])-1 and matrix[x][y+1] not in 'X0') else None
    moves.append((x-1,y)) if(x!=0 and matrix[x-1][y] not in 'X0') else None
    moves.append((x,y-1)) if(y!=0 and matrix[x][y-1] not in 'X0') else None

    moves.append((x+1,y-1)) if(x!=len(matrix)-1 and y!=0 and matrix[x+1][y-1] not in 'X0' ) else None
    moves.append((x+1,y+1)) if(x!=len(matrix)-1 and y!=len(matrix[0])-1 and matrix[x+1][y+1] not in 'X0') else None
    moves.append((x-1,y-1)) if(x!=0 and y!=0 and matrix[x-1][y-1] not in 'X0') else None
    moves.append((x-1,y+1)) if(x!=0 and y!=len(matrix[0])-1 and matrix[x-1][y+1] not in 'X0') else None

    moves_ = moves[:]
    for m in moves_:
        if(m in stack):
            moves.remove(m)

    return moves

def findPath(matrix,now):
    group=0
    stack= set()
    moves =[now]
    while(moves):
        moves = findMove(matrix,moves[0],stack)
        group+=1
        if(len(moves)>1):
            for i in range(1,len(moves)):
                stack.add(moves[i])
        elif(len(moves)<1):
            try:
                moves = [stack.pop()]
            except:
                moves =[]
    
    return group

def has1(matrix):
    for i in range(len(matrix)):
        if('1' in matrix[i]):
            return (i,matrix[i].index('1'))
    return ()

def connectedCell(matrix):
    max_g = 0
    cor1 = has1(matrix)
    while(cor1):
        max_g = max(findPath(matrix,cor1),max_g)
        cor1 = has1(matrix)
    print(max_g)

def main():
    n = int(input())
    m = int(input())

    matrix = []
    for _ in range(n):
        matrix.append(list(map(str, input().rstrip().split())))

    connectedCell(matrix)

if __name__ == '__main__':
    main()
