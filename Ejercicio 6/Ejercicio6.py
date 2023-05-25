class Board:
    def __init__(self, n):
        self.n = n
        self.boards = []
        self.nodes = [Node(i) for i in range(n)]

    def depth_first_search(self):
        for node in self.nodes:
            self._dfs_helper(node, [node])

        self.print_boards()
        print(f"{len(self.boards)} soluciones encontradas para un tablero de {self.n}x{self.n}")

    def _dfs_helper(self, node, path):
        if len(path) == self.n:
            board = ["." * i + "Q" + "." * (self.n - i - 1) for i in path]
            self.boards.append(board)
            return

        for neighbor in node.get_neighbors():
            if neighbor not in path and all(abs(neighbor - i) != len(path) for i, node in enumerate(path)):
                self._dfs_helper(neighbor, path + [neighbor])

    def print_boards(self):
        for board in self.boards:
            for column in board:
                print(column)
            print("")





