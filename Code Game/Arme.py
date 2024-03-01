from Wearable import Wearable



class Arme(Wearable):
    "Classe qui gère les amulettes"

    def __init__(self, name, effect, place="main", abbrv="", use=None):
        Wearable.__init__(self,name,effect,place,abbrv,use)

