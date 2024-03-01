from Wearable import Wearable
import theGame
from handler import heal,boost,nerf



class Amulette(Wearable):
    "Classe qui gère les amulettes"

    def __init__(self, name, effect, place="tête", abbrv="", use=None):
        Wearable.__init__(self,name,effect,place,abbrv,use)

    def regeneration(self,creature,compt,n):    #compt est le nombre d'action pour ce régénérer et heal et le nombre de pv que l'on s'ajoute 
        if creature.compteur%compt==0:            #tout les X actions on se regenére
            heal(creature,n)
    
    def coupCrit(self,creature,compt,n): 
        """Fonction qui definie les coups critiques"""
        if creature.compteur%compt==0:
            boost(creature,{"strength":n})  #on ajoute un bonus de dégat pour 1 tour
            theGame.theGame().addMessage("Possibilité de coup critique")
        if (creature.compteur-1) !=0 and (creature.compteur-1)%compt==0:  #Une fois le tour finit on regagne les dégats de bases
            nerf(creature,{"strength":n})
            theGame.theGame().addMessage("Plus de coup critique sniff")
