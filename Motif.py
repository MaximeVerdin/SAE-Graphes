from __future__ import annotations

from Case import Case

class Motif(object) :
    """Classe définissant une case à partir de sa position : x, y."""

    def __init__(self):
        self._cases: list[Case] = []

    def ajouterCase(self, case: Case) -> None:
        case.motif = self
        self._cases.append(case)

    def supprimerCase(self, case: Case) -> None:
        if case in self._cases:
            self._cases.remove(case)
            case.motif = None

    def getCases(self) -> list[Case]:
        return self._cases

    def getCase(self, x: int, y: int) -> Case | None:
        for case in self._cases:
            if case.x == x and case.y == y:
                return case
        return None

    def tailleMotif(self) -> int:
        return len(self._cases)

    def estValide(self) -> bool:
        valeurs = set()

        for case in self._cases:
            valeur = case.contenu

            if valeur is None:
                continue

            if valeur in valeurs:
                return False

            valeurs.add(valeur)

        return True

    def estPlein(self) -> bool:
        return all(case.contenu is not None for case in self._cases)

    def contenuValide(self, case: Case) -> bool:

        if case.contenu is None:
            return True

        if not (1 <= case.contenu <= self.tailleMotif()):
            return False

        for autre in self._cases:

            if autre is case:
                continue

            if autre.contenu == case.contenu:
                return False

        return True


def buildMotifFromListe(liste: list) -> Motif:

    """
    remplie un motif avec toutes les cases qu'il contient
    :param l: Liste contenant les cases sous forme de listes.
    :return: retourne un motif
    """
    motif = Motif()

    for x, y, valeur in liste:

        motif.ajouterCase(
            Case(
                x,
                y,
                None if valeur == 0 else valeur
            )
        )

    return motif