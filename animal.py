class Animal: # This line starts the definition of a class
    
    def __init__(self, poids, taille): # This a constructor function
        """
        takes two parameters :
         poids - weight of the animal
         taille - height of the animal
        """        
        # the constructor function is called when we want to create a new object
        # the keyword self makes reference to the object we are creating
        self.set_weigth(poids)
        self._animal_size = taille # define the atrribute 'size' on this object 
    
    ## getter method to get the properties using an object
    def get_weight(self):
        return self.__animal_weight

    ## setter method to change the value 'poids' using an object
    def set_weigth(self, poids):
        ## condition to check whether 'poids' is suitable or not
        if poids > 0 :
            self.__animal_weight = poids
        else:
            raise ValueError('Weight is null or negative, correct weight value.')

    def se_deplacer(self): # This a method
        """
        do nothing for now
        """        
        pass

    def getPoidsTaille(self):
        print("poids de l'animal",self.__animal_weight,"kg. Taille de l'animal",self._animal_size,"cm")

    def __str__(self): 
        """
        implement the method __str__ on Animal class. 
        print method invokes str to print an object.
        """        
        return f"Poids de l'animal {self.__animal_weight} kg. Taille de l'animal {self._animal_size} cm"