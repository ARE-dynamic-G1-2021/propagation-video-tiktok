## Blog

### Semaine 1 (du 09/03)

Nous avons présenté notre projet pendant la séance de mardi. Nos rôles dans la présentation :

- Salwa : Introduction
- Manissa : Explication de notre choix
- Adan : Comment nous allons procéder
- Salwa : À quoi ressemblera le rendu final ?
- Sebastian : Les résultats attendus

Nous avons ensuite défini plus explicitement notre approche au projet : on allait faire un système de recommandation, puis rajouter du code pour modéliser la propagation de notre vidéo.

### Semaine 2 (du 15/03)

Débat sur la pertinence de l'approche choisi dans la dernière séance : 

Nous avons découvert que notre méthode conçue précedemment de faire un système de recommandation pour ensuite rajouter du code pour modéliser était trop complexe. 

Nous avions trouvé trois bibliothèques Python qui pouvaient nous aider à atteindre notre but : pandas (Python Data Analysis Library), PySpark (une interface pour Apache Spark, un moteur d'analyse complexes de données à grande échelle), et Surprise (une bibliothèque conçue directement pour créer et analyser des systèmes de recommandation). 

Ils présentaient tous le même défi : ils servent tous à analyser des ensembles de données gigantesques (non-disponible pour TikTok). On aurait dû changer notre projet à quelque-chose avec des ensembles disponibles, comme Netflix ou Spotify, mais le programme aurait été d'une complexité inabordable en un mois, inadapté alors à notre projet.

C'est alors qu'on a décidé de nous réorienter vers un pseudo système de recommandation.

Pour la prochaine séance, nous nous sommes laissés la tâche de finir notre débat et d'avoir une idée très claire des étapes de l'élaboration de notre pseudo système.

### Semaine 3 (du 22/03)

Grâce à l'article de TikTok sur le fonctionnement de son algorithme, nous avons pu discerner deux approches vers les systèmes de recommandation : le "content-based filtering" et le "collaborative filtering".

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


### Semaine 5 (du 05/04)

Cette semaine, nous avons fini 2 fonctions que sont `base_video` et `base_utilisateur`. La fonction `base_video` renvoie une liste de tuples de type (int, str ,str ,str ) contenant un identifiant unique à chaque vidéo, un thème, une musique et un hashtag. Ces différents paramètres sont générés grâce à une technique de webscrapping (module beautifufulsoup) .La fonction `base_utilisateur` permet à l’aide de la fonction `base_video` d’assigner 3 listes à un nombre d’utilisateurs entrée un paramètre : une liste de vidéos likées, une liste de vidéos commentées et une liste de vidéos partagées.

Concernant la fonction `modelisation` nous avons déjà une idée et un schéma de la manière dont nous allons l’implémenter à l’aide du module Pygame. Nous savons également à peu près l’ensemble des paramètres que prendra en entrées cette fonction.

Cette semaine sera en grande partie dédiée à l’implémentation de la fonction principale : `tour_modele` qui sera probablement elle-même découpée en sous fonctions.


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
