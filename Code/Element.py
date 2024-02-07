class Element(object):
    """Classe de base pour tout les élements du jeu. Ils ont un nom
        Class abstraite."""

    def __init__(self, name, abbrv=""):
        self.name = name
        if abbrv == "":
            abbrv = name[0]
        self.abbrv = abbrv

    def __repr__(self):
        return self.abbrv

    def description(self):
        """Description de l'élement"""
        return "<" + self.name + ">"

    def meet(self, hero):
        """Fait rencontrer le héro avec un élement. Pas implémenté """
        raise NotImplementedError('Abstract Element')
