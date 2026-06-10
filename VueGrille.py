import sys

from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout

from Case import Case
from Grille import Grille
from Motif import Motif
from VueMotif import VueMotif


class VueGrille(QWidget):
    def __init__(self, taille: float = 5, grille: Grille = Grille()):
        super().__init__()

        self.taille = taille
        self.grille = grille

        self.setWindowTitle("Vue Grille")

        self.setStyleSheet("background-color: rgb(240, 240, 240);")

        self.layout = QGridLayout()

        for motif in self.grille.getMotifs():
            self.layout.addWidget(VueMotif(taille, motif))

        self.setLayout(self.layout)


        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Motif de test
    motif1 = Motif()
    motif1.ajouterCase(Case(0, 0, 1))
    motif1.ajouterCase(Case(0, 1, 2))
    motif1.ajouterCase(Case(1, 0, 3))
    motif2 = Motif()
    motif2.ajouterCase(Case(0, 2, 1))
    motif2.ajouterCase(Case(1, 1, 2))
    motif2.ajouterCase(Case(1, 2, 3))
    grille = Grille()
    grille.addMotif(motif1)
    grille.addMotif(motif2)

    window = VueGrille(grille = grille)
    sys.exit(app.exec())

