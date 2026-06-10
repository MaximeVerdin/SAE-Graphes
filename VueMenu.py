
import sys
from PyQt6.QtCore import QDate, pyqtSignal,QUrl
from PyQt6.QtWidgets import QComboBox, QLineEdit, QDateEdit, QTextEdit, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QCheckBox ,QPushButton
from PyQt6.QtGui import QDesktopServices




class VueMenu(QWidget): 
    
        
        
        
        def __init__(self): 
            super().__init__()
            

            self.setWindowTitle("Jeu de suguru")
            self.setStyleSheet("background-color: #C2C2C2")
            vlayout1 = QVBoxLayout();self.setLayout(vlayout1)
            hlayout1 = QHBoxLayout()
            hlayout2 = QHBoxLayout()
            vlayout2 = QVBoxLayout()
            
            self.boutonRegle = QPushButton("Régle")
            self.boutonRegle.setStyleSheet("background-color: #AFAFAF;")
            self.boutonRegle.setFixedSize(80, 25)
            self.boutonRegle.clicked.connect(self.ouvrir_url_regle)
            
            self.boutonJouer = QPushButton("Jouer")
            self.boutonJouer.setStyleSheet("background-color: #AFAFAF;")
            
            self.boutonParam = QPushButton("Paramètre")
            self.boutonParam.setStyleSheet("background-color: #AFAFAF;")
            self.boutonParam.clicked.connect(self.param)

            
            self.boutonQuitter = QPushButton("Quitter")
            self.boutonQuitter.setStyleSheet("background-color: #AFAFAF;")
            self.boutonQuitter.clicked.connect(self.quitter_application)

            
            #ajout des widget
            hlayout1.addWidget(self.boutonRegle)
            hlayout1.addStretch()
            
            vlayout2.addStretch(1)
            vlayout2.addWidget(self.boutonJouer)
            vlayout2.addWidget(self.boutonParam)
            vlayout2.addWidget(self.boutonQuitter)
            vlayout2.addStretch(1)
            
            #ajout des layout
            vlayout1.addLayout(hlayout1)
            hlayout2.addLayout(vlayout2)
            vlayout1.addLayout(hlayout2)
            
            
            self.show()
            
            
            
        def redimensionner_boutons(self):
            """Ajuste la taille des boutons en fonction de la taille de la fenêtre."""
            largeur = self.width() // 2   # moitié de la largeur de la fenêtre
            hauteur = self.height() // 10 # 1/10 de la hauteur de la fenêtre

            for bouton in (self.boutonJouer, self.boutonParam,self.boutonQuitter):
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = VueMenu()
    sys.exit(app.exec())