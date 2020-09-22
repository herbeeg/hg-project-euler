class LatticePaths:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.routes = 0

    def findPaths(self):
        row_pointer = 0

        while self.grid_size <= row_pointer:
            pos_x, pos_y = self.resetPosition()
            pos_y = row_pointer

            row_pointer += 1

    def maybeMoveOne(self, position):
        if self.grid_size > position:
            return position += 1
        else:
            return -1

    def goToEnd(self):
        return self.grid_size

    def nextPath(self):
        return

    def resetPosition(self):
        return 0, 0

LatticePaths(3).findPaths()
