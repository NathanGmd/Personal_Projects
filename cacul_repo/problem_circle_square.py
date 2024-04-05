import math

def calcul_hight(angle):
    radiant_angle = math.radians(angle)
    cos_value = math.cos(radiant_angle)
    square_hight = 5 - ( cos_value * 5 )
    return round(square_hight, 2)

def calcul_length(angle):
    radiant_angle = math.radians(angle)
    sin_value = math.sin(radiant_angle)
    square_length = 10 - ( sin_value * 5 ) * 2
    return round(square_length, 2)

def egalite():
    angle = 0.1
    while calcul_length(angle) != calcul_hight(angle):
        angle += 0.01
    angle_result = angle
    return round( angle_result, 2 )

print ("Angle : ", egalite())
print ( "Hauteur carré : ", calcul_hight(egalite()), "Longeur carré : ", calcul_length(egalite()) )
