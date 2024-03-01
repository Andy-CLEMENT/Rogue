from Element import Element

class Projectile(Element):
    """Créer un objet qui correspond à un projetctile"""
    def __init__(self, name, abbrv="", rangeAtk=6, strength=2, elementAtk="", timeEffect=0, proba=100):
        Element.__init__(self, name, abbrv)
        self.abbrv=abbrv
        self.rangeAtk = rangeAtk
        self.strength=strength
        self.elementAtk=elementAtk
        self.timeEffect=timeEffect
        self.proba=proba
