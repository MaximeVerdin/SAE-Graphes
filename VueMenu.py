
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QStackedWidget, QMainWindow

class VueMenu(QMainWindow):

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

        # Layout principal vertical (pour centrer verticalement)
        vlayout_page = QVBoxLayout(self.page2)

        # Layout horizontal pour centrer la colonne
        hlayout_center = QHBoxLayout()

        # Layout vertical contenant les 3 boutons
        vlayout_buttons = QVBoxLayout()

        self.boutonClair = QPushButton("Thème clair")
        self.boutonClair.setStyleSheet("background-color: #AFAFAF;")

        self.boutonSombre = QPushButton("Thème sombre")
        self.boutonSombre.setStyleSheet("background-color: #AFAFAF;")

        self.boutonRetour = QPushButton("Retour")
        self.boutonRetour.setStyleSheet("background-color: #AFAFAF;")
        self.boutonRetour.clicked.connect(lambda: self.stack.setCurrentWidget(self.page1))

        # Ajouter les boutons dans la colonne
        vlayout_buttons.addWidget(self.boutonClair)
        vlayout_buttons.addWidget(self.boutonSombre)
        vlayout_buttons.addWidget(self.boutonRetour)

        # Centrer horizontalement la colonne
        hlayout_center.addStretch(1)
        hlayout_center.addLayout(vlayout_buttons)
        hlayout_center.addStretch(1)

        # Centrer verticalement
        vlayout_page.addStretch(1)
        vlayout_page.addLayout(hlayout_center)
        vlayout_page.addStretch(1)

        
        # ajout dans le stacked widget
        self.stack.addWidget(self.page1)
        self.stack.addWidget(self.page2)

        self.show()

            
            
            
    def redimensionner_boutons(self):
        """Ajuste la taille des boutons en fonction de la taille de la fenêtre."""
        largeur = self.width() // 4   # moitié de la largeur de la fenêtre
        hauteur = self.height() // 10 # 1/10 de la hauteur de la fenêtre

        for bouton in (self.boutonJouer, self.boutonParam,self.boutonQuitter,self.boutonClair,self.boutonSombre,self.boutonRetour):
            bouton.setFixedSize(largeur, hauteur)

    def resizeEvent(self, event):
        """Appelé automatiquement à chaque redimensionnement."""
        self.redimensionner_boutons()
        super().resizeEvent(event)  
            
            
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