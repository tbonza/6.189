from graphics import *
from wheel import *

class Car():
    def __init__(self, front_tire, f_tire_rad, back_tire,
                 b_tire_rad, rect_height):
        
        # Don't run out of space
        space_x = front_tire.x
        space_y = front_tire.y - rect_height
        if space_y < 0:
            space_y = 0
        space = Point(space_x, space_y)
        
        # Car body
        self.rect = Rectangle(space, back_tire)
        # Front wheel
        self.front_wheel = Wheel(front_tire, 0.6*f_tire_rad, f_tire_rad)
        # Back wheel
        self.back_wheel = Wheel(back_tire, 0.6*b_tire_rad, b_tire_rad)  
    
    def draw(self, win):
        # draw the car body
        self.rect.draw(win)
        # draw the front wheel
        self.front_wheel.draw(win)
        # draw the back wheel
        self.back_wheel.draw(win)
        
    
    def set_color(self, tire_color, rim_color, car_color,
                  trim_color):
        # front wheel colors
        self.front_wheel.set_color(rim_color, tire_color)
        # back wheel colors
        self.back_wheel.set_color(rim_color, tire_color)
        # car colors
        self.rect.setFill(car_color)
        self.rect.setOutline(trim_color)
        self.rect.setWidth(5)
        
    def animate(self, win, dx,dy, n):
        if n > 0:
            # Move the front wheel
            self.front_wheel.move(dx,dy)
            # Move the back wheel
            self.back_wheel.move(dx,dy)
            # Move the car body
            self.rect.move(dx,dy)
            # Move the wheels & body at once
            win.after(100, self.animate, win, dx, dy, n-1)

def vroom_vroom():

    new_win = GraphWin("A Watermelon Car", 700, 300)

    # create a car object
    # 1st wheel centered at 50, 50 with radius 15
    # 2nd wheel centered at 100, 50 with radius 15
    # rectangle with a height of 40 

    car1 = Car(Point(50,50), 15, Point(100,50), 15, 40)
    car1.draw(new_win)

    # color the wheels grey with black tires, and the body pink
    car1.set_color('black', 'grey', 'pink','green')

    # make the car move on the screen
    car1.animate(new_win, 1, 0, 400)

    new_win.mainloop()
    
    
# Start the car by calling the main function "vroom_vroom". Not
# sure what happens when main function is defined in another file
vroom_vroom()