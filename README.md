# Comment utiliser ce dépôt

- [OpenVNC](#openvnc-dans-un-codespace)
- [turtle](#module-turtle)

## OpenVNC dans un Codespace

Le mot de passe est `vscode`. Cela vous connectera au bureau de votre codespace et tout programme graphique y apparaîtera comme une nouvelle fenêtre. Vous pouvez développer le panneau OpenVNC en mode plein écran durant l'exécution du programme et le réduire par la suite pour travailler dans le code.

> Fonctionne bien **à la maison** et devrait fonctionner à l'école également. Par contre, à l'école c'est préférable de travailler dans une version locale de votre projet et d'utiliser le bureau des ordinateurs du laboratoire comme environnement graphique.

## Module Turtle

### Installation
Aucune installation requise. Le module est inclus avec l'installation de Python.

### Utilisation

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
