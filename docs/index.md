# Propagation d'une vidéo sur TikTok (Spread of a video on TikTok)

## Introduction

Avec la prolifération des réseaux sociaux, particulièrement dans le contexte de la crise sanitaire du COVID-19, il nous semble pertinent de traiter comment les plateformes s'adaptent à notre psychologie. Pour nous proposer des contenus qui nous intéressent, mais surtout pour nous inciter à rester le plus longtemps possible sur la plateforme comme source de revenus.

C'est pour ceci qu'on souhaite créer une modélisation de TikTok qui nous permettra d'étudier comment une vidéo se "propage" vers les utilisateurs de la plateforme. Cela dans le but de pouvoir illustrer la propagation d'une vidéo en particulier, et éventuellement les paramètres qui ont mené à son succès.

With the rapid spread of social media, particularly during the COVID-19 pandemic, it seems relevant to study how online platforms adapt themselves to our way of thinking, whether it's to recommend content or to encourage spending more time on their platform as a source of revenue.

This is why we are attempting to create a model of TikTok that would allow us to observe how a video spreads towards the platform's users, the end goal being to illustrate the spread of an individual video, and possibly the parameters that led to its success.

## Groupe

- Salwa MUJAHID
- Manissa BOUDA
- Adan ZERRAD
- Sebastian SZEBRAT

Nous sommes des étudiants en première année de licence à la Faculté de Sciences et d'Ingénierie de Sorbonne Université. 

## Blog

### Semaine 1 (du 09/03)

Nous avons présenté notre projet pendant la séance de mardi. Nos rôles dans la présentation :

- Salwa : Introduction
- Manissa : Explication de notre choix
- Adan : Comment nous allons procéder
- Salwa : À quoi ressemblera le rendu final ?
- Sebastian : Les résultats attendus

Nous avons ensuite défini plus explicitement notre approche au projet : on allait faire un système de recommandation, puis rajouter du code pour modéliser la propagation de notre vidéo.

**Sebastian Szebrat**

### Semaine 2 (du 15/03)

Débat sur la pertinence de l'approche choisi dans la dernière séance : 

Nous avons découvert que notre méthode conçue précedemment de faire un système de recommandation pour ensuite rajouter du code pour modéliser était trop complexe. 

