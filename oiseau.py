from animal import Animal

class Oiseau(Animal): # This line starts the definition of a class
#The class definition Oiseau(Animal) means the class Oiseau inherit
# of the class Animal   

    def __init__(self, poids, taille, altitude_max):
        super().__init__(poids, taille)
        self.oiseau_alt = altitude_max

    def se_deplacer(self): # This a method
        """
        print type of moves
        """        
        print("Je vole")