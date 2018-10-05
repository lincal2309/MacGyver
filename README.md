
# MacGyver

Projet 3 - MacGyver

## Introduction

Ce jeu répond au projet 3 du parcours Développeur d'Application Python.
Il consiste à la programmer un labyrinthe dans lequel le joueur doit aider MacGyver à s'échapper, en ayant au préalable récupéré divers objets destinés à neutraliser le gardien qui l'attend à la sortie.

## Installation et pré-requis

L'utilisation de ce programme nécessite d'avoir Python3 installé ainsi qu'une console de commandes.

Pour utiliser le programme, procédez ainsi :

- Créez un environnement virtuel et activez-le
- Récupérez les fichiers du dépôt GitHub
- installez les dépendances du fichier requirements.txt

Le programme MacGyver.py peut alors être lancé.
Lorsque vous avez terminé, n'oubliez pas de désactiver votre environnement virtuel !

## Les différents fichiers

Programme principal : MacGyver.py
Fichiers de données : Donnees.py
Gestion du labyrinthe : labyrinth.py
Gestion de l'affichage : screen.py
Design patterns : observers.py
La grille définissant le labyrinthe : grille.txt
Informations sur le prgramme : le présent README.md
Lancement du programme en environnement virtuel : .gitignore et requirements.txt
Les différents fichier images sont dans le sous-répertoire Ressources.

Dépôt GitHub : [MacGyver](https://github.com/lincal2309/MacGyver.git)

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
Les premières étapes consistent à appréhender le module, créer une fenêtre, gérer les mouvements et les réponses aux touches du clavier.

### 4. Assemblage des "briques"

Après la mise en place de l'affichage à travers la classe screen, le fonctionnement est dévolu à une classe intermédiaire GameObjects pour tous les éléments du jeu ; une classe fille Persons est crée pour les personnage et la gestion de leurs déplacements.
Le lien entre la classe du labyrinthe et celle des objets est la position, gérée au travers d'une classe Places.
L'une des difficultés rencontrées a été de synchroiniser la gestion de la grille avec le mouvement des personnnage : un pattern observable est mis en place pour déclencher une méthode dans la calsse Labyrinthe lors d'un évènement de la classe Persons.
Néanmoins, choisir d'identifier les objets, en particulier les personnage, en tant que clé de la grille du labyrinthe pose certaines difficultés (identification du contenu d'un emplacement précis) et entraine des lourdeurs.

### 5. Premiers tests et résolution des dernières difficultés

Arrivé à un programme opérationnel, quelques points restaient en suspens : amélioration de l'affichage, gestion de la trasparence et synchronisation des actions. Sur ce dernier point, la coordination des classes "Personnages" et "Grille" posait problème.
La solution trouvé a consisté à refondre les classes pour gérer la grille avec, comme point d'entrée, les coordonnées dans la grille. La création d'un dictionnaire basé sur une telle clé, stockant le contenu de l'emplacement et l'image destinée à l'affichage, a permi de considérablement simplifier le programme, pour arriver à 2 classes principales : le labbyrinthe (gestion de la grille) et l'écran (gestion de l'affichage).
Cela a rendu le pattern observable caduqye pour la synchronisation des évènements de classes.

### 6. Finalisation et optimisation

Pour faciliter l'intégration des paramètres du jeu et la réuitilisation éventuelles des classes, le fichier de données est modifié pour définir une classe de ces paramètres. Celle-ci est définie sur le modèle du singleton (défini dans le fichier des modèles) puisqu'une seule instance suffit pour l'ensemble du jeu