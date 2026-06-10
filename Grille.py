import json

from Motif import *
from Case import Case

class Grille:
    """
    Cette classe est le modèle représentant une grille de données
    """
    def __init__(self):
        self.__largeur : int = 0
        self.__longueur : int = 0
        self.__liste : list[Motif] = []

    def estValide(self) -> bool:
        """
        Verifie si la grille est valide
        :return: Retourne True si la grille est valide
        """
        for motif in self.__liste:
            if not motif.estValide():
                return False
        return True

    def estPleine(self):
        """
        Verifie si la grille est complete
        :return: Retourne True si la grille est complete
        """
        for motif in self.__liste:
            if not motif.estPlein():
                return False
        return True

    def getNombreMotif(self) -> int:
        """
        Retourne le nombre de motifs dans la grille
        :return: Un entier représentant le nombre de motifs
        """
        return len(self.__liste)


    def addMotif(self, motif : Motif) -> None:
        """
        Ajoute un motif à la grille
        :param motif: Le motif à ajouter
        :return:
        """
        self.__liste.append(motif)


    def removeMotif(self, motif : Motif) -> None:
        """
        Retire un motif de la grille
        :param motif: Le motif à retirer
        :return:
        """
        self.__liste.remove(motif)


    def getMotifFromCase(self, c: Case) -> Motif | None:
        """
        Retourne le motif possèdant la case souhaité
        :param c: La case à verifier
        :return: Le motif auquel appartient la case
        """
        for motif in self.__liste:
            for case in motif.getCases():
                if c.getPosition() == case.getPosition():
                    return motif
        return None

    def getMotifs(self):
        """
        Retourne une liste de motifs
        :return: La liste des motifs de la grille
        """
        return self.__liste


    def getCase(self, c: Case) -> Case | None:
        """
        Retourne la case nécessaire dans la grille
        :param c: La case que l'on cherche
        :return: La case cherché
        """
        for motif in self.__liste:
            for case in motif.getCases():
                if c.getPosition() == case.getPosition():
                    return case
        return None


    def getCases(self) -> list[Case]:
        """
        Renvoie l'ensemble des cases de la grille
        :return: Une liste représentant toutes les cases de la grille
        """
        liste: list[Case] = []
        for motif in self.__liste:
            liste += motif.getCases()
        return liste


    def setContenue(self, case: Case) -> None:
        """
        Change la valeur de la case
        :param case: La case à changer
        :param valeur: La valeur à attribuer à la case
        :return:
        """
        motif = self.getMotifFromCase(case)
        if motif:
            motif.getCase(case.getPosition()[0], case.getPosition()[1]).setContenu(case.getContenu())


    def getContenue(self, case: Case) -> int | None:
        """
        Donne la valeur de la case
        :param case: La case dont on souhaite récupérer la valeur
        :return:
        """
        motif = self.getMotifFromCase(case)
        if motif:
            return motif.getCase(case.getPosition()[0], case.getPosition()[1]).getContenu()
        return None


    def chargerGrilleFromJson(self, file: str) -> None:
        """
        Charge dans la grille à partir d'un json
        :param file: Chemin du fichier json
        :return:
        """
        with open(file) as json_file:
            data = json.load(json_file)
            for valeur in data.values():
                self.addMotif(buildMotifFromListe(valeur))


    def toDico(self) -> dict:
        """
        Retourne un dictionnaire créé à partir de la grille actuelle
        :return: Un dictionnaire semblable à la grille
        """
        dico: dict = {}
        nom_motif: str = "motif0"
        for motif in self.__liste:
            nom_motif = nom_motif[:5] + str(int(nom_motif[5:])+1)
            liste_case_dico: list[list[int]] = []

            liste_case: list[Case] = motif.getCases()
            for case in liste_case:
                liste_case_dico.append(case.toList())

            dico[nom_motif] = liste_case_dico

        return dico


    def sauvegarderGrilleToJson(self, file: str) -> None:
        """
        Sauvegarde la grille au format json
        :param file: Chemin du fichier json
        :return:
        """

        with open(file, 'w') as json_file:
            json.dump(self.toDico(), json_file, indent=4)

    def afficherGrille(self):
        # récupération de toutes les cases
        cases = []
        for motif in self.__liste:
            cases.extend(motif.getCases())

        # calcul des dimensions de la grille
        max_x = max(case.getPosition()[0] for case in cases)
        max_y = max(case.getPosition()[1] for case in cases)

        # création de la grille vide
        grille = [["." for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        # remplissage de la grille
        for case in cases:
            x, y = case.getPosition()
            grille[y][x] = str(case.getContenu()) if case.getContenu() else "."

        # affichage
        for ligne in grille:
            print(" ".join(ligne))

if __name__ == "__main__":
    grille = Grille()
    grille.chargerGrilleFromJson("grilles/grille1.json")
    #grille.sauvegarderGrilleToJson("grilles/grille1_new.json")
    #print(grille.getContenue(Case(0,7)))
    #grille.setContenue(Case(0,7, None))
    #print(grille.getContenue(Case(0,7)))
    #print(grille.getCases())
    #print(grille.getCase(Case(0,7)))
    #case_a = Case(1, 7, 3)
    #grille.setContenue(case_a)
    grille.afficherGrille()
    #print(grille.estValide())