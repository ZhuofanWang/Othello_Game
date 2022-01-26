class Disk:
    """A disk"""
    def __init__(self, row, col, color, CELL_WIDTH, EDGE):
        self.row = row
        self.col = col
        self.color = color
        self.CELL_WIDTH = CELL_WIDTH
        self.EDGE = EDGE

    def display(self):
        "draw the disk"
        fill(self.color)
        ellipse(self.col * self.CELL_WIDTH + self.CELL_WIDTH/2,
                self.row * self.CELL_WIDTH + self.CELL_WIDTH/2,
                self.CELL_WIDTH - self.EDGE, self.CELL_WIDTH - self.EDGE)

    def __repr__(self):
        if self.color == 0:
            return "0\t"
        elif self.color == 1:
            return "1\t"
