class Case:
    def init(self, x: int, y: int, c: int):
        '''Méthode dédiée, constructeur de la classe'''

        self.abscisse: int = x
        self.ordonne: int = y
        self.contenu : int | None = None if c == 0 else c


    def setContenu(self, cakechose: int) -> None:
        '''Méthode publique, affecte le contenu de l'objet.'''
        self.contenu = cakechose


    def getContenu(self) -> int:
        '''Méthode publique, renvoie le contenu de l'objet.'''
        return self.contenu


    def getPosition(self) -> tuple:
        '''Méthode publique, renvoie la position de l'objet : tuple (x, y)'''
        return (self.__abscisse, self.ordonne)

    def toList(self) -> list:
        '''
        Retourne une liste de l'objet
        :return: (x, y, valeur)
        '''
        return [self.abscisse, self.ordonne, self.contenu]