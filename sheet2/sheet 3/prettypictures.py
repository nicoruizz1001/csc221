from gasp import * 
begin_graphics()
def printface(x, y):
    for u in x-40, x+40:
        Circle((u, y+20), 10)
    Circle((x,y), 100,)
    Line((x, y + 10), (x-20, y-30))
    Line((x-20, y - 30), (x+10, y-30))
    Arc((x, y-40), 30, 225, 315, color="red")
    for u in x-40, x+40: 
        Arc((u, y+30), 20, 30, 150, color="brown")


for col in range (40, 581, 80):
    for row in range(40, 440, 80):
        printface(col, row)

update_when('key_pressed')     
end_graphics() 
