import json
from os import close

from Motif import Motif
from Case import Case

class Grille:
    def __init__(self):
        self.__largeur : int = 0
        self.__longueur : int = 0
        self.__liste : list[Motif] = []



    def getNombreMotif(self) -> int:
        '''
        Retourne le nombre de motifs dans la grille
        :return: Un entier représentant le nombre de motifs
        '''
        return len(self.__liste)

    def addMotif(self, motif : Motif) -> None:
        '''
        Ajoute un motif à la grille
        :param motif: Le motif à ajouter
        :return:
        '''
        self.__liste.append(motif)

    def removeMotif(self, motif : Motif) -> None:
        '''
        Retire un motif de la grille
        :param motif: Le motif à retirer
        :return:
        '''
        self.__liste.remove(motif)


    def getMotifFromCase(self, c: Case) -> Motif:
        '''
        Retourne le motif possèdant la case souhaité
        :param c: La case à verifier
        :return: Le motif auquel appartient la case
        '''
        for motif in self.__liste:
            for case in motif:
                if c.__eq__(case):
                    return motif

    def getCase(self, c: Case) -> Case:
        '''
        Retourne la case nécessaire dans la grille
        :param c: La case que l'on cherche
        :return: La case cherché
        '''
        for motif in self.__liste:
            for case in motif:
                if c.__eq__(case):
                    return case

    def setContenue(self, case: Case, valeur: int | None) -> None:
        '''
        Change la valeur de la case
        :param case: La case à changer
        :param valeur: La valeur à attribuer à la case
        :return:
        '''
        self.getMotifFromCase(case).getCase(case).setContenue(valeur)

    def getContenue(self, case: Case) -> int | None:
        '''
        Donne la valeur de la case
        :param case: La case dont on souhaite récupérer la valeur
        :return:
        '''
        pass

    def chargerGrilleFromJson(self, file: str) -> None:
        '''
        Charge dans la grille à partir d'un json
        :param file: Chemin du fichier json
        :return:
        '''
        with open(file) as json_file:
            data = json.load(json_file)
            for valeur in data.values():
                self.addMotif(Motif.buildMotifFromJson(valeur))


    def toDico(self) -> dict:
        '''
        Retourne un dictionnaire créé à partir de la grille actuelle
        :return: Un dictionnaire semblable à la grille
        '''
        dico: dict = {}
        nom_motif: str = "motif0"
        for motif in self.__liste:
            nom_motif = nom_motif[:5] + str(int(nom_motif[5:])+1)
            listeCaseDico: list[list[int]] = []

            listeCase: list[Case] = motif.getCases()
            for case in listeCase:
                listeCaseDico.append(case.toList())

            dico[nom_motif] = listeCaseDico

        return dico

    def sauvegarderGrilleToJson(self, file: str) -> None:
        '''
        Sauvegarde la grille au format json
        :param file: Chemin du fichier json
        :return:
        '''

        with open(file, 'w') as json_file:
            json.dumps(self.toDico(), json_file, indent=4)
