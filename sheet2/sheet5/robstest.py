from gasp import *


Sc_width = 640
Sc_lenght = 480
begin_graphics(Sc_width, Sc_lenght)


circle_radius = 10
circle_x = 150
circle_y = 110
move_direction = 20

def grid():
    for x in range(0,640,20):
        Line((x,0),(x,640),thickness=.01,color='lightgray')

    for y in range(0,480,20):
        Line((0,y),(640,y),thickness=.01,color='lightgray')

def gamer():
 
    key = update_when('key_pressed') 
    global player 
    player = Circle((circle_x, circle_y), circle_radius, filled=True, color=color.BLUE)  
    if key == 's':
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
    remove_from_screen(player) 
    return
def rob_ots():
    global player
    grid()
    playing = True
    while playing:
        gamer()


rob_ots()
end_graphics()
    
