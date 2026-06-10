
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
    
    
    def tailleMotif(self)->int:
        """retourne le nombre de cases du motif
            :return: retourne un entier 
        """
        return len(self.__liste_cases)
    
    
    def contenuValide(self,c :Case)->bool:
        """retourne false,ainsi que la case concerne si le contenu de la case n'est pas valide (le contenu est supérieur à la taille du motif)
           :return: un boolean       
        """
        if c.getContenu() > self.tailleMotif() or c.getContenu() < 1:
            return False
        
        for case in self.__liste_cases:
            if c.getContenu() == case.getContenu() and c.getPosition() != case.getPosition() :
                return False
        return True


def buildMotifFromListe(l: list) -> Motif:
    """
    remplie un motif avec toutes les cases qu'il contient
    :param l: Liste contenant les cases sous forme de listes.
    :return: retourne un motif
    """
    motif = Motif()
    for case in l:
        motif.ajouterCase(Case(case[0],case[1],case[2]))
    return motif
    
       
        
        
        

