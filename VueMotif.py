import sys

from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout

from Case import Case
from Motif import Motif
from VueCase import VueCase


class VueMotif(QWidget):
    def __init__(self, taille: float = 5, motif: Motif = Motif()) -> None:
        super().__init__()

        self.taille = taille
        self.motif = motif


        self.setWindowTitle("Vue Motif")

        self.layout = QGridLayout()

        for case in self.motif.getCases():
            self.layout.addWidget(VueCase(self.taille, case), case.getPosition()[0], case.getPosition()[1])



        self.setLayout(self.layout)

        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Motif de test
    motif = Motif()
    motif.ajouterCase(Case(0, 0, 1))
    motif.ajouterCase(Case(0, 1, 2))
    motif.ajouterCase(Case(1, 0, 3))

    window = VueMotif(motif = motif)
    sys.exit(app.exec())

