from VueMenu import *
from Grille import *

class Controlleur():
    def __init__(self) -> None:
        self.modele = Grille
        self.vue = 
        
        
        self.vue.ouvrirUrlClicked.connect(self.ouvrir_url_regle)
        self.vue.quitterAppClicked.connect(self.quitter_application)
        self.vue.paramClicked.connect(self.)

    def ouvrir_url_regle(self):
                url = QUrl("https://www.innoludic.com/fr/2015-04-27-17-17-03/regles-du-suguru")
                QDesktopServices.openUrl(url)
                
    def quitter_application(self):
            """Ferme  la fenêtre"""
            self.close()