import random

from PyQt6.QtCore import QSettings

from VueMenu import *
from Grille import Grille
from pathlib import Path
from PyQt6.QtCore import QUrl 
from PyQt6.QtGui import QDesktopServices

class Controlleur():
    def __init__(self) -> None:
        
        self.modele: Grille = Grille()
        self.vue = VueMenu()

        self.settings = QSettings("MonEntreprise", "MonApp")
        self.case_actuelle: None | tuple[int, int] = None

        self.load_settings()

        
        self.vue.ouvrirUrlClicked.connect(self.ouvrir_url_regle)
   
        self.vue.chargerClicked.connect(self.charger)
        self.vue.nouveauClicked.connect(self.nouveau)
        

    def ouvrir_url_regle(self):
      
        url = QUrl("https://www.innoludic.com/fr/2015-04-27-17-17-03/regles-du-suguru")
        QDesktopServices.openUrl(url)
   
    

    def save(self, nom: str) -> None:
        self.modele.sauvegarderGrilleToJson(f"saves/{nom}.json")

    def charger(self,  nom: str ) -> None:
         if nom:
            self.modele.chargerSaveFromJson(f"saves/{nom}.json")
        
            
    def nouveau(self):          
          
        dossier_grilles = Path("grilles")

        json_files = list(dossier_grilles.glob("*.json"))

        if json_files:
            self.modele.chargerGrilleFromJson(random.choice(json_files))
            
    def load_settings(self):
        geometry = self.settings.value("geometry")
        window_state = self.settings.value("windowState")

        state = {}
        if geometry:
            state["geometry"] = geometry
        if window_state:
            state["windowState"] = window_state

        self.vue.set_window_state(state)

    def save_settings(self):
        state = self.vue.get_window_state()        
    
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # L'instanciation lance le contrôleur, crée la vue et lie les signaux
    controlleur = Controlleur()
    
    sys.exit(app.exec())
