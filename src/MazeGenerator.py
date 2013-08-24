import random

# The maze is represented by a 16*16 2-dimensional array

class Pixel(object):
    def __init__(self, maze):
        self.parent_maze = maze
        self.manual_discovered = False
    def set_discovered_true(self):
        self.manual_discover = True
    def discovered(self):
        if self.manual_discover != True:
            for neighbor in self.get_neighbors():
                if neighbor.discovered() == True:
                    return True
            return False
        else:
            return True
    def get_neighbors(self):
        for pixel_array in self.parent_maze.pixels:
            try:
                pixel_index = pixel_array.index(self)
                self.pixel_array = pixel_array
            except ValueError:
                continue
        left_neighbor = self.pixel_array[pixel_index-1]
        right_neighbor = self.pixel_array[pixel_index+1]
        prev_row = self.parent_maze.pixels[self.parent_maze.pixels.index(pixel_array)-1]
        next_row = self.parent_maze.pixels[self.parent_maze.pixels.index(pixel_array)+1]
        bottom_neighbor = next_row[pixel_index]
        top_neighbor = prev_row[pixel_index]
        return [left_neighbor, right_neighbor, bottom_neighbor, top_neighbor]
    
class Maze(object):
    def __init__(self):
        self.pixels = [[Pixel(self)]*16]*16

row = random.randint(0,15)
pixel = random.randint(0,15)
