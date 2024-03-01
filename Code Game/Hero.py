from Creature import Creature
from Equipment import Equipment
from handler import tir, boost, nerf
from Wearable import Wearable
import keyboard, time
import theGame



class Hero(Creature):
    """Le héro du jeu.
        C'est une creature. A un inventaire d'équipement. """
    neutralEquipement=Wearable(name="0",abbrv="",effect="") #Equipemen neutre dans body ( permet de régler quelques bugs )
    def __init__(self, name="Hero", hp=10, abbrv="@", strength=2, state="normal",stateTime=0,defense=0,categorie="cac", rangeAtk=1, elementAtk="normal", timeEffect=0, proba=100, vision=6, size=2, inventory=None, txt="", argent=0, acier=0, vie=1):
        Creature.__init__(self, name, hp, abbrv, strength, state,stateTime,defense,categorie,rangeAtk, elementAtk, timeEffect, proba)
        if inventory == None :
            self._inventory = []
        else :
            self._inventory = inventory
        self.vision = vision
        self.size=size
        self.txt=txt
        self.compteurBoss=0                         #compteur pour les fonctionnalités des boss
        body= []
        for i in range(5):
            body.append(self.neutralEquipement)    #Liste qui représente le corp du héro suivant cette répartition 
        self.body=body
        self.argent = argent
        self.acier = acier
        self.vie=vie

    def description(self):
        """Description du hero"""
        return Creature.description(self)+ str(self._inventory)+"("+str(len(self._inventory))+"/"+str(self.size)+")"

    def fullDescription(self):
        """Description complete du hero"""
        res = ""
        for e in self.__dict__:
            if e[0] != '_':
                res += '> ' + e + ' : ' + str(self.__dict__[e]) + '\n'
            else :
                res += '> ' + e[1:] + ' : ' + str(self.__dict__[e]) + '\n'
        res += '> INVENTORY : ' + str([x.name for x in self._inventory]) + "( "+str(len(self._inventory))+"/"+str(self.size)+")"
        return res

    def checkEquipment(self, o):
        """Vérifie si o est un Equipment."""
        if not isinstance(o, Equipment):
            raise TypeError('Not a Equipment')

    def take(self, elem):
        """Le héro prends et ajout l'equipement à son inventaire"""
        self.checkEquipment(elem)
        self.checkEquipment(elem)
        if elem.name == 'or':
            self.argent+=1
            theGame.theGame().addMessage("Oh shiny !")
        elif elem.name == 'acier':
            self.acier+=1
            theGame.theGame().addMessage("men of steel ?")
        elif self.inventSize():
            self._inventory.append(elem)
        else:
            return False

    def use(self, elem):
        """Utilise un équipement"""
        if elem is None:
            return
        self.checkEquipment(elem)
        if isinstance(elem,Wearable):           #Les equipements "équipable" sont traiter différament 
            if elem.place > len(self.body):
                raise ValueError("La partie du corp "+ elem.place + " n'existe pas")
            if elem in self._inventory == False or elem in self.body == False:
                raise ValueError('Equipment ' + elem.name + 'not in inventory')
            if self.body[elem.place]!= self.neutralEquipement:       #on vérifie si l'emplacement est libre 
                theGame.theGame().addMessage("Equipement non équipable, place déjà occupé par "+ str(self.body[elem.place].name))
            elif 'arc' in elem.name  :
                boost(self,elem.effect)
                self.body[elem.place]=elem      #On evite d'utiliser l'arc durant son équipement (sinon on tire au lieu de l'équiper)
                self._inventory.remove(elem)
            else :
                elem.use(self)
                self.body[elem.place]=elem  #On place l'équipement dans le dictionnaire body à son emplacement
                self._inventory.remove(elem)
                

        else:
            if elem not in self._inventory:
                raise ValueError('Equipment ' + elem.name + 'not in inventory')
            if elem.use(self):
                self._inventory.remove(elem)    #On enlève l'élement de l'inventaire une fois qu'il est utilisé
    
    def unEquip(self,elem):
        "Déséquipe l'équipement équipé"
        if elem is None:
            return
        if elem.place==None:
            theGame.theGame().addMessage("Emplacement vide, ne peut pas être deséquipé ")
        else:
            nerf(self,elem.effect)
            self.body[elem.place]= self.neutralEquipement
            self._inventory.append(elem)

    def inventSize(self):
        """Gère la taille limite de l'inventaire du héro"""
        if len(self._inventory)< self.size:
            return True

    def shot(self):
        """Fait tirer une flèche si le héros a un objet (arc) pouvant le faire"""
        if "arc" in self.body[2].name:         #Pour accepter des futurs item, il suffira qu'il y a 'bow' dans leur nom, ex: crossBOW
            self.body[2].use(self)
            return None

    
    def throw(self, rangeAtk, strength, elementAtk="", timeEffect=0,proba=100):
        #cette fonction sert a faire tirer une fleche. elle demande la direction puis tire
        stage=theGame.theGame()._floor
        coordUser=stage.pos(self)
        c = None
        while c not in ["z","q","s","d"]:
            print("Which way ? > z : top, q : left, s : down, d : right")
            time.sleep(0.5)
            c=keyboard.read_key()
        dir=stage.dir[c]
        tir(coordUser,dir, rangeAtk, strength, elementAtk, timeEffect,proba)



