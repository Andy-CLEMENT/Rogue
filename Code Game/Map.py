from Coord import Coord
from Hero import Hero
from Room import Room
from Element import Element
from Equipment import Equipment
from Creature import Creature
from utils import sign
from handler import tir
import theGame
import random, copy

class Map(object):
    """Une carte d'un étage du jeu
        Contient les éléments du jeu """

    ground = '.'  # On peut marcher dessus
    dir = {'z': Coord(0, -1), 's': Coord(0, 1), 'd': Coord(1, 0), 'q': Coord(-1, 0)}  # four direction user keys
    empty = ' '  # On peut pas marcher dessus
    fog = '#' # Partie non visible de la carte

    def __init__(self, size=random.randint(35,45), hero=None):
        self._size=size
        self._mat = []
        self._elem = {}
        self._rooms = []
        self._roomsToReach = []

        for i in range(size):
            self._mat.append([Map.empty] * size)
        if hero is None:
            hero = Hero()
        self._hero = hero
        self.generateRooms(random.randint(7,13))
        self.reachAllRooms()
        self.put(self._rooms[0].center(), hero)
        for r in self._rooms[1:]:                   #la salle de départ de l'étage est vide, on respire
            r.decorate(self)
        
        
    def addRoom(self, room):
        """Ajoute une salle sur la carte."""
        self._roomsToReach.append(room)
        for y in range(room.c1.y, room.c2.y + 1):
            for x in range(room.c1.x, room.c2.x + 1):
                self._mat[y][x] = Map.ground

    def findRoom(self, coord):
        """Si la coordonnée est dans une salle, retourne la salle où elle se trouve (la coordonnée) sinon renvoie None"""
        for r in self._roomsToReach:
            if coord in r:
                return r
        return None

    def intersectNone(self, room):
        """Test si une salles n'est pas en superposition avec une autre salle"""
        for r in self._roomsToReach:
            if room.intersect(r):
                return False
        return True

    def dig(self, coord):
        """Ajoute un élement de sol sur la coordonnée voulu.
          Si la coordonnée correspond à une salle, on considère la salle reliée."""
        self._mat[coord.y][coord.x] = Map.ground
        r = self.findRoom(coord)
        if r:
            self._roomsToReach.remove(r)
            self._rooms.append(r)

    def corridor(self, cursor, end):
        """Creuse un couloir depuis les coordonées du curseur jusqu'à la fin, et verticale puis en horizontal"""
        d = end - cursor
        self.dig(cursor)
        while cursor.y != end.y:
            cursor = cursor + Coord(0, sign(d.y))
            self.dig(cursor)
        while cursor.x != end.x:
            cursor = cursor + Coord(sign(d.x), 0)
            self.dig(cursor)

    def reach(self):
        """relie 2 salles entre elles.
           Commence par une salle reliée, et creuse un couloir vers une salle non reliée  ."""
        roomA = random.choice(self._rooms)
        roomB = random.choice(self._roomsToReach)

        self.corridor(roomA.center(), roomB.center())

    def reachAllRooms(self):
        """Relie toutes les salles entre elles.
            Commence par la première, repète x fois la fonction reach tant que toutes les salles ne sont pas reliées."""
        self._rooms.append(self._roomsToReach.pop(0))
        while len(self._roomsToReach) > 0:
            self.reach()

    def randRoom(self):
        """Une salle aléatoire qui est placée sur la carte."""
        c1 = Coord(random.randint(0, len(self) - 3), random.randint(0, len(self) - 3))
        c2 = Coord(min(c1.x + random.randint(3, 8), len(self) - 1), min(c1.y + random.randint(3, 8), len(self) - 1))
        return Room(c1, c2)

    def generateRooms(self, n):
        """Genére n salles aléatoire et les relie si elles ne sont pas reliées ."""
        for i in range(n):
            r = self.randRoom()
            if self.intersectNone(r):
                self.addRoom(r)

    def __len__(self):
        return len(self._mat)

    def __contains__(self, item):
        if isinstance(item, Coord):
            return 0 <= item.x < len(self) and 0 <= item.y < len(self)
        return item in self._elem

    def __repr__(self):
        s = ""
        for i in self._mat:
            for j in i:
                s += str(j)
            s += '\n'
        return s

    def checkCoord(self, c):
        """Vérifie si la coordonnée c est valide sur la carte."""
        if not isinstance(c, Coord):
            raise TypeError('Not a Coord')
        if not c in self:
            raise IndexError('Out of map coord')

    def checkElement(self, o):
        """Vérifie si o est un Element."""
        if not isinstance(o, Element):
            raise TypeError('Not a Element')

    def put(self, c, o):
        """Ajoute un element o sur la case c"""
        self.checkCoord(c)
        self.checkElement(o)
        if self._mat[c.y][c.x] != Map.ground:
            raise ValueError('Incorrect cell')
        if o in self._elem:
            raise KeyError('Already placed')
        self._mat[c.y][c.x] = o
        self._elem[o] = c

    def get(self, c):
        """Renvoie l'objet present sur la case c"""
        self.checkCoord(c)
        return self._mat[c.y][c.x]

    def pos(self, o):
        """Renvoie les coordonnées d'un element sur la carte """
        self.checkElement(o)
        return self._elem[o]

    def rm(self, c):
        """Supprime un element sur la coordonnée c"""
        self.checkCoord(c)
        del self._elem[self._mat[c.y][c.x]]
        self._mat[c.y][c.x] = Map.ground

    def move(self, e, way):
        """Déplace un élement e dans la direction way."""
        coordMonster = self.pos(e)
        dest = coordMonster + way
        
        if dest in self:
            objDest=self.get(dest)
            if objDest == Map.ground:
                self._mat[coordMonster.y][coordMonster.x] = Map.ground
                self._mat[dest.y][dest.x] = e
                self._elem[e] = dest
            else:
                if isinstance(objDest,Creature):
                    if objDest.name in ["Thanos"] and objDest.meet(e)==False: #Si le boss subit des dégats, il se téléporte
                        objDest.tpBoss()
                if objDest != Map.empty and (hasattr(objDest,"hp") or isinstance(e,Hero)) and objDest.meet(e) and objDest != self._hero:
                    if isinstance(objDest,Creature):
                        theGame.theGame().kill+=1
                        self.rm(dest)
                        drop=random.randint(1,10)
                        if drop == 5 or drop == 10:
                            self.put(dest, copy.copy(Equipment("or", "o")))
                        if drop == 2 :
                            self.put(dest, copy.copy(Equipment("acier", "a")))
                    else :
                        self.rm(dest)


    def moveAllMonsters(self):
        """Déplace tout les monstres de la carte.
            Si un monstre est à moins de 6 de distance du hero, le monstre avance."""
        coordHero = self.pos(self._hero)
        for e in self._elem.copy():
            coordMonster = self.pos(e)
            if isinstance(e, Creature):
                if e.stateTime <= 0:
                    e.state = "normal"
                else:
                    e.stateTime-=1
                if e != self._hero and coordMonster.distance(coordHero) < 6 and e.state!='freeze':
                    #si la creature peut tirrer à distance à distance sur le héro elle le fait
                    if e.categorie=="distance" and coordMonster.distance(coordHero)<=e.rangeAtk and (coordHero.x==coordMonster.x or coordHero.y==coordMonster.y):
                        tir(self.pos(e),self.pos(e).direction(coordHero),e.rangeAtk,e.strength,e.elementAtk,e.timeEffect, proba=e.proba)

                    #sinon elle avance en direction du hero.
                    else:
                        dir=coordMonster.direction(coordHero)
                        #si la creature a un obstacle devant elle, elle le contourne
                        if self.get(coordMonster+dir)!=Map.ground and type(self.get(coordMonster+dir))!=Hero:
                            if dir.x==0:
                                if coordMonster+Coord(1,0) in self and self.get(coordMonster+Coord(1,0))==Map.ground:    #regarde si elle peut aller a droite
                                    dir=Coord(1,0)
                                else:
                                    dir=Coord(-1,0)                                                        #sinon à gauche
                                if coordMonster+Coord(-1,0) in self and self.get(coordMonster+Coord(-1,0))==Map.ground and (coordMonster+Coord(-1,0)).distance(coordHero)<=(coordMonster+Coord(1,0)).distance(coordHero):                       #si les deux mais plus court a gauche
                                    dir=Coord(-1,0)
                            else:
                                if coordMonster+Coord(0,1) in self and self.get(coordMonster+Coord(0,1))==Map.ground:
                                    dir=Coord(0,1)
                                else:
                                    dir=Coord(0,-1)
                                if coordMonster+Coord(0,-1) in self and self.get(coordMonster+Coord(0,-1))==Map.ground and (coordMonster+Coord(0,-1)).distance(coordHero)<=(coordMonster+Coord(0,1)).distance(coordHero):
                                    dir=Coord(0,-1)
                        self.move(e,dir)
                    if e.state == 'poison':
                        e.hp -=1
                    if e.hp<=0 :
                        self.rm(coordMonster)
                elif e.state == 'freeze':
                    theGame.theGame().addMessage(str(e.name)+" est glacé, il ne peut pas bouger")

    def vision(self):
        """Retourne une copie de la carte selon la vision du héros"""
        coordHero = self.pos(self._hero)
        visionHero=[]
        for y in range(self._size):             #On crée une copie de la carte, mais on met du brouillard (Map.fog) là le héros ne voit pas, ainsi on peut afficher cette copie sans toucher à la vraie carte
            visionHero.append([Map.empty] * self._size)
            for x in range(self._size):
                coordTest=Coord(x,y)
                if coordHero.distance(coordTest)>= self._hero.vision and self.get(coordTest)!= Map.empty:
                    visionHero[y][x] = Map.fog
                else:
                    visionHero[y][x] = self._mat[y][x]
        s = ""
        for i in visionHero:
            for j in i:
                s += str(j)
            s += '\n'
        return s        
