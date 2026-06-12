import random

from PyQt6.QtCore import QSettings

from VueMenu import *
from Grille import Grille
from pathlib import Path

class Controlleur:
    def __init__(self) -> None:
        self.modele: Grille = Grille()
        self.vue = 0

        self.settings = QSettings("MonEntreprise", "MonApp")
        self.case_actuelle: None | tuple[int, int] = None

        self.load_settings()

        
        self.vue.ouvrirUrlClicked.connect(self.ouvrir_url_regle)
        self.vue.quitterAppClicked.connect(self.quitter_application)
        self.vue.paramClicked.connect(self.)

    def ouvrir_url_regle(self):
        url = QUrl("https://www.innoludic.com/fr/2015-04-27-17-17-03/regles-du-suguru")
        QDesktopServices.openUrl(url)
                
    def quitter_application(self):
        """Ferme  la fenêtre"""
        self.save_settings()
        self.close()

    def save(self, nom: str) -> None:
        self.modele.sauvegarderGrilleToJson(f"saves/{nom}.json")

    def charger(self, type: str, nom: str | None = None) -> None:
        if type == "save":
            if nom:
                self.modele.chargerSaveFromJson(f"saves/{nom}.json")
        elif type == "new":
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

        self.settings.setValue("geometry", state["geometry"])
        self.settings.setValue("windowState", state["windowState"])