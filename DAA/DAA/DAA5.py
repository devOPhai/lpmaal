class NQBacktracking:
    def __init__(self, x_, y_):
        """Initialize N-Queens Backtracking solver with an initial position for the 1st queen."""
        self.ld = [0] * 30  # Left diagonal check
        self.rd = [0] * 30  # Right diagonal check
        self.cl = [0] * 30  # Column check
        self.x = x_  # Row of the 1st queen
        self.y = y_  # Column of the 1st queen

    def printSolution(self, board):
        """A utility function to print the N-Queens solution."""
        print("N-Queens Backtracking Solution:\nGiven initial position of 1st queen at row:", self.x, "column:", self.y, "\n")
        for line in board:
            print(" ".join(map(str, line)))

    def solveNQUtil(self, board, col):
        """A recursive utility function to solve the N-Queens problem."""
        if col >= N:
            return True

        if col == self.y:
            return self.solveNQUtil(board, col + 1)

        for i in range(N):
            if i == self.x:
                continue

            if (self.ld[i - col + N - 1] != 1 and self.rd[i + col] != 1) and self.cl[i] != 1:
                board[i][col] = 1
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 1

                if self.solveNQUtil(board, col + 1):
                    return True

                board[i][col] = 0  # Backtrack
                self.ld[i - col + N - 1] = self.rd[i + col] = self.cl[i] = 0

        return False

    def solveNQ(self):
        """This function solves the N-Queens problem using Backtracking."""
        board = [[0 for _ in range(N)] for _ in range(N)]
        board[self.x][self.y] = 1
        self.ld[self.x - self.y + N - 1] = self.rd[self.x + self.y] = self.cl[self.x] = 1

        if not self.solveNQUtil(board, 0):
            print("Solution does not exist")
            return False

        self.printSolution(board)
        return True

if __name__ == "__main__":
    N = 8  # Board size
    x, y = 3, 2  # Initial position for the 1st queen
    NQBt = NQBacktracking(x, y)
    NQBt.solveNQ()
