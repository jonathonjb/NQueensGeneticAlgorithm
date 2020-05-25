import random

class NQueens():
    def __init__(self, nQueen = 8, board = []):
        self.nQueen = nQueen
        if(board == []):
            self.board = []
            self.initBoard()
        else:
            self.board = board

    def initBoard(self):
        for i in range(self.nQueen):
            self.board.append(random.randint(0, self.nQueen - 1))


    def changeOneValue(self):
        attributeIndex = random.randint(0, self.nQueen - 1)
        self.board[attributeIndex] = random.randint(0, self.nQueen - 1)

    def fitnessFunction(self):
        fitnessValue = 0
        for i in range(len(self.board)):
            queenOnePos = [i, self.board[i]]
            for j in range(i + 1, len(self.board)):
                queenTwoPos = [j, self.board[j]]
                if(self.isPairOfNonAttackingQueens(queenOnePos, queenTwoPos)):
                    fitnessValue += 1
        return fitnessValue

    def isPairOfNonAttackingQueens(self, queenOnePos, queenTwoPos):
        """
        Checks if the pair of queens can attack each other. If so, this will return false, otherwise, it will
        return true.

        """
        if(queenOnePos[0] == queenTwoPos[0] or queenOnePos[1] == queenTwoPos[1]):
            return False
        if(queenOnePos[0] < queenTwoPos[0]):
            diff = queenTwoPos[0] - queenOnePos[0]
            if(queenOnePos[1] < queenTwoPos[1]):
                if(queenTwoPos[1] - diff == queenOnePos[1]):
                    return False
            else:
                if (queenTwoPos[1] + diff == queenOnePos[1]):
                    return False
        else:
            diff = queenOnePos[0] - queenTwoPos[0]
            if (queenTwoPos[1] < queenOnePos[1]):
                if (queenOnePos[1] - diff == queenTwoPos[1]):
                    return False
            else:
                if (queenOnePos[1] + diff == queenTwoPos[1]):
                    return False

        return True

    def getAttributes(self):
        return self.board

    def __str__(self):
        return str(self.board) + ": " + str(self.fitnessFunction())