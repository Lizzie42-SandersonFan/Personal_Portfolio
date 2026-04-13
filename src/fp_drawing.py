import turtle
from all_helpers import get_midpoint

def draw_fancy_triforce(the_turtle, position):
    the_turtle.up()
    the_turtle.goto(position[0][0], position[0][1])
    the_turtle.down()
    the_turtle.goto(position[1][0], position[1][1])
    the_turtle.goto(position[2][0], position[2][1])
    the_turtle.goto(position[0][0], position[0][1])

def recursive_draw(turt, tri_num, point):
        draw_fancy_triforce(turt, point)
        if tri_num > 1:
            recursive_draw(turt, tri_num-1, [point[0], get_midpoint(point[0], point[1]), get_midpoint(point[0], point[2])])
            recursive_draw(turt, tri_num-1, [point[1], get_midpoint(point[0], point[1]), get_midpoint(point[1], point[2])])
            recursive_draw(turt, tri_num-1, [point[2], get_midpoint(point[2], point[1]), get_midpoint(point[0], point[2])])
        else:
            return 1