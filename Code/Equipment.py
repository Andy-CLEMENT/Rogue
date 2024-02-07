from Element import Element
import theGame



class Equipment(Element):
    """Une piéce d'équipement"""

    def __init__(self, name, abbrv="", use=None, permanent=False):
        Element.__init__(self, name, abbrv)
        self.usage = use
        self.permanent=permanent
        
    def meet(self,hero): # gère la rencontre entre un équipement et le héro
        if hero.take(self)== False:
            theGame.theGame().addMessage("Tu ne peux pas prendre " + self.name + " l'inventaire est plein") #phrase d'interaction
            return False
        else:
            theGame.theGame().addMessage("You pick up a " + self.name)
            return True

    def use(self, creature):
        """Utilise la pièce d'équipement. Ajoute des effets au héro.
            Renvoie True s'il est utilisé."""
        if self.usage is None:
            theGame.theGame().addMessage(self.name + " n'est pas utilisable")
            return False
        else:
            theGame.theGame().addMessage(creature.name + " a utilisé  " + self.name)
            return self.usage(self, creature)
