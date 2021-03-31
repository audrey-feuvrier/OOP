# place to define import
from animal import Animal
from zoo import Zoo
from serpent import Serpent
from oiseau import Oiseau


if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")

    #[Instanciation et attributs]
    chat = Animal(3.3,37)
    #print(chat._animal_size)
    print("chat")
    chat.getPoidsTaille()

    #[Héritage et Polymorphisme]
    vipere = Serpent(0.3,58)
    print("vipere")
    vipere.getPoidsTaille()
    vipere.se_deplacer()

    aigle = Oiseau(3.45,78, 450)
    print("oiseau")
    aigle.getPoidsTaille()
    aigle.se_deplacer()

    #[Super fonction]
    print("Altitude maximal", aigle.oiseau_alt, "m")

    #[Encapsulation]
    chien = Animal(5.6,37)
    #chien = Animal(-5.6,37)
    
    #[Association]
    anims = Zoo([chat, vipere, aigle, chien])
    #anims = Zoo([chat, 12, aigle, chien])
    renard = Animal(2.8,26)
    anims.add_animal(renard)

    #[Operator overloading]
    print(chat)
    print(renard)

    poule = Animal(1.8,25)
    vache= Animal(140,250)
    mouton=Animal(80,124)
    ferme =Zoo([poule, vache, mouton])
    #anims.add_zoo(ferme)
    zoo=anims.__add__(ferme)
