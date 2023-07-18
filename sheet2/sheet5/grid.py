from gasp import *          # So that you can draw things
from random import randint

def grid():
    for x in range(0,640,10):
        Line((x,0),(x,640),thickness=.01,color='lightgray')

    for y in range(0,480,10):
        Line((0,y),(640,y),thickness=.01,color='lightgray')

begin_graphics()
grid()
update_when('key_pressed')
end_graphics() 