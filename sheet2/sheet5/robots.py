from gasp import *
import time
from random import randint

player_x = randint(10,64)
player_y = randint(10,48)



robot_x = 63
robot_y = 40

def place_robot():
    global robot_x, robot_y, robot_shape
    robot_shape = Circle((robot_x, robot_y), 10, filled=True, color=color.RED)

def place_player():
    global player_x, player_y, player_shape
    player_shape = Circle((player_x, player_y), 10, filled=True, color=color.BLUE)

begin_graphics()

def move_player():
    global player_x, player_y, player_shape, teleport
    key = update_when('key_pressed')

    if key == 'd' and player_x < 63:
        player_x += 1
    elif key == 'a' and player_x > 0:
        player_x -= 1
    elif key == 'w' and player_y < 46:
        player_y += 1
    elif key == 's' and player_y > 0.5:
        player_y -= 1
    elif key == 'c':
        if player_x < 63:
            player_x += 1
        if player_y > 0:
            player_y -= 1
    elif key == 'Shift_L':
        if player_x > 0:
            player_x -= 1
        if player_y > 0.5:
            player_y -= 1
    elif key == 'e':
        if player_x < 63:
            player_x += 1
        if player_y < 46:
            player_y += 1
    elif key == 'q':
        if player_x > 0:
            player_x -= 1
        if player_y < 46:
            player_y += 1
    move_to(player_shape, (10 * player_x + 5, 10 * player_y + 5))

teleport = 0 

def teleport_count():
    global teleport, player_x, player_y, key
    key = update_when('key_pressed')
    if teleport <= 5:
        if key == 'space':
            teleport += 1
            player_x = randint(10,64)
            player_y = randint(10,48)   

            


def move_robot():
    global player_x, player_y, robot_x, robot_y

    if robot_x < player_x:
        robot_x += 1
    elif robot_x > player_x:
        robot_x -= 1

    if robot_y < player_y:
        robot_y += 1
    elif robot_y > player_y:
        robot_y -= 1

    move_to(robot_shape, (10 * robot_x + 5, 10 * robot_y + 5))

def check_collisions():
    global finished

    if player_x == robot_x and player_y == robot_y:
        finished = True
        clear_screen()
        Text("Game Over", (320, 240), size=20, color=color.BLUE) 
        sleep(3)

def collided():
    return player_x == robot_x and player_y == robot_y

def safely_place_player():
    place_player()

    while collided():
        place_player()

place_robot()
safely_place_player()
finished = False

while not finished:
    move_player()
    move_robot()
    check_collisions()
    teleport_count() 
end_graphics()