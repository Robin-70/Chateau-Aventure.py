lieu = "tour"
action = ()
canne_a_peche = 1
rose = 2
poisson = 0
branche = 0
branche_cassee = 1
clé = 1
couronne = 1
bougie = 1
garde_KO = 1
poisson_troll = 1
rose_princesse = 1
couronne_tête = 0
clé_porte = 1
catatorche = 1
fantome = 0
couronne_terre = 0
choix = ()

def examiner(objet):
    if objet in description:
        print(description[objet])
    else:
        print("Vous ne voyez rien de spécial à propos de ", objet,".")

description = {"torche":"C'est un objet de combustion manuelle semi-portatif à activation pyrogène, destiné à la projection directionnelle et localisée d’un rayonnement électromagnétique dans le spectre visible, généralement utilisé en contexte de déplacement nocturne ou d’exploration de cavités naturelles. Une torche quoi ;)\n"}

def inventaire():
    print("Torche allumée\n")
    if canne_a_peche == 1:
        print("Canne à pêche\n")
    if rose != 0:
        print(rose, "Rose(s)")
    if poisson == 1:
        print("Poisson cru\n")
    if branche == 1:
        print("Branche morte\n")
    if branche_cassee == 1:
        print("Branche cassée\n")
    if couronne == 1:
        print("Couronne\n")
    if bougie == 1:
        print("Bougie\n")
    if clé == 1:
        print("Clé\n")

def help():
    print("Les principales commandes sont:\n- examiner (pour avoir la description du lieu\n- examiner ... (pour avoir la description de l'objet)\n- prendre\n- utiliser\n- sentir\n- donner ... à ...- allumer ... avec torche\n- frapper ... avec ...\n- sauter\n- asseoir sur trône\n- credits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)\n")

def credits():
    print("Antoine au codage, son père pour la relecture et Iello Games pour l'histoire\nMon amie Gabrielle pour la blague du poisson\nMerci à Klanbeeld pour la musique du jardin, du sentier, du très grand z'arbre, de l'escalier du bas.\n Merci à littlerobotsoundfactory pour les sons du troll. \nMerci à theuncertainman pour les sons du guarde.\n Merci à Toam pour les sons des catacombes.\nMerci à Gertraut Hecher, pour la musique de fin.\n")


print("Bienvenue à Château Aventure.\n\nTapez 'aide' pour avoir accès aux principales commandes du jeu.\n\n")

