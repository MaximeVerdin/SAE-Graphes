import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QPushButton, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget

from Grille import Grille
from VueGrille import VueGrille


class VueJeux(QWidget):

    caseCliquee: pyqtSignal = pyqtSignal(int, int)  # x=col, y=ligne
    chiffreChoisi = pyqtSignal(int)
    sauvegarderClicked = pyqtSignal()
    accueilClicked = pyqtSignal()
    recommencerClicked = pyqtSignal()

    def __init__(self, grille: Grille):
        super().__init__()

        self.vue_grille = VueGrille(grille)

        # Boutons
        self.bouton_recommencer = QPushButton("Recommencer")
        self.bouton_recommencer.clicked.connect(self.recommencerClicked.emit)

        self.bouton_sauvegarder = QPushButton("Sauvegarder")
        self.bouton_sauvegarder.clicked.connect(self.sauvegarderClicked.emit)

        self.bouton_accueil = QPushButton("Accueil")
        self.bouton_accueil.clicked.connect(self.accueilClicked.emit)

        # Layout boutons
        self.layout_boutons = QHBoxLayout()

        self.layout_boutons.addWidget(self.bouton_recommencer)
        self.layout_boutons.addWidget(self.bouton_sauvegarder)
        self.layout_boutons.addWidget(self.bouton_accueil)


        self.widget_boutons = QWidget()
        self.widget_boutons.setLayout(self.layout_boutons)

        # Chiffres
        self.chiffres: list[QPushButton] = []

        # Layout chiffres
        self.layout_chiffres = QHBoxLayout()

        for i in range(1, self.vue_grille.getGrille().getTaillePlusGrandMotif()+1):
            self.chiffres.append(QPushButton(f"{i}"))
            self.layout_chiffres.addWidget(self.chiffres[i-1])

            self.chiffres[i-1].clicked.connect(lambda _, v=i: self.choisir_chiffre(v))

        self.widget_chiffres = QWidget()
        self.widget_chiffres.setLayout(self.layout_chiffres)

        # Layout principal
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.widget_boutons)
        self.layout.addWidget(self.vue_grille)
        self.layout.addWidget(self.widget_chiffres)

        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 5)
        self.layout.setStretch(2, 1)

        self.setLayout(self.layout)



        self.vue_grille.caseCliquee.connect(self.caseCliquee.emit)
        self.chiffreChoisi.connect(self.choisir_chiffre)

        self.show()

    def choisir_chiffre(self, valeur: int):
        self.chiffreChoisi.emit(valeur)

    def keyPressEvent(self, event):
        key = event.text()

        if key.isdigit():
            valeur = int(key)

            # option : filtrer selon taille max
            if 1 <= valeur <= len(self.chiffres):
                self.choisir_chiffre(valeur)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    g = Grille()
    g.chargerGrilleFromJson("grilles/grille1.json")

    window = VueJeux(g)
    sys.exit(app.exec())