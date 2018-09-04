# MacGyver
Projet 3 - MacGyver

## Introduction
Ce jeu répond au projet 3 du parcours Développeur d'Application Python.
Il consiste à la programmer un labyrinthe duquel le joueur doit aider MacGyver à s'échapper, en ayant au préalable récupérer divers objets destinés à neutraliser le gardien qui l'attend à la sortie.

## Les différents fichiers
Programme principal : MacGyver.py
Fichiers de données : Donnees.py
La grille définissant le labyrinthe : grille.txt
Les différents fichier images sont dans le sous-répertoire Ressources.

## Démarche de programmation
Quelques mots sur la démarche ayant mené au programme final.
### 1. Identification des classes et des principales difficultés
4 classes sont identifées au préalable ; à ce stade de la formation, le développement amènera à amender plus ou moins cette première ébauche.
Les classes préssenties sont :
- Le labyrinthe : sa structure, la gestion des différents emplacements (sous forme d'un dictionnaire, ou dune liste ?) en imaginant un développement ultérieur cela pourrait amener à créer une instance par niveau
- Les personnages : gestion des positions et mouvements
- Les positions : gestion des spécificités des emplacements pour le labyrinthes, un lien entre personnages et labirinthes qui comprendront un (ou plusieurs) attributs issus de cette classe.
- Les objets : classe similaire aux personnages pour gérer les objets. Pas sûr à 100% d'en avoir besoin

3 pans sont identifiés pour le développement :
- initialisation du jeu, en particuliuer modélisation et création de la grille à partir d'un fichier
- mise en place des apsects graphiques, des déplacements du personnage
- la dynamique du jeu, pour tenir compte de la grille et des règles complémentaires dans les mouvements des personnages.

### 2. Initialisation du jeu
Mise en place d'un fichier externe (Donnees.py) pour gérer les paramètres techniques ou déterminant les "règles" (comme la dimension du labyrinthe, la liste des objets, etc.
Initialisation du fichier principal MacGyver.py, création des classes.
Initialisation du code pour la création de la grille : lecture du fichier et mise en place des objets liés. Le principe retenu est de créer une liste dont chaque élément est une liste à 3 éléments : les 2 premiers sont les coordonnées de l'emplacement, le 3è définit son contenu. Par défaut, les contenus désignent soit un espace libre, soit la présence d'un mur.
MacGyver et le gardien sont référencés à l'entrée et à la sortie du labyrinthe.
Ensuite, les objets sont placés de façon aléatoire, à partir d'une liste temporaire créée contenant les emplacmeents libres.

Dans un premier temps, les fonctions sont créées hors classes. La transformation en méthode se fera ultérieurement, pour tenir compte des cpontraintes de l'utilisation du module graphique.

### 3. Ebauche graphique
Le module retenu avec le mentor est PyGame.
Dans la démarche de découverte du module et de propgrammation progressive au fur et à mesure de l'apprentissage, la dynamique est initialisée dans un fichier séparé qui sera réintégré au programme principal.
Les premières étapes consistent à appréhender le module, créer une fenêtre, gérer les mouvements et les réponses aux touches du clavier. Le cas échéant, les mouvements à la souris seront gérés dans un second temps.




