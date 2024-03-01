from Equipment import Equipment



class Wearable(Equipment):
    """Un équipement équipable"""
    def __init__(self, name, effect, place=None, abbrv="", use=None):
        Equipment.__init__(self, name, abbrv, use)
        self.effect = effect

        #puisque body est une liste, on associe chaque partie du corp à un indice
        if place=='tête':
            place=0
        elif place=='corps':
            place=1
        elif place=='main':
            place=2
        elif place=='jambes':
            place=3
        elif place=='pieds':
            place=4
        self.place=place
