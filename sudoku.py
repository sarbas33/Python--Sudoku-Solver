s=123
def correctness(table,val,row,col):
    for i in range(9):
        if table[row][i]==val:
            return False

    for i in range(9):
        if table[i][col]==val:
            return False

    #3X3 table starting box 
    start_row= row-(row%3)
    start_col=col-(col%3)

    for i in range(3):
        for j in range(3):
            if table[start_row+i][start_col+j]==val:
                return False
    # add any other constraints after this comment
    return True

def solution(table,row,col):
    if (row==8) and (col==9):
        return True
    
    if col==9:
        row=row+1
        col=0
        solution(table,row,col)
    if table[row][col]>0:
        return solution(table,row,col+1)
    if table[row][col]==0:
        for i in range(1,10):
            if correctness(table,i,row,col):
                table[row][col]=i
                
                if solution(table,row,col+1):
                    return True
            table[row][col]=0
    return False

table=[[5,3,4,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
solution(table,0,0)
for x in table:
    print (x)
