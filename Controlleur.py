import sys
import random
from pathlib import Path

from PyQt6.QtCore import QSettings, QUrl
from PyQt6.QtWidgets import QApplication, QFileDialog
from PyQt6.QtGui import QDesktopServices

from Solveur import Solveur
from VueMenu import VueMenu
from VueJeux import VueJeux
from Grille import Grille

class Controlleur():
    def __init__(self) -> None:
        
        self.modele: Grille = Grille()
        # Une seule vue unique gérée par le contrôleur
        self.vue = VueMenu()

        self.buildSolution()

        self.case_actuelle: None | tuple[int, int] = None

        self.vue.ouvrirUrlClicked.connect(self.ouvrirUrlRegle)
        self.vue.chargerClicked.connect(self.charger)
        self.vue.nouveauClicked.connect(self.nouveau)


    def buildSolution(self):
        solveur = Solveur(self.modele)
        self.solutions = solveur.resoudre()
        self.index = self._build_index(self.solutions)
        self.solutions_valides = set(range(len(self.solutions)))
        self.contraintes: dict[tuple[int, int], int] = {}


    def _build_index(self, solutions):
        """
        Construit l'index :
        (x, y, valeur) -> set(indices solutions)
        """

        index = {}

        for i, sol in enumerate(solutions):

            for case in sol.getCases():

                key = (case.x, case.y, case.contenu)

                if key not in index:
                    index[key] = set()

                index[key].add(i)

        return index


    def setValue(self, x: int, y: int, valeur: int | None):
        """
        Ajoute / modifie / supprime une contrainte utilisateur.
        """

        if valeur is None:
            self.contraintes.pop((x, y), None)
        else:
            self.contraintes[(x, y)] = valeur

        self._recompute()

    def _recompute(self):

        ensembles = []

        for (x, y), valeur in self.contraintes.items():

            key = (x, y, valeur)

            if key not in self.index:
                self.solutions_valides = set()
                self.onNoSolution()
                return

            ensembles.append(self.index[key])

        if not ensembles:
            self.solutions_valides = set(range(len(self.solutions)))
            return

        ensembles.sort(key=len)

        result = ensembles[0].copy()

        for s in ensembles[1:]:
            result &= s

            if not result:
                break

        self.solutions_valides = result

        if not result:
            self.onNoSolution()

    def getActiveSolutions(self):
        """
        Retourne les grilles compatibles avec l'état actuel.
        """

        return [
            self.solutions[i]
            for i in self.solutions_valides
        ]

    def onNoSolution(self):
        """
        Action effectué quand il n'y a pas de solutions
        """
        if not self.case_actuelle:
            return

        if self.difficulte == "hard":
            self.modele.setValeur(self.case_actuelle[0], self.case_actuelle[1], None)
            self.setValue(self.case_actuelle[0], self.case_actuelle[1], None)

        elif self.difficulte == "medium":
            self.modele.setValeur(self.case_actuelle[0], self.case_actuelle[1], None)
            self.setValue(self.case_actuelle[0], self.case_actuelle[1], None)

        else:
            i = random.choice(tuple(self.solutions_valides))
            self.modele.setValeur(
                *self.case_actuelle,
                self.solutions[i].getValeur(*self.case_actuelle)
            )
            self.setValue(self.case_actuelle[0], self.case_actuelle[1], self.solutions[i].getValeur(*self.case_actuelle))


    def changeValeur(self, x: int, y: int, valeur: int | None):
        ancien = self.modele.getValeur(x, y)
        self.modele.setValeur(x, y, valeur)
        if not self.modele.estValide():
            self.modele.setValeur(x, y, ancien)
            self.vue.barreStatus.showMessage("Valeur Invalide", 5000)
        else:
            self.setValue(x, y, valeur)



    def ouvrirUrlRegle(self):
      
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
            self.buildSolution()
            self.demarrer_jeu()

    def nouveau(self):
        dossier_grilles = Path("grilles")
        json_files = list(dossier_grilles.glob("*.json"))

        if json_files:
            grille_choisie = random.choice(json_files)
            self.modele.chargerGrilleFromJson(grille_choisie)
            self.buildSolution()
            self.demarrer_jeu()

    def demarrer_jeu(self):
        """Crée la vue de jeu et demande à VueMenu de l'intégrer."""

        vue_jeux = VueJeux(self.modele)

        #Connexion des signaux du widget de jeu vers le contrôleur
        vue_jeux.accueilClicked.connect(self.retourMenu)
        vue_jeux.sauvegarderClicked.connect(self.save)
        vue_jeux.recommencerClicked.connect(self.reset)


        self.vue.afficher_ecran_jeu(vue_jeux)
    
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    controlleur = Controlleur()
    sys.exit(app.exec())