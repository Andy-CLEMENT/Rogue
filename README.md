<img src="https://upload.wikimedia.org/wikipedia/commons/9/9d/Polytechnicesophia.png" alt="Logo Polytech Nice Sophia" title="Logo Polytech Nice Sophia">


# Rogue
Projet de jeu Rogue-like en language python réalisé dans le but de la formation de prépa intégrée de Polytech Nice-Sophia.
Projet à quatre personnes.

<h1>READ THIS:</h1>
<p>Il faut installer le module keyboard pour le bon fonctionnement du jeu</p>

<p>Dès que vous commencez vous devez choisir votre héros. Quatre choix s’offrent à vous. Pour plus d’informations sur leur spécificité appuyez sur “i”.</p>

<p>Vous êtes à présent en jeu. Vous pouvez vous déplacer afin de chercher de l’équipement ou des objets. 
Attention des monstres vous attaqueront, certains peuvent vous donner des effets ou vous attaquer à distance. 
Vous pouvez récolter de l’or afin d’acheter de l’équipement au marchand ou de l’acier afin que le forgerons vous améliore un équipement. 
Votre objectif est de trouver le boss de l’étage et de le vaincre. C'est seulement après qu’un escalier apparaitra pour vous emmener à l’étage suivant. </p>

 
 <h2>Commande clavier :</h2>
<p>Commande personnage :
    <ul>
    <li>Haut:       z</li>
    <li>Bas:        s</li>
   <li>Gauche:     q</li>
    <li>Droite:	    d</li>
    <li>Tirer un projectile: t</li>
    <li>Utiliser:	u</li>
    <li>Déséquiper:	b</li>
    <li>Jeter:      a</li></ul></p>

<p>Commande de Gameplay :
   <ul>
    <li>Menu Pause:     p</li>
    <li>Suicider:       k</li>
    <li>Description du personnage:	i</li>
    <li>Voir actions possible:  h</li></ul></p>

<h2>Elément :</h2>
<p>Objet :
    <ul>
     <li>Potion "!":             Augmente les points de vie (2-5)</li>
     <li>Potion TP "!":	        Vous téléporte sur la carte (usage unique)</li>
     <li>Gold "o":               Utilisée pour l’échange avec le marchand</li>
     <li>Acier "a":              Utilisée pour l’échange avec le forgeron</li>
     <li>Portoloin "w":          Vous téléporte sur la carte (usage permanent)</li>
     <li>Pierre philosophale:    Permet d'avoir une seconde vie </li>
     <li>FullBoost:              Augmente de façon permanente les stats du héro </li></ul></p>

<p>Armes :
    <ul>
     <li>Epée "é":           Donne plus de force</li>
     <li>Hallebarde "H":     Donne plus de force</li>
     <li>Excalibur "X":      Donne plus de force</li></ul></p>

<p>Armes à distance :
    <ul>
    <li>Dagger "d":     Faible portée, faible dégâts</li>
    <li>Bow “b”:        Longue portée </li>
    <li>Poison bow “p”:	Longue portée, empoisonne l’ennemi</li>
    <li>Frozen bow “f”:	Moyenne portée, freeze l’ennemi pendant deux tour (30% de chance)</li></ul></p>

<p>Armures :
    <ul>
    <li>Armure de bronze:   Augmente la défense</li>
    <li>Armure d’argent:	Augmente la défense</li>
   <li> Armure d’or:        Augmente la défense</li></ul></p>
*PS : la défense est une réduction de dégâts 


<p>Amulette :
    <ul>
   <li>Amuheal “A”:    Augmente le nombre de PV maximal du héros et régénère ça santé au bout de n tours</li>
    <li>Amucrit “C”:    Augmente la force et débloque la possibilité d’assener un coup critique tous les n tours</li></ul></p>



<h2>Creatures </h2>

<p>Héros:
    <ul>
    <li>SwordMan "@" :  epéiste de talent</li>
    <li>Tank "R":       homme énorme qui sait encaisser des dégats</li>
    <li>Archer "F":     archere qui commence avec un arc</li>
    <li>LuckyGirl "L":  Comence avec 3 golds et 2 objets aléatoires</li></ul></p>

<p>Monstre :
    <ul>
     <li>Archer empoisonné "k":  Lance des flèches empoisonnées</li>
    <li>Mage de glace "m":      Lance des projectiles qui immobilise la cible</li>
    <li>Archer "A":             Lance des projectiles</li>
   <li> Chauve-Souris "W":      Lance des projectiles empoisonnées</li></ul></p>

<p>Boss :
Abréviation des bosses = « $ »
     <ul>
    <li>Robin:      Boss qui jette des projectiles</li>
    <li>Joker:      Boss qui invoque des sbires chaque n tour</li>
    <li>Thanos: 	Boss qui se téléporte à chaque fois qu’il subit des dégâts </li>
    <li>Ragnar:	    Boss corp-à-corps</li>
    <li>Grievious:	Boss corp-à-corps</li>
    <li>Radahn:	    Boss corp-à-corps</li></ul></p>
