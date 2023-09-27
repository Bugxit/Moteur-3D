import turtle as tu
import math as m
import time as ti

tu.Screen().tracer(0)

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
    while round(self.towards(screen_center_coords[0], screen_center_coords[1])) != self.rotation+90 and round(self.towards(screen_center_coords[0], screen_center_coords[1])) != self.rotation-90 and self.ycor() <= 540:
        self.seth(self.towards(temporary_point_coords[0], temporary_point_coords[1]))
        self.forward(1)
        self.seth(abs(m.floor(self.towards(screen_center_coords[0], screen_center_coords[1]))))
    self.new_point_coords.append(round(self.xcor()))
    tu.Screen().update()


S1 = Spec((0, 0, 0), (100,100, 100), 90, 100)
S1.check_screen((0,0), (100, 100))
S1.check_screen((0,0), (100, 100))
print(S1.new_point_coords)
tu.goto(S1.new_point_coords[0], S1.new_point_coords[1])
tu.dot(10)

S2 = Spec((0, 0, 0), (100,100, 200), 90, 100)
S2.check_screen((0,0), (100, 200))
S2.check_screen((0,0), (100, 200))
print(S2.new_point_coords)
tu.goto(S2.new_point_coords[0], S2.new_point_coords[1])
tu.dot(10)
tu.done()