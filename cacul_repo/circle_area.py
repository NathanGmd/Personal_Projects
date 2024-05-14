import math

def find_y_bottom_circle():
    unknown_x = 4
    while unknown_x >= 0:
        y = math.sqrt( 4 * unknown_x - unknown_x ** 2 )
        print ("For x :", unknown_x, "y : ", y )
        unknown_x -= 0.1

# find_y_bottom_circle()

def find_y_bottom_circle():
    unknown_y = 0
    while unknown_y <= 2.1:
        x = math.sqrt( 4 * unknown_y - unknown_y ** 2 )
        print ("For y :", unknown_y, "x : ", x )
        unknown_y += 0.1


# find_y_bottom_circle()

def find_y_top_circle():
    unknown_x = 0
    while unknown_x <= 0:
        y = - math.sqrt( 16 - unknown_x ** 2)
        print ("For x :", unknown_x, "y : ", y )
        unknown_x -= 0.1

find_y_top_circle()


# print ("For x :", unknown_x, "y : ", find_y(unknown_x) )
# print (find_y())

# x = math.sqrt( ( 5 ** 2 ) - ( unknown_y ** unknown_y ) )
# y = math.sqrt( ( 5 ** 2 ) - ( unknown_x ** unknown_x ) )
