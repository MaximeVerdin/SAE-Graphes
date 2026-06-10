class Case:
    def __init__(self, x: int, y: int, c: int | None = 0) -> None:
        """Méthode dédiée, constructeur de la classe"""

        self.__abscisse: int = x
        self.__ordonne: int = y
        self.__contenu : int | None = None if c == 0 else c


    def setContenu(self, cakechose: int | None) -> None:
        """Méthode publique, affecte le __contenu de l'objet."""
        self.__contenu = cakechose


    def getContenu(self) -> int | None:
        """Méthode publique, renvoie le __contenu de l'objet."""
        return self.__contenu


    def getPosition(self) -> tuple:
        """Méthode publique, renvoie la position de l'objet : tuple (x, y)"""
        return (self.__abscisse, self.__ordonne)

    def toList(self) -> list:
        """
        Retourne une liste de l'objet
        :return: (x, y, valeur)
        """
        return [self.__abscisse, self.__ordonne, self.__contenu if self.__contenu else 0]