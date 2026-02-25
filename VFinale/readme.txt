┌────────────────────────────────────────────────┐
│                                                │
│             _                          _ _     │
│    __ _  __| | ___ ____           __ _(_) |_   │
│   / _` |/ _` |/ __|_  /  _____   / _` | | __|  │
│  | (_| | (_| | (__ / /  |_____| | (_| | | |_   │
│   \__,_|\__,_|\___/___|          \__, |_|\__|  │
│                                  |___/         │
│                                                │
└────────────────────────────────────────────────┘

###################################
###################################
####  Les fichiers qu'il y a  #####
###################################
###################################

/home/adcz/00-Laptop/Nsi/Projet/VFinale/
├── game.py
├── player.py
├── blank.py
├── tableau.py
├── tab.py
├── constructeur_tableau.py
├── etat_jeu.py
├── gravite.py
├── image
│   └── style-pixel-art-vecteur-croissant-lune-style-18-bits_682225-124.avif
├── bar_vie.py
├── deplacement_openworld.py
├── mob_hostile_1.py
├── attaque.py
└── pixel_art.py

2 directories, 14 files

#######################################
#######################################
#######   DEPENDANCES PY    ###########
#######################################
#######################################

- tkinter
- tkinter.font
- random
- math


##########################
##########################
#####    FICHIERS    #####       <-- C'est ici les trucs importants
##########################
##########################

===================================

game.py
 -- Import # des imports c tout, y a les bibliothèques utiles et les fichiers qu'on utilise
 -- Zoom # juste pour zoomer plus ou moins la fenêtre (la valeur se change dans etat_jeu.py)
 -- La fenêtre avec root et canva
 -- Appel des fonctions de créations de tableau et des persos / mob
 -- Update  <-- Lui il est important les autres on s'en fout un peu
 	-- Il rappelle récursivement la plupart des fonctions qui font tourner le jeu :
		-- gravité
		-- déplacement
		-- tracking des mob
		-- etc.
	
	-- En gros si ça s'arrête le jeu ne tourne plus


==================================

player.py # c le dessin du perso y a rien de sorcier

==================================

blank.py # c'est juste un canva vide, c utile pour faire les dessins avant de les mettre dans le jeu

==================================

tableau.py ou tab.py ça va dépendre si tab.py fonctionne
 -- des tableaux de 32x18
 -- pour le moment il y a que quelques numéros réservés :
 	-- 0, la case est vide on peut y aller
	-- 1, y a une mur
	-- 2, c'est les sorties du tableaux pour aller dun tableau à un autre
	-- 9, c'est le point d'appartition du mob1
	-- pour les autres mob on prendra d'autres numéros et pour les boss ils en auront un à part je pense
	-- il en faut un pour les checkpoint aussi

==================================

constructeur_tableau.py # parcours le tableau donné en deux fois
	-- la première fois il place que les murs
	-- la deuxième, les mobs et les décors si on en met # comme ça ils ne sont pas cachées par les murs


==================================

etat_jeu.py # y a tous les flags, toutes les coordonées, tout ce qui gère le jeu en fait
	      y a des trucs qu'on peut bouger et d'autres qu'il faut éviter
	      pour savoir si on peut changer faut juste voir si le jeu marche encore après un changement :)


=================================

gravite.py # bah ça gère la gravité
	-- pour le fonctionnement :
		-- pour noah (et lucas on sait jamais):
			- tant que le bonhomme touche le sol il descend pas

		-- pour les autres :
			il y a une variable de vitesse verticale, à laquelle on ajoute constament une valeur proportionnelle à la gravité
			donné.
			A chaque récurrence si le perso est au sol la variable est replacé à 0, sinon, il y a un .move qui le fait redescendre
			en fonction de la variable. Il y a un facteur mais j'ai oublié.

			-> Pour le saut cette variable est juste placé en négative


=================================

image/ # dedans y a qu'une seule image pour le moment, c'est l'apparence que je voulais donner pour l'attaque mais j'ai la flemme de le 
	 dessiner. Du coup je vous laisse faire


================================

bar_vie.py # ça dessine juste la barre de vie en haut à gauche, c'est un for in range c tout con.
	     et quand les pv sont <= 0, on met écran noir avec game over :(


================================

deplacement_openworld.py # c'est pour faire bouger le perso sur l'axe x (gauche ou droite)

			   	-- le petit bonhomme regarde si y a un mur ou pas et il evite de se le prendre
				   c'est tout pour le fonctionnement

				   -> !!! ça fonctionne pareil pour les mobs donc si vous comprenez pas demandez à Noam
				   	  sinon vous risquez d'être dans le mal


==================================

mob_hostile_1.py # c'est une classe avec le premier type de mob, il y a juste une hitbox j'avait la flemme de le 
		   dessiner donc vous pouver mettre ce que vous voulez, vous avez juste àà remplacé le rectangle par
		   votre dessin.

		   Pour les autres type de mob en gros vous pouvez juste faire un copier coller et changer la valeur des 
		   attributs j'ai fait en sorte que ce soit facile à refaire donc les valeurs sont générale
		   == il suffit de changer la valeur des attributs

		   Il n'y a que l'attaque qui peut être plus chiant
		   	- pour celui la c'est un tir et la hitbox et généreuse j'ai juste vérifier le centre donc éviter 
			  de faire le cercle trop grand

			- si vous voulez qu'il fasses des attaques de méler vous pouvez juste reprendre l'attaque du perso 
			  jouable, et la fonction qui vérifie s'il a touché quelque chose

		  Si vous voulez faire un tout nouveau mob complètement différent, demandez à Noam, je crois suffisemment en 
		  lui pour refaire une class à partir de 0.
		  Sinon faites un copier coller et changez les chiffres, les noms sont vraiment explicite donc réfléchissez un
		  peu avant de faire une connerie

		  Pour se déplacer au fait, il se dirige juste vers le joueurs, il a pas de cerveaux


================================

attaque.py # c'est surtout le dessin des attaques (des carrés rouges, faudra changer ça fait vrm dégueu)
	     mais en gros y a rien de compliqué
	     	- la première fonction décide dans quel sens est l'attaque (gauche droite haut bas)
			- elle appelle une autre fonction (qui dessine l'attaque)
				- ça appelle encore une autre fonction et ça enclenche le cooldown de l'atk
					- si y a quelque chose dans le carré
						- on retire des pv au mob et il à un recul
							- si ça tombe à zero, le mob meur
					- si y a rien il se passe rien


=================================

#################################
#################################
###  CE QUI RESTE A FAIRE    ####
#################################
#################################

fichier de sauvegarde (optionnel on a pas vrm de mode histoire)
	- sinon faut juste l'emplacement du dernier checkpoint, avec le tableau dans lequel c'est)

les checkpoints, suffit de lui attribuer un numéro dans les tableau est de le rendre intéractif
	-> if jeu[ej.touche_haut] and checkpoint() :
		jeu["pv"] = 10

	c tout, et checkpoint() juste faut vérifier les cases autour du perso

la déco : donner un dessin aux mob, aux attaques et mettre un fond
	- je pensais à juste faire un fond sur minecraft comme c tout carré ça peut rendre bien, et on fait un screen
	pour l'image c pas compliqué on fait un liste de liste avec les tableau [[tableau], image] et quand on construit
	le tableau, au lieu de mettre les cases on met l'image et ça peut rendre bien

	( on met un texture pack si on veut pas que ça ressemble trop au jeu de base )

les changements de tableaux, pas compliqué :
	delete("player")
	jeu["lst_mob"] = []
	jeu["lst_projectile] = [] # c'est mm pas obligé ils se retirent tout seul

	créer un fond noir 
	coller l'image ou les cases, recréer le joueur et les mobs

	si vous voulez faire simple, mettez un numéro random sur le tableau ce sera l'endroit ou le joueur réapparait.


et en gros je crois c tout

======================================

si vous comprenez pas demandez à Noam je lui fait confiance pour comprendre ce que j'ai fait
