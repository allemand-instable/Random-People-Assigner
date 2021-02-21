"""
TIRAGE
"""


#   Random FUNCTIONS
from random import randint


from RandomPeopleAssigner.tools.csv import *
from RandomPeopleAssigner.tools.mail import *



def tirageAuSort(L):

    # Liste des tirages au sort
    M=[]

    #   Liste qui va répertorier les éléments qui ont déjà été tirés et assignés
    added = []


    for k in range(len(L)):

        #   DEBUG PRINT
        """
        print("=== personnes ajoutées ===\n")
        """


        personne1 = k

        personne2 = personne1


        # on choisit un nombre aléatoire qui ne correspond ni à la personne elle même, ni à une personne qui a déjà été assignée à quelqu'un d'autre
        while personne1 == personne2 or personne2 in added :

            #   DEBUG PRINT
            """
            print("k = ", k)
            """



            # Si on n'est pas à la dernière ittération
            if k < len(L) - 1 :
                # pas d'inquiétude, on pioche dans l'ensemble des personnes
                personne2 = randint(0, len(L)-1)

            # si on n'est à la dernière ittération
            else :
                # si le dernier nombre qui reste n'est pas celle de la personne elle même
                # ie : si la dernière ittération n'est pas dans la liste added
                # note : la dernière ittération est bien Len(L) - 1
                if len(L) - 1 in added :
                    personne2 = randint(0, len(L)-2)


                # si le dernier nombre restant est la personne même
                # ==> pas de chance ! on procède à un remplacement aléatoire
                else :
                    #   DEBUG
                    """
                    print(Fore.YELLOW + "\n\n WARNING :\n boucle de récupération en cours !" + Fore.WHITE)
                    os.system("pause")
                    """

                    # on sélectionne un remplaçant aléatoirement dans la liste M
                    numero_remplacant = randint(0, len(M)-1)

                    # celle qui va être échangée est la personne associée au binome de la case numero_remplacant
                    replace = M[numero_remplacant][1]
                    # la personne selectionnee pour changer son binome
                    personne_selectionnee = M[numero_remplacant][0]
                    # le pauvre qui n'a pas pu etre placé
                    lonely_guy = L[personne1]

                    # la personne associée à la personne sans personne devient alors la personne remplacée
                    personne2 = added[numero_remplacant]

                    # on échange
                    M[numero_remplacant] = (personne_selectionnee, lonely_guy)

                    # on remplace le nombre qu'on vient d'échanger avec celui de la personne bloquée
                    # ie : on met à jour la liste added en fonction de la transformation/échange que l'on vient de faire !
                    added[numero_remplacant] = personne1


                    #   DEBUG PRINT
                    """
                    print("\nligne concernée : ", numero_remplacant + 1)
                    print("\n", M[numero_remplacant])
                    """

            #       DEBUG PRINT
            """
            print("nmbre généré : personne2 = ", personne2)
            """

        # on associe les deux personnes à l'aide d'un couple (tuple)
        # note : cela devient un couple de couples
        #        oui il faut suivre un peu ;)

        tirage = ( L[personne1], L[personne2]  )

        #   DEBUG print
        """
        print('\n' ,tirage, '\n')
        """

        #on ajoute le tirage à la liste de tirages
        M.append(tirage)

        # et on signale quelle personne vient d'être ajoutée pour les prochaines ittérations
        added.append(personne2)

        # DEBUG PRINT
        """
        print(added, "\n")
        """
    return M









def mainTirage(mail_config_json_path, user_mail_list_path):
    """
    message
    """

    data = DataFromJSON(mail_config_json_path)

    message_body = data['message']['message_body']


    message_subject = data['message']['message_title']

    """
    Variables d'esthetique
    """

    nom = 0
    email = 1
    personne1 = 0
    personne2 = 1

    """
    Listes
    """


    csv_file = user_mail_list_path

    # Participants Brute
    L = from_csv_to_list(csv_file)
    M = creerListeDeCouples(L)

    K = tirageAuSort(M)

    print(Fore.GREEN + 'Permutation  =  ' + str(Permutation) + '\n\n' + 'K = ' + str(K) + Fore.WHITE + '\n\n\n' + Fore.YELLOW)


    for n in range(len(K)):
        print(K[n][personne1][nom], K[n][personne2][nom])
        envoyer_email(K[n][personne1], K[n][personne2], message_subject, message_body, mail_config_json_path )

    f.close()

    print(Fore.WHITE)
    return
