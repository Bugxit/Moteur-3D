import turtle as tu
import math as m
import time as ti

tu.hideturtle()

tu.Screen().tracer(0)
class Point():
    
    def __init__(self, point_coords):
        self.point_coords = point_coords
        
    def turn(self, center_coords):
        tu.up()
        tu.goto(center_coords[0], center_coords[1])
        tu.seth(tu.towards(self.point_coords[0], self.point_coords[1])+1)
        tu.forward(m.sqrt((center_coords[0]-self.point_coords[0])**2+(center_coords[1]-self.point_coords[1])**2))
        self.point_coords = [tu.xcor(), tu.ycor()]

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
    
p1 = Point([-50, 150])
p2 = Point([50, 150])
p3 = Point([50, 250])
p4 = Point([-50,250])

p5 = Point([-50, 150])
p6 = Point([50, 150])
p7 = Point([50, 250])
p8 = Point([-50,250])
def generate_cube1():
    for i in range(90):
        tu.clear()
        tu.up()
        s1 = Spec((0, 0, 0), (100,100, 100), 90, 100)
        p1.turn((0, 200))
        p2.turn((0, 200))
        p3.turn((0, 200))
        p4.turn((0, 200))
        p5.turn((0, 200))
        p6.turn((0, 200))
        p7.turn((0, 200))
        p8.turn((0, 200))
        
        tu.up()
        s1.check_screen((0,0), (p1.point_coords[0], p1.point_coords[1]))
        tu.goto(s1.new_point_coords, 0)
        s1.check_screen((0,0), (50, p1.point_coords[1]))
        tu.goto(tu.xcor(), s1.new_point_coords)
        p1_save=(tu.xcor(), tu.ycor())
        tu.down()
        tu.dot(10, 'black')
        
        tu.up()
        s1.check_screen((0,0), (p2.point_coords[0], p2.point_coords[1]))
        tu.goto(s1.new_point_coords, 0)
        s1.check_screen((0,0), (50, p2.point_coords[1]))
        tu.goto(tu.xcor(), s1.new_point_coords)
        p2_save=(tu.xcor(), tu.ycor())
        tu.down()
        tu.dot(10, 'red')
        
        tu.up()
        s1.check_screen((0,0), (p3.point_coords[0], p3.point_coords[1]))
        tu.goto(s1.new_point_coords, 0)
        s1.check_screen((0,0), (50, p3.point_coords[1]))
        tu.goto(tu.xcor(), s1.new_point_coords)
        p3_save=(tu.xcor(), tu.ycor())
        tu.down()
        tu.dot(10, 'blue')
        
        tu.up()
        s1.check_screen((0,0), (p4.point_coords[0], p4.point_coords[1]))
        tu.goto(s1.new_point_coords, 0)
        s1.check_screen((0,0), (50, p4.point_coords[1]))
        tu.goto(tu.xcor(), s1.new_point_coords)
        p4_save=(tu.xcor(), tu.ycor())
        tu.down()
        tu.dot(10, 'green')
        
        tu.up()
        s1.check_screen((0,0), (p5.point_coords[0], p5.point_coords[1]))
        tu.goto(s1.new_point_coords, 0)
        s1.check_screen((0,0), (-50, p5.point_coords[1]))
        tu.goto(tu.xcor(), s1.new_point_coords)
        p5_save=(tu.xcor(), tu.ycor())

        tu.down()
        tu.dot(10, 'black')
        tu.up()
        s1.check_screen((0,0), (p6.point_coords[0], p6.point_coords[1]))
        tu.goto(s1.new_point_coords, 0)
        s1.check_screen((0,0), (-50, p6.point_coords[1]))
        tu.goto(tu.xcor(), s1.new_point_coords)
        p6_save=(tu.xcor(), tu.ycor())

        tu.down()
        tu.dot(10, 'red')
        tu.up()
        s1.check_screen((0,0), (p7.point_coords[0], p7.point_coords[1]))
        tu.goto(s1.new_point_coords, 0)
        s1.check_screen((0,0), (-50, p7.point_coords[1]))
        tu.goto(tu.xcor(), s1.new_point_coords)
        p7_save=(tu.xcor(), tu.ycor())

        tu.down()
        tu.dot(10, 'blue')
        tu.up()
        s1.check_screen((0,0), (p8.point_coords[0], p8.point_coords[1]))
        tu.goto(s1.new_point_coords, 0)
        s1.check_screen((0,0), (-50, p8.point_coords[1]))
        tu.goto(tu.xcor(), s1.new_point_coords)
        p8_save=(tu.xcor(), tu.ycor())
        tu.down()
        tu.dot(10, 'green')
        
        tu.up()
        tu.goto(p1_save[0], p1_save[1])
        tu.down()
        tu.goto(p2_save[0], p2_save[1])
        tu.goto(p3_save[0], p3_save[1])
        tu.goto(p4_save[0], p4_save[1])
        tu.goto(p1_save[0], p1_save[1])            
        tu.up()
        tu.goto(p5_save[0], p5_save[1])
        tu.down()
        tu.goto(p6_save[0], p6_save[1])
        tu.goto(p7_save[0], p7_save[1])
        tu.goto(p8_save[0], p8_save[1])
        tu.goto(p5_save[0], p5_save[1])
        
        tu.up()
        tu.goto(p5_save[0], p5_save[1])
        tu.down()
        tu.goto(p1_save[0], p1_save[1])
        tu.up()
        tu.goto(p6_save[0], p6_save[1])
        tu.down()
        tu.goto(p2_save[0], p2_save[1])
        tu.up()
        tu.goto(p7_save[0], p7_save[1])
        tu.down()
        tu.goto(p3_save[0], p3_save[1])
        tu.up()
        tu.goto(p8_save[0], p8_save[1])
        tu.down()
        tu.goto(p4_save[0], p4_save[1])
        
        tu.Screen().update()

while True:
    generate_cube1()

tu.Screen().update()