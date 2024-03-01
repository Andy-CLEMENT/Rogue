import theGame
import random, copy, keyboard
from Hero import Hero
from Element import Element

class Marchand(Element):
    def __init__(self,name="marchand",abbrv="M"):
        Element.__init__(self, name, abbrv)

    def meet(self,other):
        if isinstance(other,Hero):
            equip=theGame.theGame().equipments
            x = random.expovariate(1 / theGame.theGame()._level)+0.5
            for k in equip.keys():
                if k <= x:
                    l = equip[k]
                    r=k
            obj1=copy.copy(random.choice(l))
            prix1=int(r*1.7)+1
            x = random.expovariate(1 / theGame.theGame()._level)+0.5
            for k in equip.keys():
                if k <= x:
                    l = equip[k]
                    r=k
            obj2=copy.copy(random.choice(l))
            prix2=int(r*1.7)+1

            print("Bonjour, je suis le marchand. Vous avez "+str(other.argent)+" pièces. Vous pouvez acheter des objets si vous voulez. Je vous propose soit : "+obj1.name+" à "+str(prix1)+" pièces ou : "+obj2.name+" à "+str(prix2)+" pièces. Tapez 1 si vous voulez l'equipement 1 ou 2 pour l'equipement 2 et si vous ne voulez pas acheter tapez 0")
            z=""
            while z!="0":
                z = keyboard.read_key()
                if z == "1":
                    if other.argent < prix1:
                        print("Vous n avez pas assez d'argent")
                    else:
                        other.argent -= prix1
                        other.take(obj1)
                elif z == "2":
                    if other.argent < prix2:
                        print("Vous n avez pas assez d'argent")
                    else:
                        other.argent -= prix2
                        other.take(obj2)
                elif z!="0":
                    print("Vous n'avez pas fait la bonne commande"+"\n"+"\n"+"Je suis le marchand. Vous avez "+str(other.argent)+" pièces. Vous pouvez acheter des objets si vous voulez. Je vous propose soit : "+obj1.name+" à "+str(prix1)+" pièces ou : "+obj2.name+" à "+str(prix2)+" pièces. Tapez 1 si vous voulez l'equipement 1 ou 2 pour l'equipement 2 et si vous ne voulez pas acheter tapez 0")
            print ("Au revoir")
        return True
