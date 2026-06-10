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

        for case in self.getCases():

            if case.contenu is None:
                continue

            for voisin in self.getVoisins(case):

                if voisin.contenu == case.contenu:
                    return False

        return True

    def estPleine(self) -> bool:

        return all(
            motif.estPlein()
            for motif in self._motifs
        )

    def chargerGrilleFromJson(self, fichier: str) -> None:

        self._motifs.clear()
        self._cases.clear()

        with open(fichier, encoding="utf-8") as f:

            data = json.load(f)

            for valeur in data.values():
                self.addMotif(
                    buildMotifFromListe(valeur)
                )

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

        cases = self.getCases()

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