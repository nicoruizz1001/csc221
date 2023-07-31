from gasp import *
import time
from random import randint


class Player:
    pass

class Robot:
    pass
player = Player()
robot = Robot()

player.x = randint(10,64)
player.y = randint(10,48)



robot.x = 63
robot.y = 40

def place_robot():
    global robot
    robot = Robot()
    robot.x = 63
    robot.y = 40
    robot.shape = Circle((robot.x, robot.y), 10, filled=True, color=color.RED)

def place_player():
    global player
    player = Player()
    player.x = randint(10,64)
    player.y = randint(10,48)


begin_graphics()

def move_player():
    global player, teleport
    key = update_when('key_pressed')

    if key == 'd' and player.x < 63:
        player.x += 1
    elif key == 'a' and player.x > 0:
        player.x -= 1
    elif key == 'w' and player.y < 46:
        player.y += 1
    elif key == 's' and player.y > 0.5:
        player.y -= 1
    elif key == 'c':
        if player.x < 63:
            player.x += 1
        if player.y > 0:
            player.y -= 1
    elif key == 'Shift_L':
        if player.x > 0:
            player.x -= 1
        if player.y > 0.5:
            player.y -= 1
    elif key == 'e':
        if player.x < 63:
            player.x += 1
        if player.y < 46:
            player.y += 1
    elif key == 'q':
        if player.x > 0:
            player.x -= 1
        if player.y < 46:
            player.y += 1
    move_to(player.shape, (10 * player.x + 5, 10 * player.y + 5))

teleport = 0 

def teleport_count():
    global teleport, player, key
    key = update_when('key_pressed')
    if teleport <= 5:
        if key == 'space':
            teleport += 1
            player.x = randint(10,64)
            player.y = randint(10,48)   

            


def move_robot():
    global player, robot

    if robot.x < player.x:
        robot.x += 1
    elif robot.x > player.x:
        robot.x -= 1

    if robot.y < player.y:
        robot.y += 1
    elif robot.y > player.y:
        robot.y -= 1

    move_to(robot.shape, (10 * robot.x + 5, 10 * robot.y + 5))

def check_collisions():
    global finished

    if player.x == robot.x and player.y == robot.y:
        finished = True
        clear_screen()
        Text("Game Over", (320, 240), size=20, color=color.BLUE) 
        sleep(3)

def collided():
    return player.x == robot.x and player.y == robot.y

def safely_place_player():
    global player
    while True:
        place_player()
        player.shape = Circle((player.x, player.y), 10, filled=True, color=color.BLUE)
        if not collided():
            break

place_robot()
safely_place_player() 
finished = False

while not finished:
    move_player()
    move_robot()
    check_collisions()
    teleport_count() 
end_graphics()