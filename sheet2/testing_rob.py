from gasp import *


Sc_width = 640
Sc_lenght = 480
begin_graphics(Sc_width, Sc_lenght)


circle_radius = 10
circle_x = 150
circle_y = 110
move_direction = 20
player = Circle((circle_x, circle_y ), circle_radius, filled=True, color=color.BLUE)

def gamer_move():
    while True:

    key = update_when('key_pressed')
    if key == 'Escape':  
        break
    elif key == 's':
        move_to(player, (0, 20))
    elif key == 'w':
        circle_y += move_direction
    elif key == 'a':
        circle_x -= move_direction
    elif key == 'd':
        circle_x += move_direction
    elif key == 'e':
        circle_x += move_direction
        circle_y += move_direction 
    elif key == 'q':
        circle_x -= move_direction
        circle_y += move_direction
    elif key == 'c':
        circle_x += move_direction
        circle_y -= move_direction
    elif key == 'Shift_L':
        circle_x -= move_direction
        circle_y -= move_direction 

    

end_graphics()