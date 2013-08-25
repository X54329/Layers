import random

NUM_COLUMNS = 16
NUM_ROWS = 16

class Pixel(object):
    def __init__(self, maze, row, column):
        self.parent_maze = maze
        self.row = row
        self.column = column
        self.manual_discover = False
        self.dead_end = False
        self.discovered = False
        self.white = False
	    # Sides start at right-facing and go counter-clockwise
	    # side_open[0] ->
	    # side_open[1] /\
	    # side_open[2] <-
	    # side_open[3] \/
    	self.side_open = [False, False, False, False]
    def get_row(self):
        return self.row
    def get_column(self):
        return self.column
    def set_discovered_true(self):
        self.discovered = True
        self.white = True
    def get_sides_open(self):
	    return self.side_open
    def set_side_open(self, side):
	    self.side_open[side] = True
    def discovered(self):
        return discovered  
    def get_neighbors(self):
# I don't think we need this because the pixel remembers it's row and column now

##        for pixel_array in self.parent_maze.pixels:
##            try:
##                pixel_index = pixel_array.index(self)
##                print "row " + str(pixel_index)
##                self.pixel_array = pixel_array
##                print "column " + str(self.parent_maze.pixels.index(pixel_array))
##            except ValueError:
##                continue
        neighbors = []
        if self.column > 0:
            left_neighbor = self.parent_maze.pixels[self.row][self.column - 1]
            neighbors.append(left_neighbor)
        if self.column < NUM_COLUMNS - 1:
            right_neighbor = self.parent_maze.pixels[self.row][self.column + 1]
            neighbors.append(right_neighbor)
        if self.row > 0:
            top_neighbor = self.parent_maze.pixels[self.row - 1][self.column]
            neighbors.append(top_neighbor)
        if self.row < NUM_ROWS - 1:
            bottom_neighbor = self.parent_maze.pixels[self.row + 1][self.column]
            neighbors.append(bottom_neighbor)
        return neighbors
    
class Maze(object):
    def __init__(self):
        # for loop instead of multiplication to fix the pixel copying issue
        self.pixels = [[Pixel(self, i, j) for i in range(NUM_ROWS)] for j in range(NUM_COLUMNS)]
    def generate(self):
        row = random.randint(0,15)
        col = random.randint(0,15)
        first_pixel = self.pixels[row][col]
        first_pixel.set_discovered_true()
        self.pixel_procedure(first_pixel)
    def pixel_procedure(self, pixel):
        pixel.set_discovered_true()
        neighbors = pixel.get_neighbors()
        random.shuffle(neighbors)
        for neighbor in neighbors:
            if neighbor.discovered == False:
                if neighbor.row < pixel.row:
                    pixel.set_side_open(1)
                    neighbor.set_side_open(3)
                if neighbor.row > pixel.row:
                    pixel.set_side_open(3)
                    neighbor.set_side_open(1)
                if neighbor.column < pixel.column:
                    pixel.set_side_open(0)
                    neighbor.set_side_open(2)
                if neighbor.column > pixel.column:
                    pixel.set_side_open(2)
                    neighbor.set_side_open(0)
                neighbor.white = True
                self.pixel_procedure(neighbor)
            else:
                continue
        pixel.dead_end = True
