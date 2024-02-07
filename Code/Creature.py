from Element import Element
import theGame
import random

class Creature(Element):
    """Creatures qui sont présent sur la carte
        Se sont des élements. Ils ont des PV et de la Force"""

    def __init__(self, name, hp, abbrv="", strength=1, state="normal",stateTime=0, defense = 0, categorie="cac", rangeAtk=1, elementAtk="normal", timeEffect=0, proba=100):
        Element.__init__(self, name, abbrv)
        self.state=state
        self.hp = hp
        self.strength = strength
        self.stateTime=stateTime
        self.categorie=categorie
        self.elementAtk=elementAtk
        self.rangeAtk=rangeAtk
        self.timeEffect=timeEffect
        self.proba=proba
        self.defense=defense
        self.hpMax= hp 
        self.compteur=0

    def description(self):
        """Description de la creature"""
        return Element.description(self) + "(" + str(self.hp) + "/"+ str(self.hpMax)+ ")"

    def meet(self, other):
        """La creature rencontre une autre creature.
            L'autre attaque la creature. Renvoie True si la creature est morte"""
        deg = other.strength-self.defense             #calcul des dégats en fonction de la défense
        if deg<1:
            self.hp -= 1
        else:
            self.hp-=deg
        if self.hp < 0:
            self.hp =0
        theGame.theGame().addMessage(other.name + " a attaqué " + self.description())
        if self.hp > 0:
            if self.name in ["Thanos"]: #Si ce boss subit des dégats, il se téléporte
                self.tpBoss()
            return False
        return True

