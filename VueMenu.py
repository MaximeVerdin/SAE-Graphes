
import sys
from PyQt6.QtCore import QDate, pyqtSignal,QUrl
from PyQt6.QtWidgets import QComboBox, QLineEdit, QDateEdit, QTextEdit, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QCheckBox ,QPushButton,QStackedWidget
from PyQt6.QtGui import QDesktopServices


class VueMenu(QWidget):

    #signal

    ouvrirUrlClicked = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jeu de suguru")
        self.setStyleSheet("background-color: #C2C2C2")

        
        self.stack = QStackedWidget()
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.stack)

        # page pricipal du menu
        self.page1 = QWidget()
        vlayout1 = QVBoxLayout(self.page1)
        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        vlayout2 = QVBoxLayout()

        # Boutons page 1
        self.boutonRegle = QPushButton("Régle")
        self.boutonRegle.setStyleSheet("background-color: #AFAFAF;")
        self.boutonRegle.setFixedSize(80, 25)

        self.boutonJouer = QPushButton("Jouer")
        self.boutonJouer.setStyleSheet("background-color: #AFAFAF;")
        self.boutonJouer.clicked.connect(lambda: self.stack.setCurrentWidget(self.page3))

        self.boutonParam = QPushButton("Paramètre")
        self.boutonParam.setStyleSheet("background-color: #AFAFAF;")
        self.boutonParam.clicked.connect(lambda: self.stack.setCurrentWidget(self.page2))

        self.boutonQuitter = QPushButton("Quitter")
        self.boutonQuitter.setStyleSheet("background-color: #AFAFAF;")
        self.boutonQuitter.clicked.connect(self.close)

        # Placement page 1
        hlayout1.addWidget(self.boutonRegle)
        hlayout1.addStretch()

        vlayout2.addStretch(1)
        vlayout2.addWidget(self.boutonJouer)
        vlayout2.addWidget(self.boutonParam)
        vlayout2.addWidget(self.boutonQuitter)
        vlayout2.addStretch(1)

        vlayout1.addLayout(hlayout1)
        hlayout2.addLayout(vlayout2)
        vlayout1.addLayout(hlayout2)

        # page param
        self.page2 = QWidget()
        self.espace2 = QLabel(" ")
        vlayout_page2 = QVBoxLayout(self.page2)
        hlayout_centre2 = QHBoxLayout()
        vlayout_bouton2 = QVBoxLayout()

        self.boutonClair = QPushButton("Thème clair")
        self.boutonClair.setStyleSheet("background-color: #AFAFAF;")
        self.boutonClair.clicked.connect(self.themeClaire)

        self.boutonSombre = QPushButton("Thème sombre")
        self.boutonSombre.setStyleSheet("background-color: #AFAFAF;")
        self.boutonSombre.clicked.connect(self.themeSombre)

        self.boutonRetour2 = QPushButton("Retour")
        self.boutonRetour2.setStyleSheet("background-color: #AFAFAF;")
        self.boutonRetour2.clicked.connect(lambda: self.stack.setCurrentWidget(self.page1))

        vlayout_bouton2.addWidget(self.boutonClair)
        vlayout_bouton2.addWidget(self.boutonSombre)
        vlayout_bouton2.addWidget(self.boutonRetour2)

        hlayout_centre2.addStretch(1)
        hlayout_centre2.addLayout(vlayout_bouton2)
        hlayout_centre2.addStretch(1)

        vlayout_page2.addStretch(1)
        vlayout_page2.addWidget(self.espace2)
        vlayout_page2.addLayout(hlayout_centre2)
        vlayout_page2.addStretch(1)

        # page 3 jouer :
        self.page3 = QWidget()
        self.espace3 = QLabel(" ")
        vlayout_page3 = QVBoxLayout(self.page3)
        hlayout_centre3 = QHBoxLayout()
        vlayout_bouton3 = QVBoxLayout()

        self.boutonNouveau = QPushButton("Nouvelle partie")
        self.boutonNouveau.setStyleSheet("background-color: #AFAFAF;")

        self.boutonCharger = QPushButton("Charger partie")
        self.boutonCharger.setStyleSheet("background-color: #AFAFAF;")

        self.boutonRetour3 = QPushButton("Retour")
        self.boutonRetour3.setStyleSheet("background-color: #AFAFAF;")
        self.boutonRetour3.clicked.connect(lambda: self.stack.setCurrentWidget(self.page1))

        vlayout_bouton3.addWidget(self.boutonNouveau)
        vlayout_bouton3.addWidget(self.boutonCharger)
        vlayout_bouton3.addWidget(self.boutonRetour3)

        hlayout_centre3.addStretch(1)
        hlayout_centre3.addLayout(vlayout_bouton3)
        hlayout_centre3.addStretch(1)

        vlayout_page3.addStretch(1)
        vlayout_page3.addWidget(self.espace3)
        vlayout_page3.addLayout(hlayout_centre3)
        vlayout_page3.addStretch(1)

        # ajout dans le stacked widget
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)
        self.stack.addWidget(self.page3)

        self.show()

    def redimensionner_boutons(self):
        largeur = max(120, min(self.width() // 4, 600))
        hauteur = max(30, min(self.height() // 10, 150))

        for bouton in (
            self.boutonJouer,
            self.boutonParam,
            self.boutonQuitter,
            self.boutonClair,
            self.boutonSombre,
            self.boutonRetour2,
            self.boutonNouveau,
            self.boutonCharger,
            self.boutonRetour3
        ):
            bouton.setFixedSize(largeur, hauteur)

    def resizeEvent(self, event):
        self.redimensionner_boutons()
        super().resizeEvent(event)

    def themeClaire(self):
        with open(sys.path[0] + "/fichiers_qss/Integrid.qss", "r") as f:
            self.setStyleSheet(f.read())
            self.redimensionner_boutons()

    def themeSombre(self):
        with open(sys.path[0] + "/fichiers_qss/Combinear.qss", "r") as f:
            self.setStyleSheet(f.read())
            self.redimensionner_boutons()

    def ouvrir_url_regle(self):
        self.ouvrirUrlClicked.emit()


    def quitter_application(self):
        self.quitterAppClicked.emit()


    def param(self):
        self.ParamClicked.emit()

    def get_window_state(self):
        return {
            "geometry": self.saveGeometry(),
            "windowState": self.saveState()
        }

    def set_window_state(self, state):
        if "geometry" in state:
            self.restoreGeometry(state["geometry"])
        if "windowState" in state:
            self.restoreState(state["windowState"])










if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = VueMenu()
    sys.exit(app.exec())
