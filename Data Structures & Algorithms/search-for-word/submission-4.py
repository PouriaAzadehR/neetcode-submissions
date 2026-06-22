class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.match(board, i, j, word, 0,path):
                        return True

        else:
            return False


    def match(self, board, i, j, word, f,path):
        if f+1 == len(word):
            return True

        if i >= len(board) or i < 0:
            return False

        if j >= len(board[0]) or j < 0:
            return False


        path.add((i,j))

        

        if i+1 < len(board) :
            if board[i+1][j] == word[f+1] and (i+1,j) not in path :
                if self.match( board, i+1, j, word, f+1,path):
                    return True

        if i-1 >= 0:
            if board[i-1][j] == word[f+1] and (i-1,j) not in path :
                if self.match( board, i-1, j, word, f+1,path):
                    return True

        if j+1 < len(board[0]):
            if board[i][j+1] == word[f+1] and (i,j+1) not in path :
                if self.match( board, i, j+1, word, f+1,path):
                    return True

        if j-1 >= 0:
            if board[i][j-1] == word[f+1] and (i,j-1) not in path:
                if self.match( board, i, j-1, word, f+1,path):
                    return True


        path.remove((i,j))
        return False
