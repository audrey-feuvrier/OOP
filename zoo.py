from animal import Animal as Ani

class Zoo: # This line starts the definition of a class
        
    def __init__(self, animaux :list) :
        """
        takes one parameter :
         animaux which is a list of class Animal
        The loop allows to verify if eanch element of
        animaux is of class Animal and raise an error
        if not
        """ 
        self.animals = []
        for i in animaux :   
            self.add_animal(i)
        print("Le zoo contient", len(self.animals),"animaux.") 
    
    def add_animal(self, animal) :
        """
        takes one parameter :
        animal which is a list of class Animal
        The method add animal to the list animals
        """    
        if isinstance(animal,Ani) :
            self.animals.append(animal)  
            #print("Un animal a été ajouté au zoo")   
        else :
            raise ValueError(str(animal)+' is not of class Animal. Replace it.') 

    def add_zoo(self,animaux2) :
        """
        takes one parameter :
        animaux2 which is a list of class Zoo
        The method add animaux2 to the list animals
        """ 
        if isinstance(animaux2,Zoo) :
            self.animals += animaux2.animals
            print("De nouveaux animaux ont été ajouté. Le zoo contient maintenant", len(self.animals),"animaux.") 
        else :
            raise ValueError(str(animaux2)+' is not of class Zoo. Replace it.')     

    def __add__(self,other) :
        """
        takes one parameter :
        animaux2 which is a list of class Zoo
        The method add animaux2 to the list animals
        """ 
        if isinstance(other,Zoo) :
            print("Un nouveau zoo a été créé. Le zoo contient", len(self.animals + other.animals),"animaux.") 
            return self.animals + other.animals
        else :
            raise ValueError(str(animaux2)+' is not of class Zoo. Replace it.')  