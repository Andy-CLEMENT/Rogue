import theGame
import time
from Hero import Hero
from Element import Element



class Forgeron(Element):

    elemAmmeliorable=["dague","armure de bronze","épée", "arc", "halbarde", "armure d argent", "armure d or", "Excalibur"]      #liste des éléments améliorables
    
    def __init__(self,name="forgeron",abbrv="F"):
        Element.__init__(self, name, abbrv)

    def meet(self,other):   
        l = []
        heroInv=other._inventory
        if isinstance(other,Hero):
            print("Bonjour je suis forgeron et contre 1 d acier vous pouvez améliorer une arme ou une armure qui n a jamais été amélioré.")
            suggestion=[]
            for elem in heroInv:
                if elem.name in Forgeron.elemAmmeliorable:      #Cherche des éléments améliorables dans l'inv du héros
                    suggestion.append(elem)
            print(suggestion)
            if suggestion == []:        #Si rien n'est trouvé
                print("Allez cherchez une arme ou une armure à améliorer")
                print("Au revoir")

            if other.acier <= 0:        #Si pas d'acier
                print("Allez cherchez de l'acier et je pourrais vous aider")
                print("Au revoir")


            else:
                print("Je peux vous améliorer " + str([str(suggestion.index(elem))+ " : " + elem.name for elem in suggestion]))
                choix=theGame.theGame().select(suggestion)
                if choix:
                    for x in elem.effect.keys():        #Amélioration !
                        elem.effect[x]+=1
                    elem.name+="+"
                    print("J'ai amélioré" + elem.name)
                print("Au revoir !")
            time.sleep(1)
            return True
                

                


            












                        







                
                
                    
