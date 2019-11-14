# Sherwin Samson
# 
#
import random
import time

class TicTacToe:
    def __init__(self, board = None, last_state = None):
        if board == None:
            board = ['*', '*', '*', 
                     '*', '*', '*', 
                     '*', '*', '*']
        
        self.board = board    
        return None
    
    def xMove(self, index, board = None):
        if board == None:
            board = self.getBoard()
        board[index] = 'X'
        return board
    
    def oMove(self,index, board = None):
        if board == None:
            board = self.getBoard()
        board[index] = 'O'
        return board
    
    def checkWinner(self, board = None):
        if board == None:
            board = self.getBoard()
            
        diagonal1 = [board[0], board[4], board[8]]
        diagonal2 = [board[2], board[4], board[6]]
        column1 = [board[0], board[3], board[6]]
        column2 = [board[1], board[4], board[7]]
        column3 = [board[2], board[5], board[8]]
        
        if board[:3] == ['X', 'X', 'X']:
            return 'X'
        if board[3:6] == ['X', 'X', 'X']:
            return 'X'
        if board[6:] == ['X', 'X', 'X']:
            return 'X'
        if diagonal1 == ['X', 'X', 'X']:
            return 'X'
        if diagonal2 == ['X', 'X', 'X']:
            return 'X'
        if column1 == ['X', 'X', 'X']:
            return 'X'
        if column2 == ['X', 'X', 'X']:
            return 'X'
        if column3 == ['X', 'X', 'X']:
            return 'X'
        
        if board[:3] == ['O', 'O', 'O']:
            return 'O'
        if board[3:6] == ['O', 'O', 'O']:
            return 'O'
        if board[6:] == ['O', 'O', 'O']:
            return 'O'
        if diagonal1 == ['O', 'O', 'O']:
            return 'O'
        if diagonal2 == ['O', 'O', 'O']:
            return 'O'
        if column1 == ['O', 'O', 'O']:
            return 'O'
        if column2 == ['O', 'O', 'O']:
            return 'O'
        if column3 == ['O', 'O', 'O']:
            return 'O'
        
        return None
    
    def isFinished(self, board = None):
        if board == None:
            board = self.getBoard()
        if self.checkWinner(board) == None:
            for space in board:
                if space == '*':
                    return False
            return True
        return False
    
    def getBoard(self):
        return self.board
    
    def possibleMoves(self, board = None):
        if board == None:
            board = self.getBoard()
        open_tiles = []
        count = 0
        for x in board:
            if x == '*':
                open_tiles.append(count)
            count += 1
        return open_tiles
    
    def printoutBoard(self, board = None):
        if board == None:
            board = self.getBoard()
        count = 0
        for x in board:
            print(str(x) + " ", end=" ")
            count += 1
            if count == 3 or count == 6:
                print()
                
    def findBestMove(self, player):
        movesList = self.possibleMoves()
        
        if len(movesList) == 9:
            random.seed(time.time())
            return random.randint(0,8)
        
        else:
            boardCopy = self.getBoard().copy()
            num = self.minimax(boardCopy, player)
            return num
    
    def gameOver(self, board, player):
        if self.checkWinner(board) != None:
            if self.checkWinner(board) == player:
                return 10
            else:
                return -10
        return 0
        
    def minimax(self, initboard, player):
        board = initboard.copy()
        
        scores = []
        movesList = self.possibleMoves(initboard)
        
        for move in movesList:
            if player == 'X':
                newBoard = self.oMove(move, board.copy())
            else:
                newBoard = self.xMove(move, board.copy())
            scores.append(self.gameOver(newBoard, player))
            
        best = 20
        for score in scores:
            if score < best:
                best = score
        return movesList[scores.index(best)]
        
        
#######################################################


def start():
    game = TicTacToe()
    draw = False

    counter = 0
    while counter < 10:
        print()
        game.printoutBoard()
        print()
        
        if game.checkWinner() != None:
            print("Winner: " + game.checkWinner())
            break
        if game.isFinished():
            print("Draw!")
            draw = True
            break
        
        if counter%2 == 0:
            index = game.findBestMove('X')
            game.xMove(index)
        else:
            index = game.findBestMove('O')
            game.oMove(index)
        
        counter += 1
        
    return draw
    
    
    
    

##########################
print("Starting...\n\n")

draws = 0
for x in range(100):
    if start():
        draws += 1

print("\n\nAverage draws: " + str(draws))
print("\n\nEnd of program")