Nous avions trouvé trois bibliothèques Python qui pouvaient nous aider à atteindre notre but : pandas (Python Data Analysis Library), PySpark (une interface pour Apache Spark, un moteur d'analyse complexes de données à grande échelle), et Surprise (une bibliothèque conçue directement pour créer et analyser des systèmes de recommandation). 

Ils présentaient tous le même défi : ils servent tous à analyser des ensembles de données gigantesques (non-disponible pour TikTok). On aurait dû changer notre projet à quelque-chose avec des ensembles disponibles, comme Netflix ou Spotify, mais le programme aurait été d'une complexité inabordable en un mois, inadapté alors à notre projet.

C'est alors qu'on a décidé de nous réorienter vers un pseudo système de recommandation.

Pour la prochaine séance, nous nous sommes laissés la tâche de finir notre débat et d'avoir une idée très claire des étapes de l'élaboration de notre pseudo système.

**Sebastian Szebrat**

### Semaine 3 (du 22/03)

Vu qu'on veut s'axer sur le point de vue de la propagation d'une vidéo vers des utilisateurs (content-based) et non pas des utilisateurs vers la vidéo (collaborative filtering), on s'est décidé de faire une simulation d'un système de recommandation basé sur le "content-based filtering". 

On prendra alors en paramètre pour les utilisateurs :

- les vidéos likées
- les vidéos partagées
- les comptes suivis
- les commentaires postés

Pour les vidéos, on prendra en compte :

- les hashtags
- l'audio sélectionné par le créateur

Le code sera divisé en quatre fonctions principales :

`base_videos` : crée et formatte une liste de tuples représentant chaque vidéo, comportant chacun les paramètres audio et hashtag, et un identifiant unique

`base_utilisateurs` : crée une liste de listes représentant chaque utilisateur

`tour_modele` : faire visionner une vidéo à chaque utilisateur et rajouter des intéractions à chacune -> comment les intéractions seront rajoutées à voir

`modelisation` : montrer le séquencement du modèle avec matplotlib, tkinter, pygame ou autre

**Sebastian Szebrat**

### Semaine 4 (du 29/03)

Nous avons rendu le carnet de bord sur Moodle pendant la semaine. Par la même occasion, nous avons pu commencer à faire des recherches à propos du projet.

A propos des fonctions principales, nous avons attribué à chaque personne une fonction principale parmis les 4 que nous avons listées pendant la semaine précédente :
- Adan : `base_videos`
- Manissa : `base_utilisateur`
- Sebastian : `tour_modele`
- Salwa : `modelisation`

Nous avons aussi un peu réfléchi sur le module que nous allons choisir pour illustrer la propagation. Nous avons décidé d’utiliser les modules `matplotlib` pour présenter les données chiffrées, `tkinter` pour créer des widgets et `pygame` pour faire des animations, mais cela dépend encore de l’avancement du projet.

Nous avons cherché des tutoriels pour `tkinter` et `pygame` sur Youtube, ainsi que les documentations associées.

Au niveau du code, nous avons terminé d’écrire la fonction `base_videos`. Nous avons également avancé pour la fonction `base_utilisateur`, mais il ne reste plus qu’à tester les fonctions pendant la séance en présentiel.

La difficulté était au niveau de l’importation du module `pygame`, car bien qu’il soit déjà installé, le compilateur ne reconnaît pas le module `pygame`.

**Salwa Mujahid**

### Semaine 5 (du 05/04)

Cette semaine, nous avons fini 2 fonctions que sont `base_video` et `base_utilisateur`. La fonction `base_video` renvoie une liste de tuples de type (int, str ,str ,str ) contenant un identifiant unique à chaque vidéo, un thème, une musique et un hashtag. Ces différents paramètres sont générés grâce à une technique de webscrapping (module beautifufulsoup) .La fonction `base_utilisateur` permet à l’aide de la fonction `base_video` d’assigner 3 listes à un nombre d’utilisateurs entrée un paramètre : une liste de vidéos likées, une liste de vidéos commentées et une liste de vidéos partagées.

Concernant la fonction `modelisation` nous avons déjà une idée et un schéma de la manière dont nous allons l’implémenter à l’aide du module Pygame. Nous savons également à peu près l’ensemble des paramètres que prendra en entrées cette fonction.

Cette semaine sera en grande partie dédiée à l’implémentation de la fonction principale : `tour_modele` qui sera probablement elle-même découpée en sous fonctions.

**Adan Zerrad**

### semaine 6 (du 12/04)

Pour cette semaine, on  a commencé par l’idée de définir la fonction `tour_modele`, et de la découper en sous fonctions.
La fonction `tour_modele`: consiste à faire visionner une vidéo à chaque utilisateur et ajouter des interactions.

Pendant qu’on réfléchissait aux sous fonctions, on s’est rendu compte qu’on s’est éloigné de l’objectif de départ, du coup on a dû modifier la base utilisateur pour rendre la suite des fonctions plus raisonnable et efficace. 

`Clarification :` 

Avant :

base_utilisateur : crée une liste de listes représentant chaque utilisateur, cette liste contient :
- identifiant_utilisateur.
- liked_videos : liste des vidéos likées.
- commented_videos : listes des vidéos commentées.
- shared_videos : listes des vidéos partagées. 
    
Après :

base_utilisateur :  crée une liste de Tuple de type :
- identifiant.
- liste musiques favoris.
- liste hashtags favoris.
- liste thèmes favoris.

Ces paramètres seront générés aléatoirement.

#### Les sous fonctions de tour_modele :

`interactions_video` : celle ci génère la liste des interactions (interaction video_utilisateur) c’est une liste qui a comme paramètres :
- identifiant_utilisateur. 
- liked_videos.
- commented_videos.
- shared_videos.
    
`gen_user_pref` : attribue des vidéos, thèmes préférés initialement.

`add_interaction` :  rajoute plus de vidéos selon les conditions définies par le modèle.
      
#### Les points sur lesquels nous avons pensés :

--comment recommander ou faire visionner une vidéo tiktok ?  

- En se basant sur les caractéristiques de la vidéo, on les compare avec les paramètres de l’utilisateur (audios favoris, hashtags favoris, thèmes favoris). Si une similarité a lieu, on attribue la vidéo à la liste des interactions correspondante, sinon pas d’attribution . 
      
--Les utilisateurs doivent-ils être dynamiques ?
   
- oui, il faut qu’on mette à jour constamment les préférences de l’utilisateur (introduire de nouveaux thèmes, sons et hashtags) afin que la propagation s'arrête au bout d’un moment).

--Quand est-ce que la propagation de la vidéo «VIDEO_1» s’arrête ?
   
- Proposition 1 : Celle-ci  s’arrête une fois qu’une autre vidéo «VIDEO_2» est plus virale «a plus d’interactions avec les utilisateurs »
- Proposition 2 : Celle-ci s’arrête après X temps .
         
#### En ce qui concerne l’animation :

on a beaucoup avancé cette semaine sur `pygame` et `tkinter` par rapport à la dernière fois :
- on a pu placer des individus de manière aléatoire dans l’animation.
- pour l’instant, l’animation est manuelle sur `pygame`. 
- on a réalisé des fonctions qui permettent l’interaction entre la vidéo qu’on déplace manuellement et les individus.

#### Ce nous devons faire :

- importer les bases `base_utilisateur`, `base_video` dans `pygame` pour attribuer un élément de la base  à chaque personne.
- Ajouter des commandes, des actions lorsqu’on valide les paramètres dans la fenêtre `tkinter`.
- Distancer les personnes pour avoir un rendu plus réaliste .
- Ajouter un graphique avec `tkinter` (pas encore sûr).

**Manissa Bouda**

### semaine 7/8 (du 17/04 au 03/05)

Ces deux dernières semaines nous avons effectuer quelques modifications sur les bases utilisateurs et vidéo, nous nous sommes en grande partie consacré à la finalisation de l’animation et à la préparation de l’oral .

Nous avons modifié le format de `base_utilisateur` et `base_video` afin de mieux les adapter à la mise en place de l’animation.

`base_utilisateur` crée un dictionnaire de liste de type :

•	identifiant.
•	liste musiques favoris.
•	liste hashtags favoris.
•	liste thèmes favoris

`base_video` se présente sous la forme d’une liste de liste:

•	identifiant 
•	nombre de like
•	nombre de commentaire
•	nombre de partage
•	thème de la video 
•	musique de la video 
•	hashtag de la video 

#### En ce qui concerne l’animation :

Nous avons automatisé le déplacement de la vidéo Tiktok vers les utilisateurs même s’il reste possible de le faire manuellement.
Les caractéristiques de chaque utilisateur qui  «visionne  » la vidéo ainsi que les caractéristiques de la vidéo (thème, musique, hashtag ) sont désormais affiché à gauche de l’écran.
Un système de visualisation temporelle à également été mis en place afin de savoir en combien de temps une vidéo a atteint un de ces objectifs de like , commentaire , partage entré en paramètre.
Un temps d’arrêt (en seconde) est également entrée en paramètres au cas ou la video n’obtiendrai jamais un de ces objectifs. 

#### En ce qui concerne la présentation oral :

Nous nous sommes répartir équitablement les différentes parties de la présentation afin de traiter les aspects les plus importants de notre modèle.
Nous avons également réalisé le diaporama ainsi qu’une video de présentation des principaux affichages et fonctionnalités de l’animation finale.

**Adan Zerrad**