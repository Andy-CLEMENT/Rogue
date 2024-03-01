# Rogue
Projet de jeu Rogue-like en language python réalisé dans le but de la formation de prépa intégrée de Polytech Nice-Sophia

READ THIS:
Il faut installer le module keyboard pour le bon fonctionnement du jeu

Dès que vous commencez vous devez choisir votre héros. Quatre choix s’offrent à vous. Pour plus d’informations sur leur spécificité appuyez sur “i”.

Vous êtes à présent en jeu. Vous pouvez vous déplacer afin de chercher de l’équipement ou des objets. 
Attention des monstres vous attaqueront, certains peuvent vous donner des effets ou vous attaquer à distance. 
Vous pouvez récolter de l’or afin d’acheter de l’équipement au marchand ou de l’acier afin que le forgerons vous améliore un équipement. 
Votre objectif est de trouver le boss de l’étage et de le vaincre. C'est seulement après qu’un escalier apparaitra pour vous emmener à l’étage suivant. 

 
                            Commande clavier :
Commande personnage :
    Haut:       z
    Bas:        s
    Gauche:     q
    Droite:	    d
    Tirer un projectile: t
    Utiliser:	u
    Déséquiper:	b
    Jeter:      a

Commande de Gameplay :
    Menu Pause:     p
    Suicider:       k
    Description du personnage:	i
    Voir actions possible:  h


                            Elément :
Objet :
    Potion "!":             Augmente les points de vie (2-5)
    Potion TP "!":	        Vous téléporte sur la carte (usage unique)
    Gold "o":               Utilisée pour l’échange avec le marchand
    Acier "a":              Utilisée pour l’échange avec le forgeron
    Portoloin "w":          Vous téléporte sur la carte (usage permanent)
    Pierre philosophale:    Permet d'avoir une seconde vie 
    FullBoost:              Augmente de façon permanente les stats du héro

Armes :
    Epée "é":           Donne plus de force
    Hallebarde "H":     Donne plus de force
    Excalibur "X":      Donne plus de force

Armes à distance :
    Dagger "d":     Faible portée, faible dégâts
    Bow “b”:        Longue portée
    Poison bow “p”:	Longue portée, empoisonne l’ennemi
    Frozen bow “f”:	Moyenne portée, freeze l’ennemi pendant deux tour (30% de chance)

Armures :
    Armure de bronze:   Augmente la défense
    Armure d’argent:	Augmente la défense
    Armure d’or:        Augmente la défense
*PS : la défense est une réduction de dégâts 


Amulette :
    Amuheal “A”:    Augmente le nombre de PV maximal du héros et régénère ça santé au bout de n tours
    Amucrit “C”:    Augmente la force et débloque la possibilité d’assener un coup critique tous les n tours



                            Creatures :

Héros:
    SwordMan "@" :  epéiste de talent
    Tank "R":       homme énorme qui sait encaisser des dégats
    Archer "F":     archere qui commence avec un arc
    LuckyGirl "L":  Comence avec 3 golds et 2 objets aléatoires

Monstre :
    Archer empoisonné "k":  Lance des flèches empoisonnées
    Mage de glace "m":      Lance des projectiles qui immobilise la cible
    Archer "A":             Lance des projectiles
    Chauve-Souris "W":      Lance des projectiles empoisonnées

Boss :
Abréviation des bosses = « $ »
    Robin:      Boss qui jette des projectiles
    Joker:      Boss qui invoque des sbires chaque n tour
    Thanos: 	Boss qui se téléporte à chaque fois qu’il subit des dégâts 
    Ragnar:	    Boss corp-à-corps
    Grievious:	Boss corp-à-corps
    Radahn:	    Boss corp-à-corps
