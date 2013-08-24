import random

MAX_INDEX = 15

# The maze is represented by a 16*16 2-dimensional array

class Pixel(object):
    def __init__(self, maze):
        self.parent_maze = maze
        self.manual_discover = False
        self.dead_end = False
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
        neighbors = []
        if pixel_index > 0:
            left_neighbor = self.pixel_array[pixel_index-1]
            neighbors.append(left_neighbor)
        if pixel_index < MAX_INDEX:
            right_neighbor = self.pixel_array[pixel_index+1]
            neighbors.append(right_neighbor)
        pixel_array_index = self.parent_maze.pixels.index(pixel_array)
        if pixel_array_index > 0:
            prev_row = self.parent_maze.pixels[pixel_array_index-1]
            top_neighbor = prev_row[pixel_index]
            neighbors.append(top_neighbor)
        if pixel_array_index < MAX_INDEX:
            next_row = self.parent_maze.pixels[pixel_array_index+1]
            bottom_neighbor = next_row[pixel_index]
            neighbors.append(bottom_neighbor)
        return neighbors
    
class Maze(object):
    def __init__(self):
        self.pixels = [[Pixel(self)]*(MAX_INDEX+1)]*(MAX_INDEX+1)
        self.current_pixel = None
    def generate(self):
        row = random.randint(0,15)
        col = random.randint(0,15)
        self.current_pixel = self.pixels[row][col]
        self.current_pixel.set_discovered_true()
        self.pixel_procedure(self.current_pixel)
    def pixel_procedure(self, pixel):
        neighbors = pixel.get_neighbors()
        random.shuffle(neighbors)
        for neighbor in neighbors:
            if neighbor.discovered == False:
                self.current_pixel = neighbor
                print 
                self.pixel_procedure(neighbor)
            else:
                continue
        pixel.dead_end = True