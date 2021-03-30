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