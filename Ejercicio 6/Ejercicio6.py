class Board:
    def __init__(self, n):
        self.n = n
        self.boards = []
        self.possible_board = []
        self.diagonal = []
        self.antidiagonal = []

    def depth_first_search(self):
        self._dfs_helper()
        self.print_boards()
        print(f"{len(self.boards)} soluciones encontradas para un tablero de {self.n}x{self.n}")

    def _dfs_helper(self, row=0):
        if row == self.n:
            board = ["." * i + "Q" + "." * (self.n - i - 1) for i in self.possible_board]
            self.boards.append(board)
            return

        for col in range(self.n):
            if col in self.possible_board or row - col in self.diagonal or row + col in self.antidiagonal:
                continue

            self.possible_board.append(col)
            self.diagonal.append(row - col)
            self.antidiagonal.append(row + col)

            self._dfs_helper(row + 1)

            self.possible_board.pop()
            self.diagonal.pop()
            self.antidiagonal.pop()

    def print_boards(self):
        for board in self.boards:
            for column in board:
                print(column)
            print("")

if __name__ == "__main__":
    n = int(input("Ingrese el número de pokeballs: "))

    board = Board(n)
    board.depth_first_search()

