import copy
from collections import Counter
class Board:
    def __init__(self, n):
        self.n = n
                    #list of n _ 's         #do that n times
        self.table = [['_' for _ in range(n)] for _ in range(n)] 

    def __str__(self):
        newTable = []
        for row in self.table:
            itemRow = ' '.join(row)
            newTable.append(itemRow)
        return '\n'.join(newTable) #convert to string
        

    def getSize(self): #returns the size
        return self.n

    def place(self,row, column): #needs to place a queen on the board

        if self.canPlace(row,column):
            if self.isPositionOnBoard(row,column):
                self.table[row][column] = 'Q' #refers to a single element
                print("placing queen")

    def isValidHorizontal(self, row,column):
        for i in range(self.n): #column doesn't change
            if self.table[row][i] == 'Q':
                print("cannot place horizontal")
                return False
        return True


    def isValidVertical(self, row,column):
        for i in range(self.n): #column doesn't change
            if self.table[i][column] == 'Q':
                print("cannot place vertical")
                return False
        return True

    def isValidDownLeft(self, row, column):
        dr = -1
        dc = 1
        r = row
        c = column
        print("calling is valid down left", r, c)
        print("trying to insert down and left")
        while self.isPositionOnBoard(r,c):
            print("trying", r, c)
            if self.isQueen(r,c):
                print("Cannot insert Queen DL")
                return False
            
            r = r + dr
            c = c + dc
        return True


    def isValidDownRight(self, row, column):
        dr = -1
        dc = -1
        r = row
        c = column
        print("trying to insert down and right")
        while self.isPositionOnBoard(r,c):
            if self.isQueen(r,c):
                print("cannot insert queen DR")
                return False
            r = r + dr
            c = c + dc
        return True

    def isValidUpRight(self, row, column):
        dr = 1
        dc = -1
        r = row
        c = column
        print("trying to insert up and right")
        while self.isPositionOnBoard(r,c):
            if self.isQueen(r,c):
                print("Cannot insert Q UR")
                return False
            r = r+ dr
            c = c + dc
        return True

    def isValidUpLeft(self, row, column):
        dr = 1
        dc = 1
        r = row
        c = column
        print("trying to inswert up and left")
        while self.isPositionOnBoard(r,c):
            if self.isQueen(r,c):
                print("cannot insert Q UL")
                return False
            r = r+ dr
            c = c + dc
        return True

    def canPlace(self, row, column):
        testDownLeft = self.isValidDownLeft(row,column)
        testDownRight = self.isValidDownRight(row,column)
        testHorizontal = self.isValidHorizontal(row,column)
        testVertical = self.isValidVertical(row,column)
        testUpLeft = self.isValidUpLeft(row,column)
        testUpRight = self.isValidUpRight(row,column)
        #if testDownLeft:
        #    print('testDownLeft is true')
        #else:
        #    print('testDownLeft is false')
        #if testDownRight:
        #    print('testDownRight is true')
        #else:
        #    print('testDownRight is false')
        #if testHorizontal:
        #    print('testHorizontal is true')
        #else:
        #    print('testHorizontal is false')
        #if testVertical:
        #    print('testVertical is true')
        #else:
            #print('testVertical is false')
        #if testUpLeft:
        #    print('testUpLeft is true')
        #else:
        #    print('testUpLeft is false')
        #if testUpRight:
        #    print('testUpRight is true')
        #else:
        #    print('testUpRight is false')
        # and self.isValidDownRight(row,column) and self.isValidHorizontal(row,column) and self.isValidUpLeft(row,column) and self.isValidUpRight(row,column) and self.isValidVertical(row,column))

        return (testUpRight and testUpLeft and testDownLeft and testDownRight and testHorizontal and testVertical)
    def isPositionOnBoard(self, row, column):
        r = row
        c = column
        
        if (r < self.n and c < self.n and r >=0 and c >=0):
            print("position is valid")
            return True
        return False



    def isQueen(self, row, column):
        if self.table[row][column] == 'Q':
            return True
        else:
            print("there is no queen")
            return False


    def isSolved(self):
        counter = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.isQueen(i,j):
                    counter += 1

        if counter < self.n:           
            print('not solved')
            return False
        return True


########recursive part ############ 

def recursive_solve(column,board):
    if board.isSolved():
        print('solution')
        print(board)
        input()
    elif column < 0:
        pass
    else:
        for i in range(board.getSize()):
            checkBoard = copy.deepcopy(board)
            if checkBoard.canPlace(i,column):
                checkBoard.place(i,column)
                recursive_solve(column-1,checkBoard)

def solve(board):
    recursive_solve(board.getSize()-1,board)

def main():
    board = Board(8)
    #board.place(0,2)
    #board.isSolved()
    #board.place(3,1)
    #board.place(1,0)
    #board.place(2,3)
    #print(board.isSolved())
    solve(board)
    #board.canPlace(1,2)
    #print(board)
    
main()