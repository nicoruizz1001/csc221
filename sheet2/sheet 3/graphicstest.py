from gasp import *

begin_graphics()
Line((290,190), (300, 210))
Line((290,190 ),(310, 190))
Circle((300, 200), 100)
Circle((270,220), 10)
Circle((330,220), 10)
Arc((300, 180), 30, 225, 315)

update_when('key_pressed')     
end_graphics()