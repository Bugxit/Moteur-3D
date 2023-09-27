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
    def check_point(self):
        tu.up()
        s1 = Spec((0, 0, 0), (100,100, 100), 90, 100)
        s1.check_screen((0,0), (p1.point_coords[0], p1.point_coords[1]))
        tu.goto(s1.new_point_coords, 0)
        s1.check_screen((0,0), (50, p1.point_coords[1]))
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
        
        p1.check_point()
        p2.check_point()
        p3.check_point()
        p4.check_point()
        p5.check_point()
        p6.check_point()
        p7.check_point()
        p8.check_point()

        tu.up()
        tu.goto(p1.save[0], p1.save[1])
        tu.down()
        tu.goto(p2.save[0], p2.save[1])
        tu.goto(p3.save[0], p3.save[1])
        tu.goto(p4.save[0], p4.save[1])
        tu.goto(p1.save[0], p1.save[1])            
        tu.up()
        tu.goto(p5.save[0], p5.save[1])
        tu.down()
        tu.goto(p6.save[0], p6.save[1])
        tu.goto(p7.save[0], p7.save[1])
        tu.goto(p8.save[0], p8.save[1])
        tu.goto(p5.save[0], p5.save[1])
        
        tu.up()
        tu.goto(p5.save[0], p5.save[1])
        tu.down()
        tu.goto(p1.save[0], p1.save[1])
        tu.up()
        tu.goto(p6.save[0], p6.save[1])
        tu.down()
        tu.goto(p2.save[0], p2.save[1])
        tu.up()
        tu.goto(p7.save[0], p7.save[1])
        tu.down()
        tu.goto(p3.save[0], p3.save[1])
        tu.up()
        tu.goto(p8.save[0], p8.save[1])
        tu.down()
        tu.goto(p4.save[0], p4.save[1])
        
        tu.Screen().update()
        ti.sleep(0.01)

while True:
    generate_cube1()

tu.Screen().update()