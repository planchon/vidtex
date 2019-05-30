# VidTeX
Un logiciel permettant de créer des vidéos en python en utilisant LaTeX et les différentes technologies SVG.

## Installation
VidTex repose sur 3 technologies : `pdflatex`, `python3` et`ffmpeg`. Ces technologies sont indispensable au fonctionnement de VidTex. 

*Des technologies supplémentaires peuvent être requise lors de l'utilisation de paquet d'animation.*

## Utilisation
### Fonctionnement d'un projet
Un projet se compose d'un film, de plusieurs (ou non) scènes, contenant elle même plusieurs (ou non) animations.
Tout le projet se trouve dans un dossier, ce même dossier contient un fichier `movie_main.py` qui contient lui même la time-line du film.


```
FILM (movie_main.py)
 |
 |----> SCENE_1 (scene1.py)
 |       |----> animation_1 [de: 00s, à 15s]      
 |       |----> animation_2 [de: 05s, à 23s]
 |       |----> animation_3 [de: 23s, à 30s]
 |       |----> animation_4 [de: 02s, à 10s]
 |       |----> ...
 |       
 |----> SCENE_2 (scene2.py)
 |       |----> animation_1 [de: 01s, à 09s]      
 |       |----> animation_2 [de: 06s, à 40s]
 |       |----> animation_3 [de: 22s, à 23s]
 |       |----> animation_4 [de: 04s, à 11s]
 |       |----> ...
``` 

### Ajouter une scène / animation

Pour ajouter un objet de film (scène / animation), il suffit de l'ajouter à la timeline de la class dans laquel on se trouve (`Movie` ou `Scene`) en utilisant la fonction `prepare(self)` et en ajoutant l'objet grâce à `self.add_to_timeline(Object, Debut, Fin, ...)`. 

Le rendu se fait de façon automatique en suivant votre timeline.

###  Faire le rendu
Le rendu se fait sur le dossier du film. Utiliser la commande : 
```
./vidtex.py NOM_DU_DOSSIER
```
Si il n'y a pas d'erreur, vous verrez une barre de progression indiquant la durée restante de rendu. 

## Gestionnaire d'animation
Ce projet est avant tout **communautaire**. Les animations comprises dans le projet de base ne permettent que de faire des animations basiques. Cependant, un gestionnaire d'animation est proposé.

```
EN COURS DE REALISATION
```


## Licence
Copyright © Paul Planchon 2018
Vous pouvez utiliser / modifier ce logiciel si vous me citez dans votre logiciel. Les utilisations commerciales ne sont pas autorisées sans autorisation.