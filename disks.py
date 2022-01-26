from disk import Disk


class Disks:
    "List of list, consisting of disks"

    def __init__(self, WIDTH, HEIGHT, CELL_WIDTH, EDGE, USER_COLOR,
                 COMPUTER_COLOR):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CELL_WIDTH = CELL_WIDTH
        self.EDGE = EDGE
        self.num_of_rows = int(self.HEIGHT/self.CELL_WIDTH)
        self.num_of_cols = int(self.WIDTH/self.CELL_WIDTH)
        self.matrix = [[None] * self.num_of_cols
                       for i in range(self.num_of_rows)]
        self.black_count = 0
        self.white_count = 0
        self.total_disks = 0
        self.u_color = USER_COLOR
        self.c_color = COMPUTER_COLOR

    def create(self, playerX, playerY, color):
        '''create a disk on desired, legal place'''
        curr_col = int(playerX//self.CELL_WIDTH)
        curr_row = int(playerY//self.CELL_WIDTH)
        self.matrix[curr_row][curr_col] = Disk(curr_row, curr_col,
                                               color,
                                               self.CELL_WIDTH,
                                               self.EDGE)
        if color == self.u_color:
            self.black_count += 1
        else:
            self.white_count += 1
        self.total_disks += 1

    def is_full(self):
        '''check whether all cells have been taken up'''
        if self.total_disks == self.num_of_rows * self.num_of_cols:
            return True
        else:
            return False

    def display(self):
        '''call each disk's display method'''
        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                if self.matrix[row][col] is not None:
                    self.matrix[row][col].display()
