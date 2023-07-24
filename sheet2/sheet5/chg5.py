from gasp import *


Sc_width = 640
Sc_lenght = 480
begin_graphics(Sc_width, Sc_lenght, title="Moving Circle", background=color.WHITE)


circle_radius = 10
circle_x = 150
circle_y = 110
move_direction = 20

def grid():
    for x in range(0,640,20):
        Line((x,0),(x,640),thickness=.01,color='lightgray')

    for y in range(0,480,20):
        Line((0,y),(640,y),thickness=.01,color='lightgray')

while True:
    clear_screen()
    grid()  
    Circle((circle_x, circle_y), circle_radius, filled=True, color=color.BLUE)

    key = update_when('key_pressed')
    key_alt = update_when('key_pressed')
    if key == 'Escape':  
        break
    elif key == 's':
        circle_y -= move_direction
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