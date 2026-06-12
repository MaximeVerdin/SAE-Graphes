import sys
import random
from pathlib import Path

from PyQt6.QtCore import QSettings, QUrl
from PyQt6.QtWidgets import QApplication, QFileDialog
from PyQt6.QtGui import QDesktopServices

from VueMenu import VueMenu
from VueJeux import VueJeux 
from Grille import Grille

class Controlleur():
    def __init__(self) -> None:
        
        self.modele: Grille = Grille()
        # Une seule vue unique gérée par le contrôleur
        self.vue = VueMenu() 

        self.settings = QSettings("MonEntreprise", "MonApp")
        self.case_actuelle: None | tuple[int, int] = None

        self.load_settings()

        # Connexions aux signaux de VueMenu
        self.vue.ouvrirUrlClicked.connect(self.ouvrir_url_regle)
        self.vue.chargerClicked.connect(self.charger)
        self.vue.nouveauClicked.connect(self.nouveau)
        
    def ouvrir_url_regle(self):
        url = QUrl("https://www.innoludic.com/fr/2015-04-27-17-17-03/regles-du-suguru")
        QDesktopServices.openUrl(url)
   
    def retourMenu(self):
        # On demande à VueMenu de réafficher la page 1 du QStackedWidget
        self.vue.afficher_menu_principal()

    def save(self) -> None:
        fichier_sauvegarde, _ = QFileDialog.getSaveFileName(
            self.vue,
            "Sauvegarder la partie",
            "saves/nouvelle_sauvegarde.json",
            "Fichiers JSON (*.json)"
        )
        if fichier_sauvegarde:
            self.modele.sauvegarderGrilleToJson(fichier_sauvegarde)
            
            
    def reset(self):
        pass

    def charger(self) -> None:
        fichier_choisi, _ = QFileDialog.getOpenFileName(
            self.vue,
            "Charger une partie",
            "saves",
            "Fichiers JSON (*.json)"
        )
        if fichier_choisi:
            self.modele.chargerGrilleFromJson(fichier_choisi)
            self.demarrer_jeu()
        
    def nouveau(self):          
        dossier_grilles = Path("grilles")
        json_files = list(dossier_grilles.glob("*.json"))

        if json_files:
            grille_choisie = random.choice(json_files)
            self.modele.chargerGrilleFromJson(grille_choisie)
            self.demarrer_jeu()

    def demarrer_jeu(self):
        """Crée la vue de jeu et demande à VueMenu de l'intégrer."""
        
        vue_jeux = VueJeux(self.modele)
        
        #Connexion des signaux du widget de jeu vers le contrôleur
        vue_jeux.accueilClicked.connect(self.retourMenu)
        vue_jeux.sauvegarderClicked.connect(self.save)
        vue_jeux.recommencerClicked.connect(self.reset)
        
        
        self.vue.afficher_ecran_jeu(vue_jeux)
            
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
    controlleur = Controlleur()
    sys.exit(app.exec())