import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QGuiApplication, QPainter
from PyQt6.QtWidgets import QWidget, QApplication
from Case_old import Case


class VueCase(QWidget):
    def __init__(self, taille: float = 5, case: Case = Case(0, 0, None)) -> None:
        """
        Créer le widget représentant une case
        :param taille: Un nombre donnant le pourcentage de l'écran occupé par une case
        """
        super().__init__()

        self.taille: float = min((QGuiApplication.primaryScreen().size().width() * taille / 100, QGuiApplication.primaryScreen().size().height() * taille / 100))
        self.case: Case = case

        self.setMinimumSize(QSize(int(self.taille)+1, int(self.taille)+1))


        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)

        cote = int(self.taille)

        x = (self.width() - cote) // 2
        y = (self.height() - cote) // 2

        painter.drawRect(x, y, cote, cote)

        texte: str = ""
        valeur: int | None = self.case.getContenu()
        if valeur:
            texte = str(valeur)

        painter.drawText(
            x, y, cote, cote,
            Qt.AlignmentFlag.AlignCenter,
            texte
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VueCase()
    sys.exit(app.exec())