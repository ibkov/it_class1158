class SeaMap:
    def __init__(self):
        self.mass = [['.' for i in range(10)] for j in range(10)]

    def recur(self, row, col):
        if row < 0 or row > 9 or col < 0 or col > 9 or self.mass[row][col] != 'x':
            return
        if self.mass[row][col] == 'x' and row + 1 >= 0 and row + 1 <= 9 and self.mass[row + 1][col] != 'x':
            self.mass[row + 1][col] = '*'
        if self.mass[row][col] == 'x' and row - 1 >= 0 and row - 1 <= 9 and self.mass[row - 1][col] != 'x':
            self.mass[row - 1][col] = '*'
        if self.mass[row][col] == 'x' and col + 1 >= 0 and col + 1 <= 9 and self.mass[row][col + 1] != 'x':
            self.mass[row][col + 1] = '*'
        if self.mass[row][col] == 'x' and col - 1 >= 0 and col - 1 <= 9 and self.mass[row][col - 1] != 'x':
            self.mass[row][col - 1] = '*'
        self.recur(row + 1, col)
        self.recur(row - 1, col)
        self.recur(row, col + 1)
        self.recur(row, col - 1)

    def shoot(self, row, col, result):
        if result == 'miss':
            self.mass[row][col] = '*'
        elif result == 'hit':
            self.mass[row][col] = 'x'
        elif result == 'sink':
            self.recur(row, col);

    def cell(self, row, col):
        return self.mass[row][col]

sm = SeaMap()
sm.shoot(2, 0, 'sink')
sm.shoot(6, 9, 'hit')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()