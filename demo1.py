from turtle import *

# variables

# format est : nom = valeur
# mécanisme : assigne la valeur en mémoire et on peut faire
# référence à cette valeur avec nom

angle = 100
distance = 10 

delay(50)  # nombre de ms entre les instructions


while angle > 20:
    forward(distance)
    left(angle)
    distance = distance + 3
    angle = angle - 3

mainloop() # garde la fenêtre ouverte
