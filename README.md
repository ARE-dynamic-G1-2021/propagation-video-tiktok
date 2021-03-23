# Propagation d'une vidéo sur TikTok (Spread of a video on TikTok)

## Introduction

Avec la prolifération des réseaux sociaux, particulièrement dans le contexte de la crise sanitaire du COVID-19, il nous semble pertinent de traiter comment les plateformes s'adaptent à notre psychologie. Pour nous proposer des contenus qui nous intéressent, mais surtout pour nous inciter à rester le plus longtemps possible sur la plateforme comme source de revenus.

C'est pour ceci qu'on souhaite créer une modélisation de TikTok qui nous permettra d'étudier comment une vidéo se "propage" vers les utilisateurs de la plateforme. Cela dans le but de pouvoir illustrer la propagation d'une vidéo en particulier, et éventuellement les paramètres qui ont mené à son succès.

With the rapid spread of social media, particularly during the COVID-19 pandemic, it seems relevant to study how online platforms adapt themselves to our way of thinking, whether it's to recommend content or to encourage spending more time on their platform as a source of revenue.

This is why we are attempting to create a model of TikTok that would allow us to observe how a video spreads towards the platform's users, the end goal being to illustrate the spread of an individual video, and possibly the parameters that led to its success.

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

Grâce a l'article de TikTok sur le fonctionnement de son algorithme, nous avons pu discerner deux approches vers les systèmes de recommandation : le "content-based filtering" et le "collaborative filtering".

Vu qu'on veut s'axer sur le point de vue de la propagation d'une vidéo vers des utilisateurs (content-based) et non pas des utilisateurs vers la vidéo (collaborative filtering), on s'est décidé de faire une simulation d'un système de recommandation basé sur le "content-based filtering". 

On prenda alors en paramètre pour les utilisateurs :

- les vidéos likées
- les videos partagées
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