import turtle as tu
import math as m
import time as ti

tu.hideturtle()

tu.Screen().tracer(0)
class Point():
    
    def __init__(self, point_coords):
        self.point_coords = point_coords

    def turn_z(self, center_coords):
        tu.up()
        tu.goto(center_coords[0], center_coords[1])
        tu.seth(tu.towards(self.point_coords[0], self.point_coords[1])-1)
        tu.forward(m.sqrt((center_coords[0]-self.point_coords[0])**2+(center_coords[1]-self.point_coords[1])**2))
        self.point_coords = [tu.xcor(), tu.ycor(), self.point_coords[2]]
        
    def turn_y(self, center_coords):
        tu.up()
        tu.goto(center_coords[0], center_coords[1])
        tu.seth(tu.towards(self.point_coords[0], self.point_coords[2])-1)
        tu.forward(m.sqrt((center_coords[0]-self.point_coords[0])**2+(center_coords[1]-self.point_coords[2])**2))
        self.point_coords = [tu.xcor(), self.point_coords[1], tu.ycor()]

    def turn_x(self, center_coords):
        tu.up()
        tu.goto(center_coords[0], center_coords[1])
        tu.seth(tu.towards(self.point_coords[1], self.point_coords[2])-1)
        tu.forward(m.sqrt((center_coords[0]-self.point_coords[1])**2+(center_coords[1]-self.point_coords[2])**2))
        self.point_coords = [self.point_coords[0], tu.xcor(), tu.ycor()]
    
    def check_point(self):
        tu.up()
        s1 = Spec((0, 0, 0), (100,100, 100), 90, 150)
        s1.check_screen((0,0), (self.point_coords[0], self.point_coords[2]))
        tu.goto(s1.new_point_coords, 0)
        s1.check_screen((0,0), (self.point_coords[1], self.point_coords[2]))
        tu.goto(tu.xcor(), s1.new_point_coords)
        self.save=(tu.xcor(), tu.ycor())

class Spec(tu.Turtle):

  def __init__(self, spec_coords, TD_point_coords, rotation, screen_size):
    super().__init__(visible = False)
    self.spec_coords_x, self.spec_coords_y, self.spec_coords_z = spec_coords[0], spec_coords[1], spec_coords[2]
    self.TD_point_x, self.TD_point_y, self.TD_point_z = TD_point_coords[0], TD_point_coords[1], TD_point_coords[2]
    self.rotation = rotation
    self.screen_size = screen_size
    self.new_point_coords = []

  def check_screen(self, temporary_spec_coords, temporary_point_coords):
    self.up()
    self.goto(temporary_spec_coords[0], temporary_spec_coords[1])
    self.seth(self.rotation)
    self.forward(self.screen_size)
    screen_center_coords = [self.xcor(), self.ycor()]
    self.goto(temporary_spec_coords[0], temporary_spec_coords[1])
    self.seth(0)
    cancel = 0
    save = round(self.towards(screen_center_coords[0], screen_center_coords[1]))
    while cancel != 1 and round(self.towards(screen_center_coords[0], screen_center_coords[1])) != self.rotation+90 and round(self.towards(screen_center_coords[0], screen_center_coords[1])) != self.rotation-90 and self.ycor() <= 540:
        if round(self.towards(screen_center_coords[0], screen_center_coords[1])) >= self.rotation+90 >= save:
            cancel = 1
            self.seth(self.towards(temporary_point_coords[0], temporary_point_coords[1]))
            self.backward(2)
        elif round(self.towards(screen_center_coords[0], screen_center_coords[1])) <= self.rotation-90 <= save:
            cancel = 1
            self.seth(self.towards(temporary_point_coords[0], temporary_point_coords[1]))
            self.backward(2)
        self.seth(self.towards(temporary_point_coords[0], temporary_point_coords[1]))
        save = round(self.towards(screen_center_coords[0], screen_center_coords[1]))
        self.forward(1)
        self.seth(abs(m.floor(self.towards(screen_center_coords[0], screen_center_coords[1]))))
    self.new_point_coords = (round(self.xcor()))
z_change = -50
list_points_cube = [Point([-50, 50, 150-z_change]), Point([50, 50, 150-z_change]), 
               Point([50, 50, 250-z_change]), Point([-50, 50,250-z_change]), 
               Point([-50, -50, 150-z_change]), Point([50, -50, 150-z_change]),  
               Point([50, -50, 250-z_change]), Point([-50, -50, 250-z_change])] 
list_points_pyramid = [Point([0, 50, 200-z_change]),
               Point([-50, -50, 150-z_change]), Point([50, -50, 150-z_change]),  
               Point([50, -50, 250-z_change]), Point([-50, -50, 250-z_change])] 
list_points_table = [Point([-50, -50, 150-z_change]), Point([-50, -50, 175-z_change]),
                       Point([-50, -25, 150-z_change]), Point([-50, -25, 175-z_change]),
                       Point([-50, 0, 150-z_change]), Point([-50, 0, 175-z_change]),
                       Point([-50, 0, 150-z_change]), Point([-50, 0, 175-z_change])]

