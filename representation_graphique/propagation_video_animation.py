import tkinter_file3 as tkinter_file
import pygame
import random

"""
Astuce : Si vous renommez le fichier tkinter, écrivez " importe <file_renommé> as tkinter_file "
De cette façon, vous n'avez pas besoin de changer tout le code tout en restant fonctionnel
et ayant la possibilité de garder les fichiers dans le même dossier

"""

def animation_go():

    pygame.init() # initialiser les modules

    #========================================================
    #       V A R I A B L E S
    #========================================================

    #----------------------------
    # Données chiffrées
    #----------------------------
    resolution = (1400, 700)
    distance = 5

    #----------------------------
    # Générer une fenêtre
    #----------------------------
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    pygame.display.set_caption("Propagation Vidéo")

    #========================================================
    #       C L A S S E S
    #========================================================

    class Animation :
        def __init__(self):
            self.afficher_animation = False
            self.is_playing = False
            self.pressed = {}

            self.tiktok = TikTok()
            self.statistique = Statistique()
            self.commande = Commande()
            
            self.mission = False
            self.nombre_de_gens = 150
            self.objectif_vues = 500
            self.objectif_likes = 200
            self.objectif_commentaires = 100
            self.objectif_partages = 25
            self.objectifs()

        def afficher_pygame(self):
            self.afficher_animation = True

        def start(self):
            self.is_playing = True

        def objectifs(self):
            
            gens = tkinter_file.nombre_utilisateurs.parametre
            view = tkinter_file.objectif_vues.parametre
            likes = tkinter_file.objectif_likes.parametre
            comments = tkinter_file.objectif_commentaires.parametre
            shares = tkinter_file.objectif_partages.parametre

            if len(gens) > 0 and ord(gens) >= 49 and ord(gens) <= 57 :
                self.nombre_de_gens = int(view)
            if len(view) > 0 and ord(view) >= 49 and ord(view) <= 57 :
                self.objectif_vues = int(view)
            if len(likes) > 0 and ord(likes) >= 49 and ord(likes) <= 57 :
                self.objectif_likes = int(likes)
            if len(comments) > 0 and ord(comments) >= 49 and ord(comments) <= 57 :
                self.objectif_commentaires = int(comments)
            if len(shares) > 0 and ord(shares) >= 49 and ord(shares) <= 57 :
                self.objectif_partages = int(shares)
        
        def update(self):
            screen.blit(animation.tiktok.image, animation.tiktok.rect)
            if animation.pressed.get(pygame.K_RIGHT) and animation.tiktok.rect.x + animation.tiktok.rect.width < screen.get_width() :
                animation.tiktok.move_right()
            elif animation.pressed.get(pygame.K_LEFT) and animation.tiktok.rect.x > 0 :
                animation.tiktok.move_left()
            elif animation.pressed.get(pygame.K_DOWN) and animation.tiktok.rect.y + animation.tiktok.rect.height < screen.get_height() :
                animation.tiktok.move_down()
            elif animation.pressed.get(pygame.K_UP) and animation.tiktok.rect.y > 0 :
                animation.tiktok.move_up()
            i = 0
            while i < self.nombre_de_gens :
                commande.mission()
                if pygame.Rect.collidepoint(liste_collisions[i], (animation.tiktok.rect.x, animation.tiktok.rect.y)) and not self.mission:
                    print("Collision numéro", i)
                    animation.statistique.nombre_de_vues()
                    print("Nombre de vues actuel :", animation.statistique.vues)
                i += 1

    #-------------------------------------------------------------------------

    # Les fonctions supplémentaires (double move) permettent d'aller en diagonale, mais je n'ai pas réussi pour l'instant

    class TikTok :
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load('Images/tiktok-40p.png').convert_alpha()
            self.vitesse = 1
            self.rect = self.image.get_rect()
            self.rect.x = 1300
            self.rect.y = 600

        def move_right(self):
            self.rect.x += self.vitesse
        
        def move_left(self):
            self.rect.x -= self.vitesse
        
        def move_down(self):
            self.rect.y += self.vitesse
        
        def move_up(self):
            self.rect.y -= self.vitesse

        """
        def move_up_left(self):
            self.rect.x -= self.vitesse
            self.rect.y -= self.vitesse

        def move_up_right(self):
            self.rect.x += self.vitesse
            self.rect.y -= self.vitesse

        def move_down_left(self):
            self.rect.x -= self.vitesse
            self.rect.y += self.vitesse

        def move_down_right(self):
            self.rect.x += self.vitesse
            self.rect.y += self.vitesse
        """

    #-------------------------------------------------------------------------

    # Cette classe permet d'afficher les données chiffrées en haut à gauche de l'écran

    class Statistique :
        def __init__(self):
            super().__init__()
            self.vues = 0
            self.likes = 0
            self.commentaires = 0
            self.partages = 0

        def nombre_de_vues(self):
            self.vues += 1

        def nombre_de_likes(self):
            self.likes += 1

        def nombre_de_commentaires(self):
            self.commentaires += 1

        def nombre_de_partages(self):
            self.partages += 1

    #-------------------------------------------------------------------------

    # Lorsque animation.mission = True, ça veut dire que la mission est accomplie ^^

    class Commande :
        def __init__(self):
            super().__init__()
            self.launched = False

        def lancer(self):
            self.launched = True

        def mission(self):
            if animation.statistique.vues >= animation.objectif_vues and not animation.mission :
                print("Mission accomplie ! Le nombre de vues est atteint !")
                animation.mission = True
            elif animation.statistique.likes >= animation.objectif_likes and not animation.mission :
                print("Mission accomplie ! Le nombre de likes est atteint !")
                animation.mission = True
            elif animation.statistique.commentaires >= animation.objectif_commentaires and not animation.mission :
                print("Mission accomplie ! Le nombre de commentaires est atteint !")
                animation.mission = True
            elif animation.statistique.partages >= animation.objectif_partages and not animation.mission :
                print("Mission accomplie ! Le nombre de partages est atteint !")
                animation.mission = True

    #-------------------------------------------------------------------------

    class Couleur :
        def __init__(self):
            super().__init__()
            self.blue = (89, 152, 255)
            self.black = (0, 0, 0)
            self.white = (255, 255, 255)
            self.pink = (252, 142, 187)

    #-------------------------------------------------------------------------

    class Image :
        def __init__(self):
            super().__init__()
            self.background = pygame.image.load('Images/red-background.jpg').convert()
            self.personne = pygame.image.load('Images/personne-40p.png').convert_alpha()

    #-------------------------------------------------------------------------

    class Texte :
        def __init__(self):
            super().__init__()
            self.chargement_1 = "Chargement de l'Animation..."
            self.chargement_2 = "Récupération des données..."
            self.titre = "P r o p a g a t i o n   o f   T i k T o k   v i d e o   a n i m a t e d"

            self.instruction_1 = "Press SpaceBar to Start"
            self.instruction_2 = "Use Right, Left, Up and Down Arrows to Move"
            self.instruction_3 = "If you touch a human, the console prints a collide and a number"
            self.instruction_4 = "And the number of views increases"
            self.instruction_5 = "Your mission is to reach the goal (only of views, at least for now)"

            self.chronometre = 'O'.rjust(3)

    #-------------------------------------------------------------------------

    class Police :
        def __init__(self):
            super().__init__()
            self.arial = pygame.font.SysFont("arial", 30) # Police depuis le système
            self.last_dream = pygame.font.Font("Polices/Last-Dream.ttf", 50) # Police téléchargée

    #-------------------------------------------------------------------------

    class Redige :
        def __init__(self):
            super().__init__()
            self.chargement_1 = police.arial.render(texte.chargement_1, False, couleur.white)
            self.chargement_2 = police.arial.render(texte.chargement_2, False, couleur.white)

            self.titre = police.last_dream.render(texte.titre, True, couleur.white)
            self.titre_shadow = police.last_dream.render(texte.titre, True, couleur.black)

            self.instruction_1 = police.arial.render(texte.instruction_1, False, couleur.white)
            self.instruction_2 = police.arial.render(texte.instruction_2, False, couleur.white)
            self.instruction_3 = police.arial.render(texte.instruction_3, False, couleur.white)
            self.instruction_4 = police.arial.render(texte.instruction_4, False, couleur.white)
            self.instruction_5 = police.arial.render(texte.instruction_5, False, couleur.white)
        
    #========================================================
    #       C H A R G E R   L E S   C L A S S E S
    #========================================================

    animation = Animation()
    tiktok = TikTok()
    statistique = Statistique()
    commande = Commande()
    couleur = Couleur()
    texte = Texte()
    police = Police()
    image = Image()
    redige = Redige()

    #========================================================
    #       F O N C T I O N S
    #========================================================

    #----------------------------
    # Positions ordonnées
    #----------------------------

    def liste_positions_ordonnees(distance):
        """
        ----------------------------------------------------
        Retourne une liste de <nombre> (ici 250) positions ordonnées
        des nombres compris entre 0 à <nombre>  * <distance>
        ----------------------------------------------------
        nombre : nombre de positions à générer dans une liste (int)
        distance : distance entre les personnes horizontalement (en pixels) (int)
        ----------------------------------------------------
        """
        liste_positions = []
        i = 0
        while i < 250 * distance :
            liste_positions.append(i)
            i += distance
        return liste_positions

    #----------------------------
    # Positions aléatoires
    #----------------------------

    def liste_positions_aleatoires(nombre, distance):
        """
        ----------------------------------------------------
        Retourne une liste de <nombre> positions aléatoires des
        nombres compris entre 0 à <nombre> * <distance>
        ----------------------------------------------------
        nombre : nombre de positions à générer dans une liste (int)
        distance : distance entre les personnes (en pixels) (int)
        ----------------------------------------------------
        """
        liste_positions = liste_positions_ordonnees(distance)
        liste_pos_aleatoires = []
        population = 0

        while population < nombre :
            liste_pos_aleatoires.append(random.choice(liste_positions))
            population += 1
        
        return liste_pos_aleatoires

    #----------------------------
    # Stocker les positions
    #----------------------------

    liste_positions_1 = liste_positions_aleatoires(animation.nombre_de_gens, distance)
    liste_positions_2 = liste_positions_aleatoires(animation.nombre_de_gens, distance)

    #----------------------------
    # Générer des rectangles pour chaque humain
    #----------------------------

    def collide_human():
        liste_collide = []
        i = 0
        while i < animation.nombre_de_gens :
            liste_collide.append(pygame.Rect(liste_positions_1[i], liste_positions_2[i], 20, 20))
            i += 1
        return liste_collide

    liste_collisions = collide_human()

    #========================================================
    #       A F F I C H A G E
    #========================================================

    # Cette affichage n'apparaît pas parce qu'elle est trop rapide pour nous

    screen.fill(couleur.blue)

    screen.blit(redige.chargement_1, [100, 100])
    screen.blit(redige.chargement_2, [100, 130])

    pygame.display.flip()


    #========================================================
    #       B O U C L E    P R I N C I P A L E
    #========================================================

    #----------------------------
    # Maintenir la fenêtre ouverte
    #----------------------------
    
    launched = True

    while launched :

        #----------------------------
        # Arrière-plan
        #----------------------------
        screen.blit(image.background, (0, -20))

        #----------------------------
        # Textes
        #----------------------------
        screen.blit(redige.titre_shadow, [160, 105])
        screen.blit(redige.titre, [165, 100])
        screen.blit(redige.instruction_1, [200, 200])
        screen.blit(redige.instruction_2, [200, 250])
        screen.blit(redige.instruction_3, [200, 300])
        screen.blit(redige.instruction_4, [200, 350])
        screen.blit(redige.instruction_5, [200, 400])

        #----------------------------
        # Images
        #----------------------------
        i = 0
        while i < animation.nombre_de_gens :
            screen.blit(image.personne, [liste_positions_1[i], liste_positions_2[i]])
            i += 1

        #----------------------------
        # Evènements
        #----------------------------
        if animation.is_playing:
            animation.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                launched = False
                animation.commande.launched = False

            elif event.type == pygame.KEYDOWN:
                animation.pressed[event.key] = True

                if event.key == pygame.K_SPACE:
                    animation.start()

            elif event.type == pygame.KEYUP:
                animation.pressed[event.key] = False           

        #----------------------------
        # Mise à jour
        #----------------------------
        pygame.display.flip()

    #----------------------------
    # Décharger les modules standards
    #---------------------------- 

    pygame.quit()

    #========================================================
    #       I N F O R M A T I O N S    
    #========================================================
    
    """
    Tâches restantes :

    - Distancer les gens
    - Attribuer les identités et les listes aux gens
    - Lorsqu'un certain objectif est atteint, stopper le chronomètre
    - Afficher les statistiques et les objectifs
        - Soit dans la fenêtre du chronomètre
        - Soit dans cette fenêtre (animation)

    """

    #--------------------------------------------------------------

    """

    Quelques idées de fonctions :

    - distance_positions() : plus les gens sont proches au départ, plus ils sont serrés
    Plus, les personnes sont loins de tiktok, plus ils sont serrées
    Finalement, on devrait ne pas les distancer ?

    - attribuer_id() : qui donne un id à chaque personne
    C'est en partie déjà fait grâce au collide_human()

    - acivites_id() : liste d'activité à stocker pour chaque id (likes, comms, partages)

    - stocker_gens_ordre() : stocke les positions des personnes du plus loin au plus proche de tiktok,
    Placer les gens dans l'ordre, du plus proche au plus loin dans une liste (pour que tiktok les rejoigne)
    On suppose que x est prioritaire
    On peut utiliser la liste déjà ordonnée
    
    - avancer() : permet à tiktok d'avancer automatiquement selon les gens
    Faire avancer tiktok vers la liste où sa vidéo apparaît (dans l'ordre de stocker_gens_ordre())

    - chronomètre() : à notre échelle

    - temps() : en même temps que le chronomètre, cette durée doit être plus réaliste (semaines, mois, années etc.)

    ------------------------------------------------------------------------

    - Elle peut permettre en plus, de distancer les personnes entre elles
    pers1, pers2 et pers3 étaient des paramètres (int)

    def liste_positions_aleatoires():

        while population < nombre :
            aleatoire = random.choice(liste_positions)
            if aleatoire > pers_3 :
                liste_pos_aleatoires.append(aleatoire * 1.5)
            elif aleatoire > pers_2 :
                liste_pos_aleatoires.append(aleatoire * 1.2)
            elif aleatoire > pers_1 :
                liste_pos_aleatoires.append(aleatoire * 1)
            else :
                liste_pos_aleatoires.append(aleatoire / 2)
            #liste_pos_aleatoires.append(random.choice(liste_positions))
            population += 1
        return liste_pos_aleatoires

    ------------------------------------------------------------------------

    # Si on arrive pas à distancer les gens avec la fonction précédente...

    def distance_positions(liste1, liste2):

        liste_1_final = []
        for j in liste2:
            for i in liste1:
                if i > 500 and j > 500 :
                    liste_1_final.append(i*1.5)
                elif i > 300 and j > 300 :
                    liste_1_final.append(i*1.3)
                elif i > 200 and j > 200 :
                    liste_1_final.append(i*1.1)
                else :
                    liste_1_final.append(i)
        return liste_1_final

    liste_positions_1 = distance_positions(liste_positions_1, liste_positions_2)
    liste_positions_2 = distance_positions(liste_positions_2, liste_positions_1)

    ------------------------------------------------------------------------

    def attribuer_id():

        liste_id = []
        i = 0
        while i < nombre_de_gens :
            liste_id.append((i, (liste_positions_1[i], liste_positions_2[i])))
            i += 1
        return liste_id

    ------------------------------------------------------------------------

    # import time

    # Les variables du chronomètre :
    - 3, c'est juste l'endroit par rapport à x, rjust est facultatif
    - Je sais pas ce qu'est USEREVENT :')
    - 1000 c'est un intervalle, le compteur s'active tous les 1000 millisecondes

    clock = pygame.time.Clock()
    counter = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    # Celui-là, faut placer vers la fin de la boucle launched :

    screen.blit(pygame.font.SysFont('Consolas', 30).render(redige.chronometre, True, couleur.white), [32, 48])

    elif event.type == pygame.USEREVENT: 
        counter += 1
        redige.chronometre = str(counter)+" semaines".rjust(3) if counter < 52 else '1 An!'

    clock.tick(60)

    """

    #--------------------------------------------------------------

    """

    Quelques remarques par rapport au sujet :

        En réalité...
        Les vidéos populaires sont regardées par millions et non par centaines...
        On peut voir, commenter, partager plusieurs fois, mais on ne peut liker qu'une seule fois
        Là, au lieu d'une personne, on on peut faire comme si que c'était un groupe de personnes
        parce qu'on compte plus d'une vue pour une personne, c'est bizarre...

    """

    #--------------------------------------------------------------


    """
    Crédits :

        La police Last-dream a été téléchargée depuis ce site :
        https://www.dafont.com/last-dream.font

    """