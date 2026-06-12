import sys

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QPainter, QPen, QFont, QColor
from PyQt6.QtWidgets import QWidget, QApplication

from Grille import Grille


class VueGrille(QWidget):

    caseCliquee: pyqtSignal = pyqtSignal(int, int)  # x=col, y=ligne

    def __init__(self, grille: Grille):
        super().__init__()

        self.grille = grille
        self.marge = 20
        self.taille_case = 40

        self.case_selectionnee = None  # (x, y)

        self.setWindowTitle("Vue Grille")
        self.show()

    def resizeEvent(self, event):
        self.update()

    def getGrille(self) -> Grille:
        return self.grille

    def calculer_taille_case(self):
        cases = self.grille.getCases()

        if not cases:
            return 40

        max_x = max(c.x for c in cases) + 1  # colonnes
        max_y = max(c.y for c in cases) + 1  # lignes

        largeur = self.width() - 2 * self.marge
        hauteur = self.height() - 2 * self.marge

        return min(
            largeur // max_x,
            hauteur // max_y
        )

    def calculer_offset(self):
        cases = self.grille.getCases()

        if not cases:
            return 0, 0

        max_x = max(c.x for c in cases) + 1
        max_y = max(c.y for c in cases) + 1

        grille_w = max_x * self.taille_case
        grille_h = max_y * self.taille_case

        dx = (self.width() - grille_w) // 2
        dy = (self.height() - grille_h) // 2

        return dx, dy

    def paintEvent(self, event):
        painter = QPainter(self)

        self.taille_case = self.calculer_taille_case()
        dx, dy = self.calculer_offset()

        pen = QPen(Qt.GlobalColor.black)
        painter.setPen(pen)

        for case in self.grille.getCases():

            x = dx + case.x * self.taille_case
            y = dy + case.y * self.taille_case

            painter.drawRect(x, y, self.taille_case, self.taille_case)

            texte = "" if case.contenu is None else str(case.contenu)

            font = QFont()
            font.setPointSize(max(6, self.taille_case // 3))
            painter.setFont(font)

            painter.drawText(
                x,
                y,
                self.taille_case,
                self.taille_case,
                Qt.AlignmentFlag.AlignCenter,
                texte
            )

        if self.case_selectionnee is not None:

            sel_x, sel_y = self.case_selectionnee

            x = dx + sel_x * self.taille_case
            y = dy + sel_y * self.taille_case

            if not self.grille.getCase(self.case_selectionnee[0], self.case_selectionnee[1]).fixe:
                overlay = QColor(255, 165, 0, 100)
            else:
                overlay = QColor(255, 0, 0, 100)

            painter.fillRect(
                x,
                y,
                self.taille_case,
                self.taille_case,
                overlay
            )

        pen = QPen(Qt.GlobalColor.black)
        pen.setWidth(max(2, self.taille_case // 15))
        painter.setPen(pen)

        for motif in self.grille.getMotifs():

            positions = {(c.x, c.y) for c in motif.getCases()}

            for (x, y) in positions:

                px = dx + x * self.taille_case
                py = dy + y * self.taille_case
                w = self.taille_case
                h = self.taille_case

                if (x, y - 1) not in positions:
                    painter.drawLine(px, py, px + w, py)

                if (x, y + 1) not in positions:
                    painter.drawLine(px, py + h, px + w, py + h)

                if (x - 1, y) not in positions:
                    painter.drawLine(px, py, px, py + h)

                if (x + 1, y) not in positions:
                    painter.drawLine(px + w, py, px + w, py + h)

    def mousePressEvent(self, event):

        if event.button() != Qt.MouseButton.LeftButton:
            return

        x_click = event.position().x()
        y_click = event.position().y()

        dx, dy = self.calculer_offset()

        col = int((x_click - dx) // self.taille_case)
        row = int((y_click - dy) // self.taille_case)

        case = self.grille.getCase(col, row)

        if case is None:
            return

        pos = (col, row)

        if self.case_selectionnee == pos:
            self.case_selectionnee = None
        else:
            self.case_selectionnee = pos

        self.caseCliquee.emit(col, row)
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    g = Grille()
    g.chargerGrilleFromJson("grilles/grille1.json")

    window = VueGrille(g)
    sys.exit(app.exec())