while True:
    if lieu == "hutte":
        if canne_a_peche == 0:
            print("Vous êtes debout dans une petite hutte.\nIl y a une canne à pêche ici.\n")
        if canne_a_peche == 1:
            print("Vous êtes debout dans une petite hutte.\n")
        while lieu == "hutte":
            action = input ()
            if action in ("examiner canne à pêche", "examiner canne a peche", "examiner canne à peche", "examiner canne a pêche", "examiner canne"):
                if canne_a_peche == 0:
                    print("La canne à pêche est une simple canne à pêche.")
            elif action in ("prendre canne à pêche", "prendre canne a peche", "prendre canne à peche", "prendre canne a pêche", "prendre canne"):
                print("Vous avez maintenant une canne à pêche dans votre inventaire.\n")
                canne_a_peche = 1
                description["canne"] = "Un bout de bois avec une ficelle et un hameçon. Parfait pour taquiner de la truite.\n"
                description["canne à pêche"] = "Un bout de bois avec une ficelle et un hameçon. Parfait pour taquiner de la truite.\n"
                description["canne a peche"] = "Un bout de bois avec une ficelle et un hameçon. Parfait pour taquiner de la truite.\n"
                description["canne à peche"] = "Un bout de bois avec une ficelle et un hameçon. Parfait pour taquiner de la truite.\n"
                description["canne a pêche"] = "Un bout de bois avec une ficelle et un hameçon. Parfait pour taquiner de la truite.\n"
            elif action == "examiner":
                if canne_a_peche == 0:
                    print("Vous êtes debout dans une petite hutte.\nIl y a une canne à pêche ici.\n")
                if canne_a_peche == 1:
                    print("Vous êtes debout dans une petite hutte.\n")
            elif action == ("sortie"):
                print("Les sorties sont:\nsortir hutte\n")
            elif action in ("sortir hutte", "nord"):
                lieu = "jardin"
            elif action == "aide":
                help()
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else: 
                print("Commande inconnue\n")

    if lieu == "jardin":

        print("Vous êtes dans les jardins royaux, la végétation est luxuriante.\nIl y a un rosier. Vous apercevez aussi une hutte.\n")
        while lieu == "jardin":
            action = input()
            if action in ("cueillir rose", "prendre rose"):
                rose += 1
                print("Vous avez maintenant", rose,"rose dans votre inventaire.\n")

                description["rose"] = "une fleur rose sentant bon.\n"
            elif action == ("sentir rose"):
                print ("Cela sent bon.")
            elif action == ("examiner rosier"):
                print("Il y a une très jolie rose dessus")
            elif action == "examiner":
                print("Vous êtes dans les jardins royaux, leur végétation est luxuriante.\nIl y a un rosier. Vous apercevez aussi une hutte.\n")
            elif action in ("allumer rosier avec torche", "utiliser torche avec rosier"):
                print("Vous n'oseriez pas brûler les rosiers royaux.\n")
            elif action == "sortie":
                print("Les sorties sont:\nest\nouest\nentrer hutte\n")
            elif action == ("est"):
                lieu = "étang"
            elif action == ("ouest"):
                lieu = "sentier"
            elif action == ("entrer hutte"):
                lieu = "hutte"
            elif action == "aide":
                help()
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else:
                print("Commande inconnue\n")

    if lieu == "étang":
        print("Vous arrivez sur la rive d'un étang\n")
        while lieu == "étang":
            action = input()
            if action ==("sortie"):
                print("Les sorties sont:\nouest")
            elif action ==("examiner étang"):
                if poisson == 0:
                    print("Il y a des poissons qui nagent dans l'étang.\n")
                if poisson == 1:
                    print("Il n'y a plus de poisson, c'est juste de l'eau.\n")
            elif action in ("utiliser canne à pêche", "pêcher", "pecher", "utiliser canne a pêche", "utiliser canne a peche", "utiliser canne à peche", "utiliser canne"):
                if canne_a_peche == 1:
                    if poisson == 0:
                        print("Vous réussissez à attraper un poisson.\nVous avez maintenant un poisson dans votre inventaire.\n")
                        poisson = 1
                        description["poisson"] = "Un poisson fraichement pêché, cru. Il s'appelle probablement Steve.\n"
                    elif poisson == 1:
                        print("Vous avez pêché le seul poisson de l'étang, il n'y en a plus\n")
                else:
                    print("Vous n'avez pas de canne à pêche...\n")
            elif action ==("manger poisson"):
                print("Le poisson ne peut pas être mangé cru...\n")
            elif action == "examiner":
                print("Vous êtes sur la rive d'un étang.\n")
            elif action ==("ouest"):
                lieu = "jardin"
            elif action == "aide":
                help()
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else:
                print("Commande inconnue\n")

    if lieu == "sentier":
        print("Vous marchez le long d'un sentier sinueux qui serpente à travers les collines.\nIl y a un très grand z'arbre.\n")
        while lieu == "sentier":
            action = input()
            if action == "examiner":
                print("Vous marchez le long d'un sentier sinueux qui serpente à travers les collines.\nIl y a un très grand z'arbre.\n")
            elif action ==("sortie"):
                print("Les sorties sont:\nest\nnord\nmonter arbre\n")
            elif action ==("est"):
                lieu = "jardin"
                
            elif action ==("nord"):
                lieu = "pont_levis"
                
            elif action in ("monter très grand z'arbre", "monter arbre", "monter z'arbre\n"):
                lieu = "cime_arbre"
                
            elif action == "aide":
                help()
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else:
                print("Commande inconnue\n")
            
    if lieu =="cime_arbre":
        if branche == 0:
            print("Vous arrivez en haut du très grand z'arbre.\nIl y a une branche morte qui semble bien solide.\n")
        if branche == 1:
            print("Vous arrivez en haut du très grand z'arbre.\n")
        while lieu == "cime_arbre":
            action = input ()
            if action ==("sortie"):
                print("Les sorties sont:\n descendre")
            elif action ==("sauter"):
                print("Vous tombez du haut du très grand z'arbre et mourez.\n")
                
                exit() 
                print("GAME OVER")
            elif action in ("grimper branche morte", "monter branche", "monter branche morte"):
                print("La branche se casse sous vos pieds, vous tombez du z'arbre et mourez.\n")
                
                exit() 
                print("GAME OVER")
            elif action in("prendre branche", "prendre branche morte"):
                print("Vous récupérez la branche.\nVous avez maintenant une branche dans votre inventaire.\n")
                branche = 1
                description["branche"] = "Une branche morte venant du très grand z'arbre.\n"
            elif action == "examiner":
                if branche == 0:
                    print("Vous arrivez en haut du très grand z'arbre.\nIl y a une branche morte qui semble bien solide.")
                if branche == 1:
                    print("Vous arrivez en haut du très grand z'arbre.")
            elif action == ("descendre"):
                lieu = "sentier"
                
            elif action == "aide":
                help()  
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else:
                print("Commande inconnue\n")

    if lieu == "pont_levis":
        if poisson_troll == 1:
            print("Vous vous trouvez face au pont levis qui mène à... Château Aventure.\nLe troll mange le poisson.\n")
        elif poisson_troll == 0:
            print("Vous vous trouvez face au pont levis qui mène à... Château Aventure.\nUn troll peu amène vous barre le passage.\n")
        while lieu == "pont_levis":
            action = input()
            if action == ("sortie"):
                print("Les sorties sont:\nsud")
                if poisson_troll == 1:
                    print("nord")
            elif action == ("examiner troll"):
                print("Le troll est tès grand, vert, fort et semble bougon.")
            elif action in ("attaquer troll", "taper troll", "frapper troll"):
                print("Le troll est beaucoup plus fort que vous et vous réduit en bouillie.\n")
                exit() 
                print("GAME OVER")
            elif action in ("donner poisson troll", "donner poisson a troll", "donner poisson à troll"):
                if poisson == 1:
                    print("Le troll accepte le poisson avec enthousiasme et le dévore en ne vous prêtant plus attention.\n")
                    poisson_troll = 1
                else:
                    print("Vous n'avez pas de poisson")
            elif action == "examiner":
                if poisson_troll == 1:
                    print("Vous vous trouvez face au pont levis qui mène à... Château Aventure.\nLe troll mange le poisson.\n")
                elif poisson_troll == 0:
                    print("Vous vous trouvez face au pont levis qui mène à... Château Aventure.\nUn troll peu amène vous barre le passage.\n")
            elif action ==("sud"):
                lieu = "sentier"
            elif action == "nord":
                if poisson_troll == 1:
                    lieu = "cour"
                if poisson_troll == 0:
                    print("Le troll garde l'entrée")
            elif action == "aide":
                help()
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else:
                print ("Commande inconnue\n")

    if lieu == "cour":
        if couronne_tête == 0:
            if garde_KO == 0:
                print("Vous êtes dans la cour de Château Aventure.\nUn garde bloque le passage vers le nord.\n")
            else:
                print("Vous êtes dans la cour de Château Aventure.\nLe garde est toujours assommé.\n")
        elif couronne_tête == 1:
            if garde_KO == 0:
                print("Le garde se prosterne devant le monarque.")
            elif garde_KO == 1:
                print("Le garde se réveille et s'agenouille devant son nouveau roi.\n")
                garde_KO = 0
                
        while lieu == "cour":
            action = input()
            if action == "examiner garde":
                if garde_KO == 1:
                    if clé == 1:
                        print("Le garde est armé d'une épée, mais est assommé.\n")
                    else:
                        print("Le garde est armé d'une épée, il a une clé attachée à la ceinture, mais est assommé.\n")
                else:
                    if clé == 1:
                        print("Le garde est armé d'une épée.")
                    else:
                        print("Le garde est armé d'une épée, il a une clé attachée à la ceinture.")
            elif action in ("frapper garde avec branche", "assommer garde avec branche", "assommer garde avec branche morte", "frapper garde avec branche morte"):
                if branche == 1:
                    print("Vous vous glissez sournoisement derrière le garde et l'assommez à l'aide de la branche morte.\nCelle-ci se brise et n'est plus utilisable.\n")
                    branche = 0
                    branche_cassee = 1
                    garde_KO = 1
                    description["branche"] = "La branche morte venant du très grand z'arbre, mais brisée.\n"
                else:
                    print("Vous n'avez pas de branche.\n")
            elif action == "prendre clé":
                if garde_KO == 0:
                    print("Le garde dégaine son épée et vous tue.\n")
                    exit()
                else:
                    print("Vous récupérez la clé attachée à la ceinture du garde.\nVous avez une clé dans votre inventaire.\n")
                    clé = 1
                    description["clé"] = "C'est une clef, ressemblant à toutes les autres clé. (Ha, la réforme de l'orthographe)\n"
                    description["clef"] = "C'est une clé, ressemblant à toutes les autres clef. (Ha, la réforme de l'orthographe)\n"
            elif action in ("demander à passer", "demander a passer", "demander pour passer"):
                if couronne_tête == 0:
                    print("Le garde répond:\n'Je ne laisse pas passer les gueux comme vous !'\n")
            elif action == "prendre épée":
                if garde_KO == 0:
                    print("Le garde la tient, vous ne tenteriez pas de la lui voler.\n")
                else:
                    print("Vous ne pouvez pas prendre l'épée, vous risqueriez de vous blesser.\n")
            elif action == "sortie":
                print("Sorties disponibles :")
                print("sud")
                if catatorche == 0:
                    print("descendre")
                else:
                    print("descendre (catacombes)")
                print("monter")
                if couronne_tête == 1 or garde_KO == 1:
                    print("nord")
            elif action == "sud":
                lieu = "pont_levis"
            elif action == "monter":
                if clé_porte == 0:
                    lieu = "escalier_haut"
                else:
                    lieu = "tour"
            elif action == "descendre":
                if catatorche == 0:
                    lieu = "escalier_bas"
                else:
                    lieu = "catacombe"
            elif action == "nord":
                if couronne_tête == 1 or garde_KO == 1:
                    lieu = "banquet"
                else:
                    print("Le garde bloque le passage vers le nord.\n")
            elif action == "aide":
                help()
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else:
                print("Commande inconnue\n")

                
    if lieu == "escalier_haut":
        print("Vous montez l'escalier de la tour.\nVous vous trouvez face à une porte qui est fermée à clé.\n")
        while lieu == "escalier_haut":
            action = input()
            if action == ("ouvrir porte"):
                if clé == 1:            
                    print("Grâce à la clé, vous ouvrez la porte\n")
                    clé_porte = 1
                    choix = input("Voulez-vous entrer ? (o/n)\n")
                    if choix == "o":
                        lieu = "tour"
                    elif choix == "n":
                        print("D'accord")
                    else:
                        print("Tu dois taper o (pour entrer dans la tour) ou n( pour ne pas entrer dans la tour)\nTape entrer, pour entrer.\n")
                else:           
                    print("On t'a dit que la porte était fermée à clé...\n")
            elif action == ("sortie"):
                print ("descendre")
                if clé_porte == 1:
                    print("entrer")
            elif action == ("descendre"):
                lieu = "cour"
            elif action == ("entrer"):
                lieu = "tour"
            elif action == "aide":
                help()
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else:
                print ("Commande inconnue\n")
                
    if lieu == "tour":
        print("Vous êtes dans la tour.\nLa princesse se trouve là.\n")
        while lieu == "tour":
            action = input()
            if rose_princesse == 0:
                if action == "examiner princesse":
                    print("La princesse est magnifique, mais semble triste.\n")
                elif action == "embrasser princesse":
                    print("La princesse vous gifle et dit:\n<<Je ne suis pas ce genre de fille !>>\n")
                elif action == "donner rose à princesse":
                    if rose > 0:
                        print("La princesse est agréablement surprise, et sait désormais qu'elle peut vous faire confiance et se confier à vous.\n")
                        rose_princesse = 1
                    if rose == 0:
                        print("Vous n'avez pas de rose...\n")
                elif action == ("sortie"):
                    print ("descendre")
                elif action == "aide":
                    help()
                elif action in ("crédits", "credits"):
                    credits()
                elif action == "inventaire":
                    inventaire()
                else:
                    print ("La princesse n'est pas d'humeur à parler.\n")
            elif rose_princesse == 1:
                if action == "embrasser princesse":
                    if couronne_tête == 0:
                        print("La princesse vous repousse et dit:\nPas en dehors du mariage !\n")
                    elif couronne_tête == 1:
                        print("La princesse vous repousse et dit:\nPas avant que nous soyons mariés !\n")
                elif action in ("donner couronne à princesse", "donner couronne a princesse"):
                    if couronne == 1:
                        print ("La princesse s'exclame:\n<<La couronne de mon père !\nVous avez apaisé son esprit, et vous pouvez à présent lui succéder.>>\nLa princesse pose la couronne sur votre tête.\n")
                        couronne_tête = 1
                    elif couronne == 0:
                        print("Vous n'avez pas de couronne\n")
                elif action == ("parler princesse de trône"):
                    print ("Elle dit:\n<<Seul le roi peut y prendre place.>>\n")
                elif action == "parler princesse de couronne":
                    print("Elle dit:\n<<Seul le digne héritier peut la porter.>>\n")
                elif action == ("demander princesse en mariage"):
                    if couronne_tête == 0:
                        print ("<<Je ne me marierai qu'avec quelqu'un de sang royal.>>\n")
                    if couronne_tête == 1:
                        print("La princesse se réjouit:\n<<Oui ! Marions-nous !>>\n")
                elif action == ("sortie"):
                    print ("descendre\n")
                elif action == ("descendre"):
                    if clé_porte == 0:
                        lieu = "escalier_haut"
                    if clé_porte == 1:
                        lieu = "cour"
                elif action == "aide":
                    help()
                    print ("\n- demander ... en mariage\n- embrasser...\n- parler ... de trône\n")
                elif action in ("crédits", "credits"):
                    credits()
                elif action == "inventaire":
                    inventaire()
                elif action.startswith("examiner "):
                    examiner(action[len("examiner "):])
                else:
                    print ("Commande inconnue\n")

    if lieu == "banquet":
        if couronne_tête == 1:
            print("Vous arrivez dans une grande salle de banquet.\nCette pièce se révèle pleine de fêtards qui célèbrent le nouveau propriétaire de Château Aventure.\n")
        if couronne_tête == 0:
            if bougie == 0:
                print("Vous arrivez dans une grande salle de banquet.\nIl y a une étrange bougie sur la table.\n")
            if bougie == 1:
                print("Vous arrivez dans une grande salle de banquet.\n")
        while lieu == "banquet":
            action = input()
            if action == "examiner bougie":
                print("La bougie est recouverte de runes ésotériques, elle est éteinte.\n")
            elif action == "prendre bougie":
                print("Vous avez maintenant la bougie dans votre inventaire.\n")
                bougie = 1
                description["bougie"] = "C'est une bougie, recouverte de rune ésotériques. On dirait un exorcisme.\n"
            elif action in ("lire runes", "examiner runes"):
                print("Il semblerait que soit une sorte d'exorcisme.\n")
            elif action == "allumer bougie avec torche":
                print("Pas ici, ce lieu n'est pas approprié pour un exorcisme.")
            elif action == "sortie":
                print("sud\nnord\n")
            elif action == ("nord"):
                lieu = "salle_trone"
            elif action == ("sud"):
                    lieu = "cour"
            elif action == "aide":
                help()
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else:
                print("Commande inconnue\n")
        
                
    if lieu == "escalier_bas":
        print("Vous descendez les marches menant aux catacombes.\nIl fait trop noir pour continuer.\n")
        while lieu == "escalier_bas":  
            action = input()
            if action == "utiliser torche":
                print ("Vous pouvez maintenant y voir plus clair.\n")
                catatorche = 1
            elif action == "sortie":
                print("monter\n")
                if catatorche == 1:
                    print("descendre\n")
            elif action == "monter":
                lieu = "cour"
            elif action == "descendre":
                if catatorche == 1:
                    lieu = "catacombe"
                elif catatorche == 0:
                    print("Il fait trop sombre pour descendre\n")
            elif action == "examiner":
                print("Vous êtes dans les escaliers menant aux catacombes")
            elif action == "aide":
                help()
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else:
                print ("Commande inconnue\n")

    if lieu == "catacombe":
        if fantome == 1:
            print("Vous êtes dans les catacombes.\nIl y a un effrayant fantôme. Il porte une couronne.\n")
        if fantome == 0:
            if couronne_terre == 0:
                  print("Vous êtes dans les catacombes.\n")
            if couronne_terre == 1:
                  print("Vous êtes dans les catacombes.\nIl y une couronne par terre.\n")
        while lieu == "catacombe":
            action = input()
            if action == ("allumer bougie avec torche"):
                if bougie == 1:
                    if fantome == 1:
                        print ("La bougie dégage une fumée étrange et âcre.\nLe fantôme s'enfuit et disparaît en laissant tomber la couronne.\n")
                        fantome = 0
                        couronne_terre = 1
                    if fantome == 0:
                        print("Elle est déjà allumée.\n")
                    couronne_terre = 1
                if bougie == 0:
                    print("Vous n'avez pas de bougie...\n")
            if action == ("prendre couronne"):
                if fantome == 1:
                    print ("Le fantôme l'a sur la tête.")
                if fantome == 0:
                    print("Vous rammassez la couronne tombée au sol.\nVous avez maintenant une couronne dans votre inventaire\n")
                    description["couronne"] = "La couronne du roi de Château Aventure.\n"
                    couronne = 1
                    couronne_terre = 0
            elif action == ("porter couronne"):
                if fantome == 1:
                    print ("Le fantôme l'a sur la tête.")
                if fantome == 0:
                    print("Vous n'oseriez quand même pas la porter sans être son propriétaire légitime !\n")
            elif action == "examiner":
                if fantome == 1:
                    print("Vous êtes dans les catacombes.\nIl y a un effrayant fantôme. Il porte une couronne.\n")
                if fantome == 0:
                    if couronne_terre == 0:
                          print("Vous êtes dans les catacombes.\n")
                    if couronne_terre == 1:
                          print("Vous êtes dans les catacombes.\nIl y une couronne par terre.\n")
            elif action == "sortie":
                print("monter")
            elif action == "monter":
                lieu = "cour"
            elif action == "aide":
                help()
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else:
                print ("Commande inconnue\n")

    if lieu == "salle_trone":
        print("C'est la salle du trône de Château Aventure !\nIl y a un trône d'or richement orné.\n")
        while lieu == "salle_trone":
            action = input()
            if action in ("asseoir sur trône", "s'asseoir sur trône", "asseoir sur trone", "s'asseoir sur trone"):
                if couronne_tête == 0:
                    print("Vous n'oseriez pas vous asseoir sur ce magnifique trône !\n")
                if couronne_tête == 1:
                    print("Longue vie au roi de Château Aventure.\nFIN!")
                    input("Appuyez sur Entrée pour quitter") 
                    exit() 
                    print("Bien Joué")
            elif action =="examiner":
                print("C'est la salle du trône de Château Aventure !\nIl y a un trône d'or richement orné.\n")
            elif action == "sortie":
                print("sud")
            elif action == "sud":
                lieu = "banquet"
            elif action == "aide":
                help()
            elif action in ("crédits", "credits"):
                credits()
            elif action == "inventaire":
                inventaire()
            elif action.startswith("examiner "):
                examiner(action[len("examiner "):])
            else:
                print ("Commande inconnue\n")
