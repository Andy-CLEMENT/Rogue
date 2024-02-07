from Creature import Creature
from Coord import Coord
import handler
import theGame



class Boss(Creature):

    def __init__(self, name, hp=10, abbrv="$", strength=3, state="normal",stateTime=0, defense = 0, categorie="cac", rangeAtk=1, elementAtk="normal", timeEffect=0, proba=100):
        Creature.__init__(self, name, hp, abbrv, strength, state,stateTime,defense,categorie,rangeAtk,elementAtk,timeEffect,proba)

    def spawnArmy(self,map,creature,hero,compt, r=2):   #Creature: monstre qui se fera invoquer par le boss / map : On ajoute la carte pour les fonction lié à la carte / hero: désigne le héro 
        coordHero= map.pos(hero)                            # c: Tout les c tour on invoque les monstres / n: nombre de monstre qui spawn à chaque invocation ( 1 de base)
        coordBoss= map.pos(self)                            # distance: rayon  ou l'invocation est possible                                                                           
        if  coordBoss.distance(coordHero)<=r and  hero.compteurBoss%compt==0: #On vérifie la distance entre le boss et le héro:
          for i in [Coord(1,0),Coord(-1,0),Coord(0,1),Coord(0,-1)]:
            coordCreature=coordBoss+i
            if map.get(coordCreature) == map.ground:
                map.put(coordCreature,creature)
                theGame.theGame().addMessage("Monstre apparu")
                return None
        return None
    
    def tpBoss(self):   #Permet au boss de se téléporter
        handler.teleport(self,True)
        theGame.theGame().addMessage(self.name+" s'est téléporter !")
