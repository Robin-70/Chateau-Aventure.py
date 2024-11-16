lieu = "hutte"
action = ()
canne_a_peche = "non"
rose = "non"
poisson = "non"
branche = "non"
branche_cassée = "non"
clé = "non"
couronne = "non"
bougie = "non"
garde_KO = "non"
poisson_troll = "non"
rose_princesse ="non"
couronne_tête = "non"
clé_porte = "non"
choix = ()
catatorche ="non"
fantome= "oui"
couronne_terre:"non"
while True:
    if lieu == "hutte":
        if canne_a_peche == "non":
            print("Vous êtes debout dans une petite hutte.\nIl ya une canne à pêche ici.")
        if canne_a_peche == "oui":
            print("Vous êtes debout dans une petite hutte.")
        while lieu == "hutte":
            action = input ()
            if action == ("examiner canne à pêche"):
                print("La canne à pêche est une simple canne à pêche.")
            elif action == ("prendre canne à pêche"):
                print("Vous avez maintenant une canne à pêche dans votre inventaire.")
                canne_a_peche = "oui"
            elif action == "examiner":
                if canne_a_peche == "non":
                    print("Vous êtes debout dans une petite hutte.\nIl ya une canne à pêche ici.")
                if canne_a_peche == "oui":
                    print("Vous êtes debout dans une petite hutte.")
            elif action == ("sortie"):
                print("Les sorties sont:\n sortir hutte")
            elif action == ("sortir hutte"):
                lieu = "jardin"
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else: 
                print("Commande inconnue")

    if lieu == "jardin":
        print("Vous êtes dans les jardins royaux, la végétation est luxuriante.\nIl y a un rosier. Vous apercevez aussi une hutte.")
        while lieu == "jardin":
            action = input()
            if action == ("cueillir rose"):
                print("Vous avez maintenant une rose dans votre inventaire.")
                rose = "oui"
            elif action == ("sentir rose"):
                print ("Cela sent bon.")
            elif action == "examiner":
                print("Vous êtes dans les jardins royaux, leur végétation est luxuriante.\nIl y a un rosier. Vous apercevez aussi une hutte.")
            elif action == "sortie":
                print("Les sorties sont:\nest\nouest\nentrer hutte")
            elif action == ("est"):
                lieu = "étang"
            elif action == ("ouest"):
                lieu = "sentier"
            elif action == ("entrer hutte"):
                lieu = "hutte"
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- sentir\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else:
                print("Commande inconnue")

    if lieu == "étang":
        print("Vous arrivez sur la rive d'un étang")
        while lieu == "étang":
            action = input()
            if action ==("sortie"):
                print("Les sorties sont:\nouest")
            elif action ==("examiner étang"):
                print("Il y a des poissons qui nagent dans l'étang.")
            elif action ==("utiliser canne à pêche"):
                if canne_a_peche == "oui":
                    print("Vous réussissez à attraper un poisson.\nVous avez maintenant un poisson dans votre inventaire.")
                    poison = "oui"
                else:
                    print("Vous n'avez pas de canne à pêche...")
            elif action ==("manger poisson"):
                print("Le poisson ne peut pas être mangé cru...")
            elif action == "examiner":
                print("Vous êtes sur la rive d'un étang.")
            elif action ==("ouest"):
                lieu = "jardin"
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else:
                print("Commande inconnue")

    if lieu == "sentier":
        print("Vous marchez le long d'un sentier sinueux qui serpente à travers les collines.\nIl y a un très grand z'arbre.")
        while lieu == "sentier":
            action = input()
            if action == "examiner":
                print("Vous marchez le long d'un sentier sinueux qui serpente à travers les collines.\nIl y a un très grand z'arbre.")
            elif action ==("sortie"):
                print("Les sorties sont:\nest\nnord\nmonter très grand z'arbre")
            elif action ==("est"):
                lieu = "jardin"
            elif action ==("nord"):
                lieu = "pont_levis"
            elif action ==("monter très grand z'arbre"):
                lieu = "cime_arbre"
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else:
                print("Commande inconnue")
            
    if lieu =="cime_arbre":
        if branche == "non":
            print("Vous arrivez en haut du très grand z'arbre.\nIl y a une branche morte qui semble bien solide.")
        if branche == "oui":
            print("Vous arrivez en haut du très grand z'arbre.")
        while lieu == "cime_arbre":
            action = input ()
            if action ==("sortie"):
                print("Les sorties sont:\n descendre")
            elif action ==("sauter"):
                print("Vous tombez du haut du très grand z'arbre et mourez.")
                print(exit) 
                exit() 
                print(test)
            elif action ==("grimper branche morte"):
                print("La branche se casse sous vos pieds, vous tombez du z'arbre et mourez")
                print(exit) 
                exit() 
                print(test)
            elif action ==("prendre branche"):
                print("Vous récupérez la branche.\nVous avez maintenant une branche dans votre inventaire.")
                branche = "oui"
            elif action ==("prendre branche morte"):
                print("Vous récupérez la branche.\nVous avez maintenant une branche dans votre inventaire.")
                branche = "oui"
            elif action == "examiner":
                if branche == "non":
                    print("Vous arrivez en haut du très grand z'arbre.\nIl y a une branche morte qui semble bien solide.")
                if branche == "oui":
                    print("Vous arrivez en haut du très grand z'arbre.")
            elif action == ("descendre"):
                lieu = "sentier"
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- grimper\n - crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else:
                print("Commande inconnue")

    if lieu == "pont_levis":
        if poisson_troll == "oui":
            print("Vous vous trouvez face au pont levis qui mène à... Château Aventure.\nLe troll mange le poisson.")
        elif poisson_troll == "non":
            print("Vous vous trouvez face au pont levis qui mène à... Château Aventure.\nUn troll peu amène vous barre le passage.")
        while lieu == "pont_levis":
            action = input()
            if action == ("sortie"):
                print("Les sorties sont:\nsud")
                if poisson_troll == "oui":
                    print("nord")
            elif action == ("examiner troll"):
                print("Le troll est tès grand, vert, fort et semble bougon.")
            elif action == ("attaquer troll"):
                print("Le troll est beaucoup plus fort que vous et vous réduit en bouillie.")
                print(exit) 
                exit() 
                print(test)
            elif action == ("taper troll"):
                print("Le troll est beaucoup plus fort que vous et vous réduit en bouillie.")
                print(exit) 
                exit() 
                print(test)
            elif action == ("frapper troll"):
                print("Le troll est beaucoup plus fort que vous et vous réduit en bouillie.")
                print(exit) 
                exit() 
                print(test)
            elif action == ("donner poisson troll"):
                if poisson == "oui":
                    print("Le troll accepte le poisson avec enthousiasme et le dévore en ne vous prêtant plus attention.")
                    poisson_troll = "oui"
                else:
                    print("Vous n'avez pas de poisson")
            elif action == ("donner poisson à troll"):
                if poisson == "oui":
                    print("Le troll accepte le poisson avec enthousiasme et le dévore en ne vous prêtant plus attention.")
                    poisson_troll = "oui"
                else:
                    print("Vous n'avez pas de poisson")
            elif action == "examiner":
                if poisson_troll == "oui":
                    print("Vous vous trouvez face au pont levis qui mène à... Château Aventure.\nLe troll mange le poisson.")
                elif poisson_troll == "non":
                    print("Vous vous trouvez face au pont levis qui mène à... Château Aventure.\nUn troll peu amène vous barre le passage.")
            elif action ==("sud"):
                lieu = "sentier"
            elif action == "nord":
                if poisson_troll == "oui":
                    lieu = "cour"
                if poisson_troll == "non":
                    print("Le troll garde l'entrée")
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- donner ... à ...\n- attaquer\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else:
                print ("Commande inconnue")

    if lieu == "cour":
        if couronne_tête == "non":
            if garde_KO == "non":
                print("Vous êtes dans la cour de Château Aventure.\nUn garde bloque le passage vers le nord.")
            else:
                print("Vous êtes dans la cour de Château Aventure.\nLe garde est toujours assommé.")
        elif couronne_tête == "oui":
            if garde_KO == "non":
                 print("Le garde se prosterne devant le monarque.")
            if garde_KO == "oui":
                print("Le garde se réveille et s'agenouille devant son nouveau roi.")
                harde_KO = "non"
        while lieu == "cour":
            action = input()
            if action ==("examiner garde"):
                if garde_KO == "oui":
                    if clé  == "oui":
                        print("Le garde est armé d'une épée, mais est assommé.")
                    if clé  == "non":
                        print("Le garde est armé d'une épée, il a une clé attaché à la ceinture, mais est assommé.")
                if garde_KO == "non":
                    if clé  == "oui":
                        print("Le garde est armé d'une épée.")
                    if clé  == "non":
                        print("Le garde est armé d'une épée, il a une clé attaché à la ceinture.")
            elif action == ("frapper garde avec branche"):
                if branche == "oui":
                    print("Vous vous glissez sournoisement derrière le garde et l'assommez à l'aide de la branche morte.\nCelle-ci se brise et n'est plus utilisable.")
                    branche = "non"
                    branche_cassée = "oui"
                    garde_KO = "oui"
                else:
                    print("Vous n'avez pas de branche.")
            elif action == ("frapper garde avec branche morte"):
                if branche == "oui":
                    print("Vous vous glissez sournoisement derrière le garde et l'assommez à l'aide la branche morte.\nCelle-ci se brise et n'est plus utilisable.")
                    branche = "non"
                    branche_cassée = "oui"
                    garde_KO = "oui"
                else:
                    print("Vous n'avez pas de branche.")
            elif action == ("taper garde avec branche"):
                if branche == "oui":
                    print("Vous vous glissez sournoisement derrière le garde et l'assommez à l'aide la branche morte.\nCelle-ci se brise et n'est plus utilisable.")
                    branche = "non"
                    branche_cassée = "oui"
                    garde_KO = "oui"
                else:
                    print("Vous n'avez pas de branche.")
            elif action == ("taper garde avec branche morte"):
                if branche == "oui":
                    print("Vous vous glissez sournoisement derrière le garde et l'assommez à l'aide la branche morte.\nCelle-ci se brise et n'est plus utilisable.")
                    branche = "non"
                    branche_cassée = "oui"
                    garde_KO = "oui"
                else:
                    print("Vous n'avez pas de branche.")
            elif action == ("assommer garde avec branche"):
                if branche == "oui":
                    print("Vous vous glissez sournoisement derrière le garde et l'assommez à l'aide la branche morte.\nCelle-ci se brise et n'est plus utilisable.")
                    branche = "non"
                    branche_cassée = "oui"
                    garde_KO = "oui"
                else:
                    print("Vous n'avez pas de branche.")
            elif action == ("assommer garde avec branche morte"):
                if branche == "oui":
                    print("Vous vous glissez sournoisement derrière le garde et l'assommez à l'aide la branche morte.\nCelle-ci se brise et n'est plus utilisable.")
                    branche = "non"
                    branche_cassée = "oui"
                    garde_KO = "oui"
                else:
                    print("Vous n'avez pas de branche.")
            elif action == ("prendre clé"):
                if garde_KO == "non":
                    print("Le garde dégaine son épée et vous tue.")
                    print(exit) 
                    exit() 
                    print(test)
                if garde_KO == "oui":
                    print("Vous récupérez la clé attachée à la ceinture du garde.\nVous avez une clé dans votre inventaire.")
                    clé = "oui"
            elif couronne_tête == "non":
                if action == ("Demander à  passer"):
                    print ("Le garde répond:\n 'Je ne laisse pas passer les gueux comme vous !'")
            elif action == ("Prendre épée"):
                print("Vous ne pouvez pas prendre l'épée, vous risqueriez de vous blesser")
            elif action == ("sortie"):
                print("monter\ndescendre\nsud")
                if couronne_tête == "non":
                    if garde_KO == "oui":
                        print("nord")
                if couronne_tête == "oui":
                    print("nord")
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- frapper ... avec ...\n- crédits\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == ("sud"):
                lieu = "pont_levis"
            elif action == ("monter"):
                if clé_porte == "non":
                    lieu = "escalier_haut"
                if clé_porte == "oui":
                    lieu = "tour"
            elif catatorche == "non":
                if action == ("descendre"):
                    lieu = "escalier_bas"
            elif action == ("descendre"):
                    lieu = catacombe
            elif garde_KO == "oui":
                if action == ("nord"):
                    lieu = "banquet"
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else:
                print("Commande inconnue")
                
    if lieu == "escalier_haut":
        print("Vous montez l'escalier de la tour.\nVous vous trouvez face à une porte qui est fermée à clé.")
        while lieu == escalier_haut:
            if action == ("ouvrir porte"):
                if clé == "oui":            
                    print("Grâce à la clé, vous ouvrez la porte")
                    clé_porte = "oui"
                    choix = input("Voulez-vous entrer ? (o/n)")
                    if choix == "o":
                        lieu = "tour"
                    elif choix == "n":
                        print("D'accord")
                    else:
                        print("Tu dois taper o (pour entrer dans la tour) ou n( pour ne pas entrer dans la tour)")
                else:           
                    print("On t'a dit que la porte était fermée à clé...")
            elif action == ("sortie"):
                print ("descendre")
                if clé_porte == "oui":
                    print("entrer")
            elif action == ("descendre"):
                lieu = "cour"
            elif action == ("entrer"):
                lieu = "tour"
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- ouvrir\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else:
                print ("Commande inconnue")
                
    if lieu == "tour":
        print("Vous êtes dans la tour.\nLa princesse se trouve là.")
        while lieu == "tour":
            action = input()
            if rose_princesse == "non":
                if action == "examiner princesse":
                    print("La princesse est magnifique, mais semble triste.")
                elif action == "embrasser princesse":
                    print("La princesse vous gifle et dit:\n<<Je ne suis pas ce genre de fille !>>")
                elif action == "donner rose à princesse":
                    if rose == "oui":
                        print("La princesse est agréablement surprise, et sait désormais qu'elle peut vous faire confiance et se confier à vous.")
                        rose_princesse = "oui"
                    if rose == "non":
                        print("Vous n'avez pas de rose...")
                elif action == ("sortie"):
                    print ("descendre")
                elif action == "aide":
                    print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- donner ... à ...\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
                elif action == "crédits":
                    print("Antoine au codage et son père pour la relecture")
                elif action == "inventaire":
                    print ("Torche allumée")
                    if canne_a_peche == "oui":
                        print ("Canne à pêche")
                    if rose == "oui":
                        print ("Rose")
                    if poisson == "oui":
                        print("Poisson cru")
                    if branche == "oui":
                        print("Branche morte")
                    if branche_cassée == "oui":
                        print("Branche cassée")
                    if couronne == "oui":
                        print("Couronne")
                    if bougie == "oui":
                        print ("Bougie")
                    if clé == "oui":
                        print ("Clé")
                else:
                    print ("La princesse n'est pas d'humeur à parler.")
            elif rose_princesse == "oui":
                if action == "embrasser princesse":
                    if couronne_tête == "non":
                        print("La princesse vous repousse et dit:\nPas en dehors du mariage !")
                    elif couronne_tête == "oui":
                        print("La princesse vous repousse et dit:\nPas avant que nous soyons mariés !")
                elif action == ("donner couronne à princesse"):
                    if couronne == "oui":
                        print ("La princesse s'exclame:\n<<La couronne de mon père !\nVous avez apaisé son esprit, et vous pouvez à présent lui succéder.>>\nLa princesse pose la couronne sur votre tête.")
                        couronne_tête = "oui"
                    elif couronne == "non":
                        print("Vous n'avez pas de couronne")
                elif action == ("parler princesse de trône"):
                    print ("Elle dit:\n<<Seul le roi peut y prendre place.>>")
                elif action == "parler princesse de couronne":
                    print("Elle dit:\n<<Seul le digne héritier peut la porter.>>")
                elif action == ("demander princesse en mariage"):
                    if couronne_tête == "non":
                        print ("<<Je ne me marierai qu'avec quelqu'un de sang royal.>>")
                    if courrone_tête == "oui":
                        print("La princesse se réjouit:\n<<Oui ! Marions-nous !>>")
                elif action == ("sortie"):
                    print ("descendre")
                elif action == ("descendre"):
                    lieu = "escalier_haut"
                elif action == "aide":
                    print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\ndemander ... en mariage\n- donner ... à ...\n- embrasser\n- parler ... de trône\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
                elif action == "crédits":
                    print("Antoine au codage et son père pour la relecture")
                elif action == "inventaire":
                    print ("Torche allumée")
                    if canne_a_peche == "oui":
                        print ("Canne à pêche")
                    if rose == "oui":
                        print ("Rose")
                    if poisson == "oui":
                        print("Poisson cru")
                    if branche == "oui":
                        print("Branche morte")
                    if branche_cassée == "oui":
                        print("Branche cassée")
                    if couronne == "oui":
                        print("Couronne")
                    if bougie == "oui":
                        print ("Bougie")
                    if clé == "oui":
                        print ("Clé")
                else:
                    print ("Commande inconnue")


    if lieu == "banquet":
        if couronne_tête == "oui":
            print("Vous arrivez dans une grande salle de banquet.\nCette pièce se révèle pleine de fêtards qui célèbrent le nouveau propriétaire de Château Aventure.")
        if couronne_tête == "non":
            if bougie == "non":
                print("Vous arrivez dans une grande salle de banquet.\nIly a une étrange bougie sur la table.")
            if bougie == "oui":
                print("Vous arrivez dans une grande salle de banquet.")
        while lieu == "banquet":
            action = input()
            if action == "examiner bougie":
                print("La bougie est recouverte de runes ésotériques, elle est éteinte.")
            elif action == "prendre bougie":
                print("Vous avez maintenant la bougie dans votre inventaire.")
                bougie = "oui"
            elif action == "lire runes":
                print("Il semblerait que soit une sorte d'exorcisme.")
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- crédits\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == ("nord"):
                lieu = "salle_trone"
            elif action == ("sud"):
                    lieu = "cour"
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else:
                print("Commande inconnue")
        
                
    if lieu == "escalier_bas":
        print("Vous descendez les marches menant aux catacombes.\nIl fait trop noir pour continuer.")
        while lieu == "escalier_bas":
            action = input()
            if action == "utiliser torche":
                print ("Vous pouvez maintenant y voir plus clair.")
                catatorche = "oui"
            elif action == "sortie":
                print("monter")
                if catatorche == "oui":
                    print("descendre")
            elif action == "monter":
                lieu = "cour"
            elif catatorche == "oui":
                lieu = catacombe
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else:
                print ("Commande inconnue")

    if lieu == "catacombe":
        if fantome == "oui":
            print("Vous êtes dans les catacombes.\nIl y a un effrayant fantôme. Il porte une couronne.")
        if fantome == "non":
            if couronne_terre == "non":
                  print("Vous êtes dans les catacombes.")
            if couronne_terre == "oui":
                  print("Vous êtes dans les catacombes.\nIl y une couronne par terre.")
        while lieu == "catacombe":
            action = input
            if action == ("allumer bougie avec torche"):
                if bougie == "oui":
                    print ("La bougie dégage une fumée étrange et âcre.\nLe fantôme s'enfuit et disparaît en laissant tomber la couronne.")
                    couronne_terre = "oui"
                if bougie == "non":
                    print("Vous n'avez pas de bougie...")
            if action == ("prendre couronne"):
                if fantome == "oui":
                    print ("Le fantôme l'a sur la tête.")
                if fantome == "non":
                    print("Vous rammassez la couronne tombée au sol.\nVous avez maintenant une couronne dans votre inventaire")
            elif action == ("porter couronne"):
                if fantome == "oui":
                    print ("Le fantôme l'a sur la tête.")
                if fantome == "non":
                    print("Vous n'oseriez quand même pas la porter sans être son propriétaire légitime !")
            elif action == "sortie":
                print("monter")
            elif action == "monter":
                lieu = "cour"
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- allumer ... avec torche\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else:
                print ("Commande inconnue")

    if lieu == "salle_trone":
        print("C'est la salle du trône de Châtaau Aventure !\nIl y a un trône d'or richement orné.")
        while lieu == "banquet":
            action = input()
            if action == "asseoir sur trône":
                if couronne_tête == "non":
                    print("Vous n'oseriez pas vous asseoir sur ce magnifique trône !")
                if couronne_tête == "oui":
                    print("Longue vie au roi de Château Aventure.\nFIN!")
                    input("Appuyez sur Entrée pour quitter")
                    print(exit) 
                    exit() 
                    print(test)
            elif action == "aide":
                print ("Les principales commandes sont:\n- examiner\n- prendre\n- utiliser\n- asseoir sur trône\n- crédits\n- inventaire\n- sortie, pour avoir les sorties du lieu (recopier complètement le nom)")
            elif action == "crédits":
                print("Antoine au codage et son père pour la relecture")
            elif action == "inventaire":
                print ("Torche allumée")
                if canne_a_peche == "oui":
                    print ("Canne à pêche")
                if rose == "oui":
                    print ("Rose")
                if poisson == "oui":
                    print("Poisson cru")
                if branche == "oui":
                    print("Branche morte")
                if branche_cassée == "oui":
                    print("Branche cassée")
                if couronne == "oui":
                    print("Couronne")
                if bougie == "oui":
                    print ("Bougie")
                if clé == "oui":
                    print ("Clé")
            else:
                print ("Commande inconnue")