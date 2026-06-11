import json

from Case import Case
from Motif import Motif, buildMotifFromListe


class Grille:
    """
    Cette classe est le modèle représentant une grille de données
    """
    def __init__(self):

        self._motifs: list[Motif] = []

        self._cases: dict[tuple[int, int], Case] = {}

    def addMotif(self, motif: Motif) -> None:

        self._motifs.append(motif)

        for case in motif.getCases():
            self._cases[(case.x, case.y)] = case

    def removeMotif(self, motif: Motif) -> None:

        if motif in self._motifs:

            self._motifs.remove(motif)

            for case in motif.getCases():
                self._cases.pop((case.x, case.y), None)

    def getMotifs(self) -> list[Motif]:
        return self._motifs

    def getNombreMotif(self) -> int:
        return len(self._motifs)

    def getCase(self, x: int, y: int) -> Case | None:
        return self._cases.get((x, y))

    def getCases(self) -> list[Case]:
        return list(self._cases.values())

    def getMotifFromCase(self, case: Case) -> Motif | None:
        return case.motif

    def setValeur(self, x: int, y: int, valeur: int | None) -> None:

        case = self.getCase(x, y)

        if case is not None:
            case.contenu = valeur

    def getValeur(self, x: int, y: int) -> int | None:

        case = self.getCase(x, y)

        if case is not None:
            return case.contenu

        return None

    def getVoisins(self, case: Case) -> list[Case]:

        voisins = []

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):

                if dx == 0 and dy == 0:
                    continue

                voisin = self.getCase(
                    case.x + dx,
                    case.y + dy
                )

                if voisin:
                    voisins.append(voisin)

        return voisins

    def estValide(self) -> bool:

        for motif in self._motifs:

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
                self.addMotif(
                    buildMotifFromListe(valeur)
                )

    def chargerSaveFromJson(self, fichier: str) -> None:

        self._motifs.clear()
        self._cases.clear()

        with open(fichier, encoding="utf-8") as f:
            data = json.load(f)

        motifs_data = data.get("motif", {})

        for nom_motif, liste_cases in motifs_data.items():

            motif = Motif()

            for x, y, valeur, fixe in liste_cases:
                case = Case(
                    x=x,
                    y=y,
                    contenu = None if valeur == 0 else valeur,
                    motif = motif
                )

                case.fixe = fixe

                motif.ajouterCase(case)
                self._cases[(x, y)] = case

            self._motifs.append(motif)

    def toDico(self) -> dict:

        resultat = {}

        for i, motif in enumerate(self._motifs, start=1):

            resultat[f"motif{i}"] = [
                case.toList()
                for case in motif.getCases()
            ]

        return resultat

    def sauvegarderGrilleToJson(self, fichier: str) -> None:

        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(
                self.toDico(),
                f,
                indent=4
            )

    def afficherGrille(self):
        """
        Permet d'afficher la grille
        :return:
        """
        # récupération de toutes les cases
        cases = []
        for motif in self.__liste:
            cases.extend(motif.getCases())

        if not cases:
            return

        max_x = max(case.x for case in cases)
        max_y = max(case.y for case in cases)

        grille = [
            ["." for _ in range(max_x + 1)]
            for _ in range(max_y + 1)
        ]

        for case in cases:

            grille[case.y][case.x] = (
                str(case.contenu)
                if case.contenu is not None
                else "."
            )

        for ligne in grille:
            print(" ".join(ligne))