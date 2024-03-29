import propagation_video_animation as pygame_file
import tkinter
import random

# Astuce : Si vous renommez le fichier tkinter, écrivez " importe <file_renommé> as pygame_file "
# De cette façon, vous n'avez pas besoin de changer tout le code tout en restant fonctionnel
# et ayant la possibilité de garder les fichiers dans le même dossier

#========================================================
#       F E N E T R E
#========================================================

app = tkinter.Tk()

app.title("Propagation d'une vidéo")
app.geometry("400x800+0+0")
app.configure(bg = "#123249")

#========================================================
#       A R R I E R E - P L A N
#========================================================

img  = tkinter.PhotoImage(file = "Images/data.gif")
canvas1 = tkinter.Canvas(app, width = 1080, height = 720)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image(-200, 0, image = img, anchor = "nw")   

#========================================================
#       C L A S S E S
#========================================================

class Nombre_Abonnes:
    def __init__(self):
        super().__init__()

        self.objectif = tkinter.Label(app, text="Nombre d'abonnés : ", font = ("Times 11"), bg = "#eaf2f8", highlightcolor = "#a2d9ce", height= 2, width = 25, borderwidth=3, relief="flat")
        self.entry = tkinter.Entry(app, font = ('Helvetica', 24), width = 5)
        self.parametre = 2

        self.objectif.place(x = 50, y = 60)
        self.entry.place(x = 260, y = 60)

    def confirmer(self):
        self.parametre = self.entry.get()
        if int_test(self.parametre) :
            print("Le créateur a", self.parametre, "abonnés")
        else :
            print("Par défaut, le créateur possède 1 abonné")

#------------------------------------

class Nombre_Utilisateurs:
    def __init__(self):
        super().__init__()

        self.objectif = tkinter.Label(app, text="Nombre d'utilisateurs : ", font = ("Times 11"), bg = "#eaf2f8", highlightcolor = "#a2d9ce", height= 2, width = 25, borderwidth=3, relief="flat")
        self.entry = tkinter.Entry(app, font = ('Helvetica', 24), width = 5)
        self.parametre = 150

        self.objectif.place(x = 50, y = 120)
        self.entry.place(x = 260, y = 120)

    def confirmer(self):
        self.parametre = self.entry.get()
        if int_test(self.parametre) :
            print("Il y a", self.parametre, "personnes dans ce monde")
        else :
            print("Par défaut, il y a 150 personnes dans ce monde")

#------------------------------------

class Objectif_Vues:
    def __init__(self):
        super().__init__()

        self.objectif = tkinter.Label(app, text="Objectif Nombre de vues :", font = ("Times 11"), bg = "#eaf2f8", highlightcolor = "#a2d9ce", height=2, width = 25, borderwidth=3, relief="flat")
        self.entry = tkinter.Entry(app, font = ('Helvetica', 24), width = 5)
        self.parametre = 500

        self.objectif.place(x = 50, y = 180)
        self.entry.place(x = 260, y = 180)

    def confirmer(self):
        self.parametre = self.entry.get()
        if int_test(self.parametre) :
            print("Objectif :", self.parametre, "vues")
        else :
            print("Par défaut, l'objectif est défini à 500 vues")

#------------------------------------

class Objectif_Likes:
    def __init__(self):
        super().__init__()

        self.objectif = tkinter.Label(app, text="Objectif Nombre de likes :", font = ("Times 11"), bg = "#eaf2f8", highlightcolor = "#a2d9ce", height=2, width = 25, borderwidth=3, relief="flat")
        self.entry = tkinter.Entry(app, font = ('Helvetica', 24), width = 5)
        self.parametre = 75

        self.objectif.place(x = 50, y = 240)
        self.entry.place(x = 260, y = 240)

    def confirmer(self):
        self.parametre = self.entry.get()
        if int_test(self.parametre) :
            print("Objectif :", self.parametre, "likes")
        else :
            print("Par défaut, l'objectif est défini à 75 likes")

#------------------------------------