list_points = list_points_table

def turn_all_points_z():
    for i in range(len(list_points)):
        list_points[i].turn_z((0,0))
def turn_all_points_x():
    for i in range(len(list_points)):
        list_points[i].turn_x((0, 200-z_change))
def turn_all_points_y():
    for i in range(len(list_points)):
        list_points[i].turn_y((0, 200-z_change))
def check_all_points():
    for i in range(len(list_points)):
        list_points[i].check_point()

def generate_cube(size):
    while True:
        tu.clear()
        tu.up()
        turn_all_points_x()
        turn_all_points_y()
        turn_all_points_z()
        
        check_all_points()

        tu.up()
        tu.goto(list_points[0].save[0]*size, list_points[0].save[1]*size)
        tu.down()
        tu.goto(list_points[1].save[0]*size, list_points[1].save[1]*size)
        tu.goto(list_points[2].save[0]*size, list_points[2].save[1]*size)
        tu.goto(list_points[3].save[0]*size, list_points[3].save[1]*size)
        tu.goto(list_points[0].save[0]*size, list_points[0].save[1]*size)            
        tu.up()
        tu.goto(list_points[4].save[0]*size, list_points[4].save[1]*size)
        tu.down()
        tu.goto(list_points[5].save[0]*size, list_points[5].save[1]*size)
        tu.goto(list_points[6].save[0]*size, list_points[6].save[1]*size)
        tu.goto(list_points[7].save[0]*size, list_points[7].save[1]*size)
        tu.goto(list_points[4].save[0]*size, list_points[4].save[1]*size)
        
        tu.up()
        tu.goto(list_points[4].save[0]*size, list_points[4].save[1]*size)
        tu.down()
        tu.goto(list_points[0].save[0]*size, list_points[0].save[1]*size)
        tu.up()
        tu.goto(list_points[5].save[0]*size, list_points[5].save[1]*size)
        tu.down()
        tu.goto(list_points[1].save[0]*size, list_points[1].save[1]*size)
        tu.up()
        tu.goto(list_points[6].save[0]*size, list_points[6].save[1]*size)
        tu.down()
        tu.goto(list_points[2].save[0]*size, list_points[2].save[1]*size)
        tu.up()
        tu.goto(list_points[7].save[0]*size, list_points[7].save[1]*size)
        tu.down()
        tu.goto(list_points[3].save[0]*size, list_points[3].save[1]*size)
        tu.Screen().update()
        
        tu.up()
        tu.goto(list_points[4].save[0]*size, list_points[4].save[1]*size)
        tu.down()
        tu.goto(list_points[0].save[0]*size, list_points[0].save[1]*size)
        tu.up()
        tu.goto(list_points[5].save[0]*size, list_points[5].save[1]*size)
        tu.down()
        tu.goto(list_points[1].save[0]*size, list_points[1].save[1]*size)
        tu.up()
        tu.goto(list_points[6].save[0]*size, list_points[6].save[1]*size)
        tu.down()
        tu.goto(list_points[2].save[0]*size, list_points[2].save[1]*size)
        tu.up()
        tu.goto(list_points[7].save[0]*size, list_points[7].save[1]*size)
        tu.down()
        tu.goto(list_points[3].save[0]*size, list_points[3].save[1]*size)
        tu.Screen().update()

def generate_pyramid(size):
    while True:
        tu.clear()
        turn_all_points_x()
        check_all_points()
        for i in range(4):
            tu.up()
            tu.goto(list_points[0].save[0]*size, list_points[0].save[1]*size)
            tu.down()
            tu.goto(list_points[i+1].save[0]*size, list_points[i+1].save[1]*size)
        tu.goto(list_points[3].save[0]*size, list_points[3].save[1]*size)
        tu.goto(list_points[2].save[0]*size, list_points[2].save[1]*size)
        tu.goto(list_points[1].save[0]*size, list_points[1].save[1]*size)
        tu.goto(list_points[4].save[0]*size, list_points[4].save[1]*size)
        tu.Screen().update()
list_points_table = [Point([-50, -50, 150-z_change]), Point([-50, -50, 175-z_change]),
                       Point([-50, -25, 150-z_change]), Point([-50, -25, 175-z_change]),
                       Point([-50, 0, 150-z_change]), Point([-50, 0, 175-z_change]),
                       Point([-50, 0, 150-z_change]), Point([-50, 0, 175-z_change])]
def generate_table():
    while True:
        tu.clear()
        check_all_points()
        tu.up()
        tu.goto(list_points[0].save[0], list_points[0].save[1])
        tu.down()
        tu.goto(list_points[1].save[0], list_points[1].save[1])
        tu.goto(list_points[3].save[0], list_points[3].save[1])
        tu.goto(list_points[2].save[0], list_points[2].save[1])
        tu.goto(list_points[0].save[0], list_points[0].save[1])
        tu.Screen().update
generate_table()


        
tu.Screen().update()