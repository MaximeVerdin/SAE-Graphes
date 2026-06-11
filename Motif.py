from __future__ import annotations

from Case import Case

class Motif(object) :
    """Classe définissant une case à partir de sa position : x, y."""

    def __init__(self):
        
        self.__liste_cases: list[Case] = []


    def estValide(self) -> bool:
        """
        Verifie si le motif est valide
        :return: Retourne True si la grille est valide, False sinon
        """
        liste_valeurs = []
        for case in self.__liste_cases:
            if not case.getContenu() in liste_valeurs or not(case.getContenu()):
                liste_valeurs.append(case.getContenu())
            else:
                return False
        return True


    def estPlein(self):
        """
        Verifie si le motif est plein
        :return: Retourne True si la grille est plein, False sinon
        """
        liste_valeurs = []
        for case in self.__liste_cases:
            if not case.getContenu() in liste_valeurs and not case.getPosition():
                liste_valeurs.append(case.getContenu())
                
        return len(liste_valeurs) == self.tailleMotif()


    def ajouterCase(self,c : Case) ->None:
        """ajoute une case du motif
            :param c: un objet de type Case"""
        self.__liste_cases.append(c)
        
        
    def supprimerCase(self,c : Case) ->None:
        """supprime une case du motif
           :param c: un objet de type Case
        """
        for case in self.__liste_cases:
            if c in self.__liste_cases:
                self.__liste_cases.remove(c)
                
                
    def getCases(self)->list[Case]:
        """retourne une liste de toute les cases du motif
            :return :une liste d'objet de type Case        
        """
        return self.__liste_cases
    
    
    def getCase(self,x :int,y :int)->Case:
        """retourne une seule case en fonction de ses coordonnée
           :return: un objet de type Case
        """
        for case in self.__liste_cases:
            if case.getPosition() == (x,y):
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


def buildMotifFromListe(l: list) -> Motif:
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