class Objectif_Commentaires:
    def __init__(self):
        super().__init__()

        self.objectif = tkinter.Label(app, text="Objectif Nombre de commentaires :", font = ("Times 11"), bg = "#eaf2f8", highlightcolor = "#a2d9ce", height=2, width = 25, borderwidth=3, relief="flat")
        self.entry = tkinter.Entry(app, font = ('Helvetica', 24), width = 5)
        self.parametre = 50

        self.objectif.place(x = 50, y = 300)
        self.entry.place(x = 260, y = 300)

    def confirmer(self):
        self.parametre = self.entry.get()
        if int_test(self.parametre) :
            print("Objectif :", self.parametre, "commentaires")
        else :
            print("Par défaut, l'objectif est défini à 50 commentaires")      

#------------------------------------

class Objectif_Partages:
    def __init__(self):
        super().__init__()

        self.objectif = tkinter.Label(app, text="Objectif Nombre de partages :", font = ("Times 11"), bg = "#eaf2f8", highlightcolor = "#a2d9ce", height=2, width = 25, borderwidth=3, relief="flat")
        self.entry = tkinter.Entry(app, font = ('Helvetica', 24), width = 5)
        self.parametre = 25

        self.objectif.place(x = 50, y = 360)
        self.entry.place(x = 260, y = 360)

    def confirmer(self):
        self.parametre = self.entry.get()
        if int_test(self.parametre) :
            print("Objectif :", self.parametre, "partages")
        else :
            print("Par défaut, l'objectif est défini à 25 partages")

#------------------------------------

class Duree_Maximale:
    def __init__(self):
        super().__init__()

        self.objectif = tkinter.Label(app, text="Durée maximale :", font = ("Times 11"), bg = "#eaf2f8", highlightcolor = "#a2d9ce", height= 2, width = 25, borderwidth=3, relief="flat")
        self.entry = tkinter.Entry(app, font = ('Helvetica', 24), width = 5)
        self.parametre = self.entry.get()

        self.objectif.place(x = 50, y = 420)
        self.entry.place(x = 260, y = 420)

    def confirmer(self):
        self.parametre = self.entry.get()
        if int_test(self.parametre) :
            print("Dans", self.parametre, "secondes, c'est terminé")
        else :
            print("Par défaut, le temps n'est pas encore défini")


def int_test(testing):
    if len(testing) > 0 :
        for i in testing :
            if ord(i) >= 48 and ord(i) <= 57 :
                continue
            else :
                return False
    else :
        return False

    return True


#========================================================
#       C H A R G E M E N T   D E   C L A S S E S
#========================================================

nombre_abonnes = Nombre_Abonnes()
nombre_utilisateurs = Nombre_Utilisateurs()
objectif_vues = Objectif_Vues()
objectif_likes = Objectif_Likes()
objectif_commentaires = Objectif_Commentaires()
objectif_partages = Objectif_Partages()
duree_maximale = Duree_Maximale()

#========================================================
#       C O M M A N D E S
#========================================================

def allumer_pygame():
    nombre_utilisateurs.confirmer()
    nombre_abonnes.confirmer()
    objectif_vues.confirmer()
    objectif_likes.confirmer()
    objectif_commentaires.confirmer()
    objectif_partages.confirmer()
    duree_maximale.confirmer()
    pygame_file.animation_go()

def quitter_tkinter():
    return quit

#========================================================
#       B O U T O N S
#========================================================

tkinter.Button(canvas1, bg = "#a9cce3", text = "Start", command = allumer_pygame, font = 50).place(x = 100, y = 610)
tkinter.Button(canvas1, bg = "#a9cce3", text = "Quitter", command = quitter_tkinter(), font = 50).place(x = 100, y = 650)

#========================================================
#       M A I N L O O P
#========================================================


app.mainloop()

#========================================================
#       I N F O R M A T I O N S
#========================================================


"""

Liste de paramètres de statistiques à montrer au cours du temps :
- Durée actuelle
- Durée à l'échelle de tiktok

Qu'est-ce qui reste à faire ?
- Placer un Chronomètre
- Possibilité de stoper le chronomètre
- Possibilité d'afficher le temps (on commencera peut-être sur la console d'abord)
- Possibilité de contrôler deux fenêtres en même temps :
    - Soit on fait sur la fenêtre de paramétrage
    - Soit on place le chronomètre dans une nouvelle fenêtre

"""