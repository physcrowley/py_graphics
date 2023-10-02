# Module Turtle

## Installation
Aucune installation requise. Le module est inclus avec l'installation de Python.

## Utilisation

Voir les démonstrations pour quelques idées et pour la structure globale.

Première ligne, pour avoir accès aux objets prédéfinis :

```python
from turtle import *
```

Dernière ligne, pour garder la fenêtre ouverte :

* Fonctionne toujours :
    ```python
    mainloop()
    ```
* Fonctionne aussi si vous avez défini un objet Screen, p. ex. `wn = Screen()` :
    ```python
    wn.mainloop()
    ```
