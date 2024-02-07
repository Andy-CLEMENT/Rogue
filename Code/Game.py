from Equipment import Equipment
from Creature import Creature
from Coord import Coord
from Hero import Hero
from Map import Map
from Stairs import Stairs
from handler import heal, teleport, boost,revive, fullBoost, amasser
from Amulette import Amulette
from Arme import Arme
from Boss import Boss
from Wearable import Wearable
from Marchand import Marchand
from Forgeron import Forgeron
import theGame
import random, copy, keyboard, time

class Game(object):
    """ Classe représentant l'état du jeu """

    """ equipments disponibles """
    equipments = {0: [Equipment("potion", "!", use=lambda self, hero: heal(hero,random.randint(2,5))),
                      Equipment("or", "o", use=lambda self, hero: amasser(hero,self)),
                      Arme("dague", effect={'strength': 3}, use = lambda self, hero: boost(hero,self.effect)),
                      Amulette(name="AmuCrit",abbrv="C", effect={'strength': 1}, use=lambda self, hero: boost(hero,self.effect)),
                      Amulette(name="AmuHeal", effect={'hpMax': 5}, use=lambda self, hero: boost(hero,self.effect))],
    
                  1: [Equipment("potion", "T", use=lambda self, hero: teleport(hero, True)),
                      Wearable(name="armure de bronze",abbrv="ab",place='corps', effect={'defense': 1}, use=lambda self,hero: boost(hero,self.effect)),
                      Arme(name="épée", effect={'strength': 2}, use=lambda self, hero: boost(hero,self.effect)),
                      Marchand()],
                  
                  2: [Arme(name="arc", effect={'strength': 2}, use=lambda self, hero: hero.throw(5, 2,"normal",4)),
                      Arme(name="halbarde", effect={'strength': 3}, use=lambda self, hero: boost(hero,self.effect)),
                      Wearable(name="armure d argent", abbrv="aa" ,place='corps', effect={'defense': 2}, use=lambda self,hero: boost(hero,self.effect)),
                      Equipment("or", "o", use=lambda self, hero: amasser(hero,self)),
                      Equipment("acier","a", use=lambda self, hero: amasser(hero,self)),
                      Forgeron()],
                      
                  3: [Equipment("portoloin", "w", use=lambda self, hero: teleport(hero, False)),
                      Wearable(name="armure d or", abbrv="ao", place='corps', effect={'defense': 3}, use=lambda self,hero: boost(hero,self.effect)),
                      Arme(name="Arc de poison", effect={'strength': 2}, use=lambda self, hero: hero.throw(5, 2,"poison",4)),
                      Arme(name="Arc de gel", effect={'strength': 2}, use=lambda self, hero: hero.throw(4, 2,"frozen",2,30))],

                  5: [Arme(name="Excalibur",abbrv="X", effect={'strength': 5}, use=lambda self, hero: boost(hero,self.effect)),
                      Equipment("Pierre Philosophale","pp",use = lambda self,hero: revive(1,hero)),
                      Equipment("Full boost","fb",use = lambda self, hero: fullBoost(hero,5,2,2)),
                      Marchand()]
        
                  }
    
    """monstres disponibles """
    monsters = {0: [Creature("Goblin", 4), Creature("Bat", 2, "W", categorie="distance", rangeAtk=5, elementAtk="poison", timeEffect=4,proba=80)],
                1: [Creature("Ork", 6,"O",2), Creature("Blob", 10), Creature("Archer", 6, categorie="distance", rangeAtk=4)], 
                2: [Creature("Archer empoisonné", 6, "k",2, categorie="distance", rangeAtk=4, elementAtk="poison", timeEffect=4,proba=90)],
                3: [Creature("Mage de glace", 6, "m",1, categorie="distance", rangeAtk=3, elementAtk="freeze", timeEffect=1,proba=30)],
                5: [Creature("Dragon", 15, strength=3, categorie="distance", rangeAtk=3)]}
    
    """ actions disponibles """
    _actions = {'z': lambda h: theGame.theGame()._floor.move(h, Coord(0, -1)), \
                'q': lambda h: theGame.theGame()._floor.move(h, Coord(-1, 0)), \
                's': lambda h: theGame.theGame()._floor.move(h, Coord(0, 1)), \
                'd': lambda h: theGame.theGame()._floor.move(h, Coord(1, 0)), \
                'i': lambda h: theGame.theGame().addMessage(h.fullDescription()), \
                'k': lambda h: h.__setattr__('hp', 0), \
                'u': lambda h: h.use(theGame.theGame().select(h._inventory)), \
                'space': lambda h: None, \
                'h': lambda h: theGame.theGame().addMessage("Actions disponibles : " + str(list(Game._actions.keys()))), \
                'p': lambda h: theGame.theGame().pause(), \
                'a' : lambda h : theGame.theGame().drop(h._inventory), \
                't': lambda h: h.shot(), \
                'b' : lambda h : h.unEquip(theGame.theGame().select(h.body)),
                }

    """Liste des boss"""
    boss = {0: [Boss("Robin",categorie="distance",rangeAtk=4, elementAtk="poison", timeEffect=4,proba=90),Boss("Ragnar"),Boss("Joker"),Boss("Radahn"),Boss("Grievous"),Boss("Thanos")]}

    def __init__(self, level=0, hero=None):
        self._level = level
        self._messages = []
        if hero == None:
            hero = Hero()
        self._hero = hero
        self._floor = None
        self.boss= Boss(name="Neutral")  ###Boss d'initialisation
        self.kill=0
        
    def buildFloor(self):
        """Crée une carte pour l'étage actuel."""
        self._floor = Map(hero=self._hero)
        self.boss=self.buildBoss()                                  #On stocke le boss dans l'argument d'instance
        self._floor.put(self._floor._rooms[-1].center(), self.boss) #On ajoute un Boss que l'on doit vaincre pour accéder à l'escalier
        theGame.theGame().addMessage(self.boss.name+" est le boss. Tue le et débloque l'escalier")
        self._level += 1

    def buildBoss(self):
        """Choisi le boss et défini ses stats"""
        boss=self.randElement(Game.boss)
        strength=0
        hp=0
        if 1<self._level<=3:    #Selon l'étage on ajoute plus ou moins de force au boss et de hp ( à équilibrer)
            strength+=2
            hp+=3
        elif 4<self._level<=5:
            strength+=3
            hp+=6
        boost(boss,{"strength":strength,"hp": hp})  #On applique les buffs pour le boss
        return boss

    def buildStairs(self): 
        """Ajoute un escalier dans la dernière salle de la map"""
        self._floor.put(self._floor._rooms[-1].center(), Stairs())

    def addMessage(self, msg):
        """Ajoute un message dans la liste des messages."""
        self._messages.append(msg)

    def readMessages(self):
        """Renvoie un clone d'un élément aléatoire d'une collection en utilisant la loi aléatoire exponentielle."""
        s = ''
        for m in self._messages:
            s += m + '. '
        self._messages.clear()
        return s

    def randElement(self, collect,rarity=0):
        """Renvoie un monstre aléatoire."""
        #rarity est la rareté minimum de la liste
        x=-1
        while x<rarity:
            x = random.expovariate(1 / (self._level+1))
        for k in collect.keys():
            if k <= x:
                l = collect[k]
        return copy.copy(random.choice(l))

    def randEquipment(self):
        """Renvoie un équipement aléatoire."""
        return self.randElement(Game.equipments)

    def randMonster(self):
        """Renvoie un monstre aléatoire."""
        return self.randElement(Game.monsters)

    def select(self, l):
        """Permet un choix dans la liste mit en entrée"""
        print("Choose item> " + str([str(l.index(e)) + ": " + e.name for e in l])+ " or e for exit")
        c=None
        while c not in [str(l.index(e)) for e in l] + ['e']:
            time.sleep(0.5)
            c = keyboard.read_key()     #Entrée clavier
            if c.isdigit() and int(c) in range(len(l)):
                return l[int(c)]
            if c =="e":
                return None

    def pause(self):
        """Arrête le jeu et permet d'arrêter le jeu"""
        print("Pause")
        print("Tap r to resume or e for exit")
        c=None
        while c not in ['e','r']:
            c = keyboard.read_key()     #Entrée clavier
            if c == 'e' :                                       
                Game._actions['k'](self._hero)        #Provoque fin du jeu          
            elif c == 'r':
                print('Soit prêt')
                time.sleep(0.5)
                return True

    def drop(self, l):
        "Permet au héros de déposer un objet sur le sol"
        item=self.select(l)
        time.sleep(0.5)
        if item is not False:
            c = None
            while c not in ["z","q","s","d"]:
                print("Chose a case to drop ? > z : top, q : left, s : down, d : right")
                c=keyboard.read_key()
                time.sleep(0.5)
                if c in ["z","q","s","d"]:
                    dir=self._floor.dir[c]
                    coordDrop=self._floor.pos(self._hero)+dir
                    if self._floor.get(coordDrop) != self._floor.ground:             #Assure une case accessible pour le drop de l'objet
                        c=None
                        print("No item in a wall >:(")
                    print("You drop " + item.name + " at " +str(coordDrop))
                else:
                     c=None
           
            self._floor.put(coordDrop,item)            #Pose l'item droppé
            l.remove(item)                             #Enlève de l'inv
        else:
            return None

    def selectPerso(self):
        """Fonction qui gère le choix du perso au début du jeu"""
        perso = [
        Hero(name="SwordMan", hp=20, abbrv="@", strength=4, size=5, txt=" @ : vous etes un epéiste de talent. votre point fort ? l'attaque ! Vous commencez avec une épée", inventory=[Arme(name="épée", effect={'strength': 2}, use=lambda self, hero: boost(hero,self.effect))],acier=1),
        Hero(name="Tank", hp=30, abbrv="R", strength=2, size= 3, txt=" R : Vous etes un homme énorme qui sait encaisser des dégats. vous commencez avec une armure ", inventory=[Wearable(name="armure de bronze",abbrv="ab",place='corps', effect={'defense': 1}, use=lambda self,hero: boost(hero,self.effect))]),
        Hero(name="Archer", hp=15, abbrv="F", strength=2, size=5, txt=" F : vous etes une archere qui fait pas mal de dégats et qui commence avec un arc", inventory=[Arme(name="arc", effect={'strength': 2}, use=lambda self, hero: hero.throw(5, 2,"normal",4))],argent=1),
        Hero(name="LuckyGirl", hp=20, abbrv="L", strength=2, size=8, txt=" L : Vous etes une femme chanceuse qui commence avec 3 gold et deux objets aléatoire",inventory=[self.randEquipment(),self.randEquipment()],argent=3, acier=1)]
        #cette fonction permet de selectionner un personnage en début de partie
        c="r"

        while c=="r":
            print("Choisit ton héro > " + str([str(perso.index(e)) + ": " + e.name+" > " for e in perso]))  #on présente les perso
            print("Tape i pour plus d'informations sur les héros"+"\n")
            c = keyboard.read_key()
            time.sleep(0.3)
            if c=="i":
                print("Des infos sur quel héros ? > " + str([str(perso.index(e)) + ": " + e.name+" ?> " for e in perso]))
                d=keyboard.read_key()
                time.sleep(0.3)
                if d.isdigit() and int(d) in range(len(perso)):
                    print(perso[int(d)].name+" > "+perso[int(d)].txt)       #on decrit les perso
                    print("press r for return"+"\n")
                    c=keyboard.read_key()
                    time.sleep(0.3)
                    while c !='r':
                        c=keyboard.read_key()
                        time.sleep(0.3)
                else:
                    c="r" 
            elif c.isdigit() and int(c) in range(len(perso)):
                self._hero=copy.copy(perso[int(c)])
            else:
                c="r" 

    def restart(self):
        """Boucle de jeu principale"""
        self._level = 0
        self.kill = 0
        self._hero = Hero()
        theGame.theGame().play()
            
    def play(self):
        """Main game loop"""
        self.selectPerso()
        self.buildFloor()
        print("--- Welcome Hero! ---")
        while self._hero.hp > 0 and self._hero.vie > 0 :        #Tant que le héros est en vie
            print(self._level)
            print(self._floor)
            print(self._hero.description())
            print(self.readMessages())
            c = keyboard.read_key()     #Entrée clavier
            time.sleep(0.1)             #Temps d'attente pour éviter les appuies de touches involontaires
            if c in Game._actions:
                if c in ['z','q','s','d']: #On ajoute 1 au compteur pour chaque déplacement 
                    Amu=self._hero.body[0]
                    if isinstance(Amu,Amulette):
                        self._hero.compteur+=1
                        if Amu.name=="AmuHeal":     #Les effets s'active en fonction de l'amulette
                            Amu.regeneration(self._hero,20,4)
                        if Amu.name=="AmuCrit":
                            Amu.coupCrit(self._hero,5,10)
                if c in ['p','k', 'i'] or self._hero.state != 'freeze':
                    Game._actions[c](self._hero)
                if c != 'p':                    #Pas de mouvement de monstre après une pause (on est pas sadique)
                    self._floor.moveAllMonsters()
                    if self.boss in self._floor._elem:  #On vérifie si le boss est toujours en vie
                        if self.boss.name in ["Joker"] :        #liste des noms des bosses qui peuvent invoquer des sbires
                            self.boss.spawnArmy(self._floor,self.randMonster(),self._hero,8)       #Le boss invoque un sbire
                    if self.boss not in self._floor._elem and not isinstance(self._floor.get(self._floor._rooms[-1].center()), Stairs) and not isinstance(self._floor.get(self._floor._rooms[-1].center()), Creature):      #Quand le Boss meurt on ajoute l'escalier
                        self.buildStairs()
                    if self._hero.state == "poison":
                        self._hero.hp-=1
                        theGame.theGame().addMessage(str(self._hero)+" is poisoned, he take a damage ")
                if self._hero.hp <= 0:
                    self._hero.vie-=1
                    self._hero.hp=self._hero.hpMax

        print(self.readMessages())            
        print("--- Game Over ---")
        print("Félicitation vous avez atteint l'étage",self._level," ! Vous avez aussi tué",self.kill+self._level-1,"monstres !\nVotre score est de",(self._level-1)*1000+self.kill*50,"points\n")
        print("Rejouer ?\nAppuyez sur y pour oui ou n pour non")
        c=None
        while c not in ['y','n']:
            c=keyboard.read_key()
            time.sleep(0.3)
            if c =='y':
                theGame.theGame().restart()     #Pour recommencer un nouveau jeu
        print("Merci d'avoir joué !")


