from Element import Element
import theGame



class Stairs(Element):
    """ Escalier qui permet de passer d'un étage à un autre. """

    def __init__(self):
        super().__init__("Stairs", 'E')

    def meet(self, hero):
        """Va en bas"""
        theGame.theGame().buildFloor()
        theGame.theGame().addMessage(hero.name + " est descendu")
