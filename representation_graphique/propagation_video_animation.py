import tkinter_file4 as tkinter_file
import musique
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
    liste_freq_abonnes = [i for i in range(100)]
    liste_gens_supp = [i for i in range(50000)]

    #----------------------------
    # Générer une fenêtre
    #----------------------------
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    pygame.display.set_caption("Propagation Vidéo")

    #========================================================
    #       C L A S S E S
    #========================================================

    # Lorsque l'animation commence...

    class Animation :
        def __init__(self):
            self.afficher_animation = False
            self.is_playing = False
            self.pressed = {}

            self.tiktok = TikTok()
            self.statistique = Statistique()
            self.commande = Commande()
            
            self.mission = False
            self.abonnes = 1
            self.nombre_de_gens = 150
            self.objectif_vues = 500
            self.objectif_likes = 200
            self.objectif_commentaires = 100
            self.objectif_partages = 25

        def afficher_pygame(self):
            self.afficher_animation = True

        def start(self):
            self.is_playing = True
        
        def update(self):
            screen.blit(animation.tiktok.image, animation.tiktok.rect)
            if animation.pressed.get(pygame.K_RIGHT) and animation.tiktok.rect.x + animation.tiktok.rect.width < screen.get_width() :
                animation.tiktok.move_right()
            elif animation.pressed.get(pygame.K_LEFT) and animation.tiktok.rect.x > 0 :
                animation.tiktok.move_left()
            if animation.pressed.get(pygame.K_DOWN) and animation.tiktok.rect.y + animation.tiktok.rect.height < screen.get_height() :
                animation.tiktok.move_down()
            elif animation.pressed.get(pygame.K_UP) and animation.tiktok.rect.y > 0 :
                animation.tiktok.move_up()

            liste_collisions = collide_human(liste_positions_1, liste_positions_2)
            
            i = 0
            while i < self.nombre_de_gens :
                commande.mission()
                if pygame.Rect.collidepoint(liste_collisions[i], (animation.tiktok.rect.x, animation.tiktok.rect.y)) and not self.mission:
                    animation.statistique.nombre_de_vues()
                if event.type == pygame.MOUSEMOTION :
                    if pygame.Rect.collidepoint(liste_collisions[i], event.pos) :
                        texte.humain = "Human selected : " + str(i)
                        redige.humain = police.arial_20.render(texte.humain, True, couleur.white)
                i += 1

    #-------------------------------------------------------------------------

    # Le mouvement de Tiktok

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

    #-------------------------------------------------------------------------

    class Id_User_Video :
        def __init__(self):
            super().__init__()
            self.liste_videos = musique.musiques()
            self.video = random.choice(self.liste_videos)

    #-------------------------------------------------------------------------

    # Les textes affichés en haut à gauche

    class Statistique :
        def __init__(self):
            super().__init__()
            self.abonnes = 2
            self.vues = 0
            self.likes = 0
            self.commentaires = 0
            self.partages = 0

        def nombre_abonnes(self):
            if random.choice(liste_freq_abonnes) == 1 :
                self.abonnes += random.randrange(self.abonnes)
                texte.abonnes = "Number of followers : " + str(self.abonnes)
                redige.abonnes = police.arial_20.render(texte.abonnes, True, couleur.white)

        def nombre_de_vues(self):
            self.vues += 1
            texte.vues = "Number of views : " + str(self.vues)
            redige.vues = police.arial_20.render(texte.vues, True, couleur.white)
            self.nombre_abonnes()

        def nombre_de_likes(self):
            self.likes += 1
            texte.vues = "Number of likes : " + str(self.likes)
            redige.vues = police.arial_20.render(texte.vues, True, couleur.white)

        def nombre_de_commentaires(self):
            self.commentaires += 1
            texte.vues = "Number of comments : " + str(self.commentaires)
            redige.vues = police.arial_20.render(texte.vues, True, couleur.white)

        def nombre_de_partages(self):
            self.partages += 1
            texte.vues = "Number of shares : " + str(self.partages)
            redige.vues = police.arial_20.render(texte.vues, True, couleur.white)

    #-------------------------------------------------------------------------

    # Lorsque animation.mission = True, ça veut dire que la mission est accomplie ^^

    class Commande :
        def __init__(self):
            super().__init__()

        def mission(self):
            if animation.statistique.vues >= animation.objectif_vues and not animation.mission :
                texte.mission_vues = "Mission accomplie ! Le nombre de vues est atteint !"
                redige.mission_vues = police.arial_20.render(texte.mission_vues, True, couleur.white)
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
            self.titre = "Propagation of Tiktok video animated"

            self.instruction_1 = "Press SpaceBar to Start"
            self.instruction_2 = "Use Right, Left, Up and Down Arrows to Move"
            self.instruction_3 = "If you touch a human, the output prints a collide and a number"
            self.instruction_4 = "And the number of views increases"
            self.instruction_5 = "Your mission is to reach the goal (only of views, at least for now)"
            self.instruction_6 = "Put your mouse on one of the human to see his id"

            #_____________________________

            current_followers = tkinter_file.nombre_abonnes.parametre
            current_people = tkinter_file.nombre_utilisateurs.parametre
            views_goal = tkinter_file.objectif_vues.parametre
            likes_goal = tkinter_file.objectif_likes.parametre
            comments_goal = tkinter_file.objectif_commentaires.parametre
            shares_goal = tkinter_file.objectif_partages.parametre

            #_____________________________

            try :
                self.abonnes = "Number of followers : " + str(current_followers)
                animation.abonnes = int(current_followers)
            except :
                self.abonnes = "Number of followers : " + str(statistique.abonnes)

            try :
                self.nombre_de_gens = "Number of people here : " + str(current_people)
            except :
                self.nombre_de_gens = "Number of people here : " + str(animation.nombre_de_gens)

            self.duree = "Time limit : "
            self.vues = "Number of views : " + str(statistique.vues)
            self.likes = "Number of likes : " + str(statistique.likes)
            self.commentaires = "Number of comments : " + str(statistique.commentaires)
            self.partages = "Number of shares : " + str(statistique.partages)

            #_____________________________

            try :
                self.objectif_vues = "Views goal : " + str(views_goal)
                animation.objectif_vues = int(views_goal)
            except :
                self.objectif_vues = "Views goal : " + str(animation.objectif_vues)

            try :
                self.objectif_likes = "Likes goal : " + str(likes_goal)
                animation.objectif_likes = int(likes_goal)
            except :
                self.objectif_likes = "Likes goal : " + str(animation.objectif_likes)

            try :
                self.objectif_commentaires = "Comments goal : " + str(comments_goal)
                animation.objectif_commentaires = int(comments_goal)
            except :
                self.objectif_commentaires = "Comments goal : " + str(animation.objectif_commentaires)

            try :
                self.objectif_partages = "Shares goal : " + str(shares_goal)
                animation.objectif_partages = int(shares_goal)
            except :
                self.objectif_partages = "Shares goal : " + str(animation.objectif_partages)

            #_____________________________

            self.mission_vues = ""
            self.theme_video = "Theme of the Video : "
            self.musique_video = "Music Used : "
            self.hashtag_video = "Hashtag : "
            self.humain = "Human selected :"


    #-------------------------------------------------------------------------

    class Police :
        def __init__(self):
            super().__init__()
            self.arial_30 = pygame.font.SysFont('arial', 30)
            self.arial_20 = pygame.font.SysFont('arial', 20)
            self.cookie_regular = pygame.font.Font('Polices/Cookie-Regular.ttf', 60)

    #-------------------------------------------------------------------------

    class Redige :
        def __init__(self):
            super().__init__()
            self.chargement_1 = police.arial_30.render(texte.chargement_1, False, couleur.white)
            self.chargement_2 = police.arial_30.render(texte.chargement_2, False, couleur.white)

            self.titre = police.cookie_regular.render(texte.titre, True, couleur.white)
            self.titre_shadow = police.cookie_regular.render(texte.titre, True, couleur.black)

            self.instruction_1 = police.arial_30.render(texte.instruction_1, False, couleur.white)
            self.instruction_2 = police.arial_30.render(texte.instruction_2, False, couleur.white)
            self.instruction_3 = police.arial_30.render(texte.instruction_3, False, couleur.white)
            self.instruction_4 = police.arial_30.render(texte.instruction_4, False, couleur.white)
            self.instruction_5 = police.arial_30.render(texte.instruction_5, False, couleur.white)
            self.instruction_6 = police.arial_30.render(texte.instruction_6, False, couleur.white)

            #_____________________________

            self.abonnes = police.arial_20.render(texte.abonnes, True, couleur.white)
            self.nombre_de_gens = police.arial_20.render(texte.nombre_de_gens, True, couleur.white)
            self.duree = police.arial_20.render(texte.duree, True, couleur.white)

            self.vues = police.arial_20.render(texte.vues, True, couleur.white)
            self.likes = police.arial_20.render(texte.likes, True, couleur.white)
            self.commentaires = police.arial_20.render(texte.commentaires, True, couleur.white)
            self.partages = police.arial_20.render(texte.partages, True, couleur.white)

            self.objectif_vues = police.arial_20.render(texte.objectif_vues, True, couleur.white)
            self.objectif_likes = police.arial_20.render(texte.objectif_likes, True, couleur.white)
            self.objectif_commentaires = police.arial_20.render(texte.objectif_commentaires, True, couleur.white)
            self.objectif_partages = police.arial_20.render(texte.objectif_partages, True, couleur.white)

            #_____________________________

            self.mission_vues = police.arial_20.render(texte.mission_vues, True, couleur.white)
            self.theme_video = police.arial_20.render(texte.theme_video, True, couleur.white)
            self.musique_video = police.arial_20.render(texte.musique_video, True, couleur.white)
            self.hashtag_video = police.arial_20.render(texte.hashtag_video, True, couleur.white)
            self.humain = police.arial_20.render(texte.humain, True, couleur.white)



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

        while population <= nombre :
            liste_pos_aleatoires.append(random.choice(liste_positions))
            population += 1
        
        return liste_pos_aleatoires

    #----------------------------
    # Générer des rectangles pour chaque humain
    #----------------------------

    def collide_human(liste_1, liste_2):
        liste_collide = []
        i = 0
        while i < animation.nombre_de_gens :
            liste_collide.append(pygame.Rect(liste_1[i], liste_2[i], 20, 20))
            i += 1
        return liste_collide

    #----------------------------
    # Stocker les positions
    #----------------------------

    liste_positions_1 = liste_positions_aleatoires(animation.nombre_de_gens, distance)
    liste_positions_2 = liste_positions_aleatoires(animation.nombre_de_gens, distance)
    liste_collisions = collide_human(liste_positions_1, liste_positions_2)

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
    
    launched = True

    while launched :

        #----------------------------
        # Arrière-plan
        #----------------------------

        screen.blit(image.background, (0, -20))
        
        #----------------------------
        # Textes Description
        #----------------------------

        screen.blit(redige.titre_shadow, [220, 155])
        screen.blit(redige.titre, [225, 150])
        screen.blit(redige.instruction_1, [260, 250])
        screen.blit(redige.instruction_2, [260, 300])
        screen.blit(redige.instruction_3, [260, 350])
        screen.blit(redige.instruction_4, [260, 400])
        screen.blit(redige.instruction_5, [260, 450])
        screen.blit(redige.instruction_6, [260, 500])

        #----------------------------
        # Images
        #----------------------------

        i = 0
        while i < animation.nombre_de_gens :
            screen.blit(image.personne, [liste_positions_1[i], liste_positions_2[i]])
            i += 1

            if random.choice(liste_gens_supp) == 1 and not animation.mission :
                animation.nombre_de_gens += 1
                liste_positions_1 += liste_positions_aleatoires(1, distance)
                liste_positions_2 += liste_positions_aleatoires(1, distance)

        #----------------------------
        # Textes Statistique
        #----------------------------

        # un chrono en secondes ici ? [30, 10]
        # un chrono en semaines ici ? [30, 30]

        screen.blit(redige.duree, [30, 80]) # en secondes
        screen.blit(redige.abonnes, [30, 110])

        screen.blit(redige.vues, [30, 140])
        screen.blit(redige.objectif_vues, [30, 160])

        screen.blit(redige.likes, [30, 190])
        screen.blit(redige.objectif_likes, [30, 210])

        screen.blit(redige.commentaires, [30, 240])
        screen.blit(redige.objectif_commentaires, [30, 260])

        screen.blit(redige.partages, [30, 290])
        screen.blit(redige.objectif_partages, [30, 310])

        #----------------------------
        # Textes Informations
        #----------------------------

        screen.blit(redige.mission_vues, [450, 20])

        screen.blit(redige.theme_video, [30, 570])
        screen.blit(redige.musique_video, [30, 590])
        screen.blit(redige.hashtag_video, [30, 610])

        screen.blit(redige.humain, [30, 650])

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

    texte.chronometre = 'O'.rjust(3) (dans la class Texte)

    # Les variables du chronomètre :
    - 3, c'est juste l'endroit par rapport à x, rjust est facultatif
    - 1000 c'est un intervalle, le compteur s'active tous les 1000 millisecondes

    clock = pygame.time.Clock()
    counter = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    # Celui-là, il faut placer vers la fin de la boucle launched :

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

        La police Cookie-Regular a été téléchargée depuis ce site :
        https://fonts.google.com/specimen/Cookie#standard-styles

    """