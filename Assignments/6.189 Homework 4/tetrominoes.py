from graphics import *

class Block(Rectangle):
    
    def __init__(self, location, color):
        #Set the location and color
        #Deal with pixels
        self.UL_corner = Point(30 * location.x, 30 * location.y)
        self.LR_corner = Point(30 + self.UL_corner.x, 30 + self.UL_corner.y)
        
        # Make a rectangle with the given coordinates
        self.block = Rectangle(self.UL_corner, self.LR_corner)
        
        # Choose rectangle color scheme
        self.block.setFill(color)
        self.block.setOutline('black')
        self.block.setWidth(2)
        
    # Make a new draw method
    def draw(self, window):
        self.block.draw(window)

class Shape(Block):
    
    def __init__(self,coords, color):
        #Where is the block located?
        self.block_location = coords
        #What color is the block?
        self.block_color = color
    
    # draw the blocks by looping through the list of coordinates
    def draw(self, window):
        
        # loop through coordinates
        for x in range(len(self.block_location)):
            
            # make_block is given a coordinate pair from block_location
            make_block = Point(self.block_location[x].getX(), 
                               self.block_location[x].getY())
            
            # Block is made from the given coordinates
            make_block = Block(make_block, self.block_color)
            
            # Block is made (drawn)
            make_block.block.draw(window)

# I_shape 
class I_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 2, center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "blue")

class J_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, "orange")

class L_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "light sky blue")

class O_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x    , center.y + 1)]
        Shape.__init__(self, coords, "red")

class S_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x    , center.y + 1),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "green")

class T_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y),
                  Point(center.x    , center.y + 1)]
        Shape.__init__(self, coords, "yellow")

class Z_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x    , center.y + 1),
                  Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, "pink")
    
#Main function to create block
def main():
    win = GraphWin("Tetrominoes", 900, 150)
    # a list of shape classes
    tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape,
                   T_shape, Z_shape]
    x = 3
    for tetromino in tetrominoes:
        shape = tetromino(Point(x,1))
        shape.draw(win)
        x += 4
    
    win.mainloop()
    
#Run the program
main()
