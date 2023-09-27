import turtle as t
import math as m

x_point = [100,100,-100,-100,100,100,-100,-100]
y_point = [100,-100,-100,100,100,-100,-100,100]
z_point = [100,100,100,100,200,200,200,200]
te = 90

new_x_dot = []
new_y_dot = []
new_variable_save = 0

negative = 0

t.Screen().tracer(0)

def transform(te, x_dot, y_dot, x_spec, y_spec):
    global new_variable_save
    global negative
    x_save = 0
    t.up()
    t.goto(x_spec, y_spec)
    t.down()
    while t.ycor() < y_dot:
        t.seth(te)
        t.forward(1)
        x_save = t.xcor()
    if t.xcor() < x_dot:
        negative = 1
    else:
        negative = -1
    stop = 0
    for i in range(80):
        t.goto(x_spec, y_spec)
        while t.ycor() < y_dot:
            t.seth(te-i*negative)
            t.forward(1)
        if abs(t.xcor()-x_dot) <= abs(t.xcor()-x_save) and stop == 0:
            new_variable_save = i
            stop = 1
        x_save = t.xcor()


for i in range(8):
    transform(90, x_point[i], z_point[i]*2, 0, 0)
    new_x_dot.append(new_variable_save*negative)
    transform(90, y_point[i], z_point[i]*2, 0, 0)
    new_y_dot.append(new_variable_save*negative)
print(new_x_dot, new_y_dot)


t.up()
t.goto(new_x_dot[0],new_y_dot[0])
for i in range(4):
    t.down()
    t.goto(new_x_dot[i],new_y_dot[i])
t.goto(new_x_dot[0],new_y_dot[0])

t.goto(new_x_dot[4],new_y_dot[4])
for i in range(4,8):
    t.down()
    t.goto(new_x_dot[i],new_y_dot[i])
t.goto(new_x_dot[4],new_y_dot[4])

t.Screen().update()
t.done()