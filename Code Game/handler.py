import theGame
import random, time
from Projectile import Projectile
from Boss import Boss

def heal(creature,n): #On peut choisir le nombre de pv que l'on ajoute (n)
    """Heal the creature"""
    gain = creature.hp + n
    if gain > creature.hpMax: #On vérifie que les gains de PV ne dépase pas le max de P
        creature.hp=creature.hpMax
    else:
        creature.hp=gain
    return True

def teleport(creature, unique):
    """Teleporte the creature"""
    r = random.choice(theGame.theGame()._floor._rooms)
    c = r.randEmptyCoord(theGame.theGame()._floor)
    if theGame.theGame()._floor.get(c):
        theGame.theGame()._floor.rm(theGame.theGame()._floor.pos(creature))
        theGame.theGame()._floor.put(c, creature)
    return unique

def tir(coordUser, dir, rangeAtk, strength, elementAtk,timeEffect,proba):
    #tir sert a tirer une fleche. elle peut etre utilisée par le hero comme les creatures et peut donner des effets à la cible (proba)
    p=Projectile("arrow",abbrv="*",rangeAtk=rangeAtk, strength=strength,elementAtk=elementAtk,timeEffect=timeEffect,proba=proba)
    stage=theGame.theGame()._floor

    if coordUser+dir in stage:            #si attaque à distance
        time.sleep(0.15)
        cible=stage.get(coordUser+dir)
        if cible==stage.ground:
            stage.put(coordUser+dir, p)            #on pose la fleche sur la map
            print(stage.vision())
            time.sleep(0.15)
            cible=stage.get(stage.pos(p)+dir)
            i=0
            while i<rangeAtk-1 and stage.pos(p)+dir in stage and (cible==stage.ground or hasattr(cible,"hp")) and (hasattr(stage.get(coordUser),"txt")==False and hasattr(cible,"hp")==True and hasattr(cible,"txt")==False)==False :            #on effectue les déplacements du projectile jusqu'a ce qu'il atteingne sa cible ou sa portée, et évite que les créatures se blessent entre elles
                a=stage.move(p,dir)
                if hasattr(cible,"hp") and p.elementAtk!="normal" and random.randint(0,100)<=p.proba:            #on fait l'effet
                    cible.state=p.elementAtk
                    cible.stateTime=p.timeEffect
                print(stage.vision())
                time.sleep(0.15)
                if cible!=stage.ground or i==rangeAtk : #retire le projectile
                    stage.rm(stage.pos(p))
                    return True
                if stage.pos(p)+dir in stage:
                    cible=stage.get(stage.pos(p)+dir)            #on definie une nouvelle cible
                i+=1
            stage.rm(stage.pos(p)) #retire le projectile

        elif hasattr(cible,"hp") and (hasattr(stage.get(coordUser),"txt")==False and hasattr(cible,"hp")==True and hasattr(cible,"txt")==False)==False:             #si attaque au cac contre une creature ou un hero
            m=cible.meet(p)
            if m==True and hasattr(cible,"txt")==False:  #si la creature est morte et que ce n'est pas le héro
                stage.rm(coordUser+dir)
            elif p.elementAtk!="normal" and random.randint(0,100)<=p.proba:            #on fait l'effet
                cible.state=p.elementAtk
                cible.stateTime=p.timeEffect

def boost(creature,effect):         #Effect doit être un dictionnaire avec comme clés la stat et en valu la valeur de changement
                                    #On peut aggrémenter la fonction en ajoutant d'autre stat à modifier
    """Boost la caractéristique mis en argument"""
    if "strength" in effect.keys():
        n=effect["strength"]
        gain = creature.strength + n
        creature.strength=gain
        if isinstance(creature,Boss):
            theGame.theGame().addMessage(creature.name+" a "+str(creature.strength)+ " point(s) de force")
        else:
            theGame.theGame().addMessage(creature.name+" a gagné "+str(n)+ " point(s) de force")
            theGame.theGame().addMessage(creature.name+" a desormais "+str(creature.strength)+ " point(s) de force")
    if "hp" in effect.keys():   #Pour les boss 
        n=effect["hp"]
        gain = creature.hp + n
        creature.hp=gain
        theGame.theGame().addMessage(creature.name+" a "+str(creature.hp)+ " point(s) de vie")
    if "hpMax" in effect.keys():
        n=effect["hpMax"]
        gain = creature.hpMax + n
        creature.hpMax=gain
        theGame.theGame().addMessage(creature.name+" a gagné "+str(n)+ " point(s) de vie maximal")
        theGame.theGame().addMessage(creature.name+" a desormais "+str(creature.hpMax)+ " PV Max")
    if "defense" in effect.keys():
        n=effect["defense"]
        gain = creature.defense + n
        creature.defense=gain
        theGame.theGame().addMessage(creature.name+" a gagné "+str(n)+ " point(s) d'armure'")
        theGame.theGame().addMessage(creature.name+" a desormais "+str(creature.defense)+ " point(s) d'armure")
    
    return True

def nerf(creature,effect):          # nerf les capacité de la créature  selon les caractéristique de l'objet
    """nerf la caractéristique"""
    if "strength" in effect.keys():
        n=effect["strength"]
        creature.strength-=n
        theGame.theGame().addMessage(creature.name+" a desormais "+str(creature.strength)+ " point(s) de force")
    if "hpMax" in effect.keys():
        n=effect["hpMax"]
        creature.hpMax-=n
        if creature.hp > creature.hpMax: #Si les hp de la creature son plus haut que ces hpMax on reduit a hpMax
            creature.hp=creature.hpMax
        theGame.theGame().addMessage(creature.name+" a desormais "+str(creature.hpMax)+ " point(s) de vie maximal")
    if "defense" in effect.keys():
        n=effect["defense"]
        creature.defense-=n
        theGame.theGame().addMessage(creature.name+" a desormais "+str(creature.defense)+ " point(s) d'armure")
    return True

def revive(plusVie,creature):
    """Ajoute une vie suplémentaire"""
    creature.vie+=plusVie
    return True

def fullBoost(creature,plusHp,plusStr,plusDef):
    """Fait un boost général du héro"""
    creature.hp+= plusHp
    creature.hpMax+= plusHp
    creature.strength+= plusStr
    creature.defense+= plusDef
    return True

def amasser(hero,ressource):
    """Permet de mettre les pièces d'or et les lingots d'acier de son inventaire à son stock"""
    if ressource.name=='or':
        hero.argent+=1
    elif ressource.name=='acier':
        hero.acier+=1
    return True
