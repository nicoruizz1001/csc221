from gasp import *   
x = 5
y = 5       # So that you can draw things
def place_player():
    print("Here I am!")
    ball = Circle((x, y), 10, filled=True)
begin_graphics()     

def move_player():
    global player_x, player_y, player_shape

    key = update_when('key_pressed')

    if key == '6' and player_x < 63:
        player_x += 1
    elif key == '3':
        if player_x < 63:
            player_x += 1
        if player_y > 0:
            player_y -= 1

    

    move_to(player_shape, (10 * player_x + 5, 10 * player_y + 5))


       # Create a graphics window
finished = False

place_player()

while not finished:
    move_player()





end_graphics()   