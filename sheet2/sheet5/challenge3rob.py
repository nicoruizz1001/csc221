from gasp import * 
from time import sleep

begin_graphics()
x = 5
y = 5
ball = Circle((x, y), 10, filled=True)
while y < 480:
    x += 4
    y += 3
    move_to(ball, (x, y))
    sleep(0.05) 
end_graphics()