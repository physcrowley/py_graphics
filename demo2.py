from turtle import *

# Déclarations initiales, utiles partout
#########################################

# la fenêtre
wn = Screen()
wn.bgcolor("lightgreen")
wn.delay(20)

# la tortue
turtle = Turtle()
turtle.penup() # se déplacer sans laisser une trace

# Définitions de fonctions (instructions nommées)
##################################################

def turn_and_move(distance):
    """ Avance le nombre de pixels spécifiés par 'distance'
    et pivote 90 degrés vers la droite."""
    turtle.forward(distance)
    turtle.right(90)


def drawbox(side_length):
    """ Dessine une boîte en faisant 3 virages et 4 déplacements,
    chaque déplacement le nombre de pixels spécifiés par 'side_length'
    """
    for turns in range(3):
        turn_and_move(side_length)
    
    # dernier déplacement
    turtle.forward(side_length)


def four_boxes(x, y):
    """ Utilise les coordonnées x,y de la souris pour placer
    le centre de la forme, et dessine 4 boîtes de couleurs
    différentes."""

    turtle.setposition(x, y)

    #
    # Le dessin
    #

    turtle.pendown()
    
    for i in range(4):
        # chaque boîte, une couleur différente
        turtle.begin_fill()
        if i == 0:
            turtle.color("red")
        elif i == 1:
            turtle.color("blue")
        elif i == 2:
            turtle.color("orange")
        elif i == 3:
            turtle.color("yellow")
        drawbox(100)
        turtle.end_fill()
    
    turtle.penup()


# Programme principal
########################

# utiliser le clic de souris pour lancer le dessin
wn.onclick(four_boxes)

# garde la fenêtre ouverte indéfiniment
wn.mainloop()  
