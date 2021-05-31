#   Random FUNCTIONS
from RandomPeopleAssigner.tools.colors import H2, H3
from random import randint


from RandomPeopleAssigner.tools.csv import *
from RandomPeopleAssigner.tools.mail import *

from pprint import pprint


def tirageAuSort(List_of_name_and_mail : list):
    Tirages = []
    if len(List_of_name_and_mail) < 2 :
        raise Exception("il faut minimum 2 personnes pour effectuer un tirage au sort !")


    Receveurs = list(List_of_name_and_mail)
    Donneurs = list(List_of_name_and_mail)

    n = len(Donneurs)

    while n > 1 :
        # H2(f"longueur de L : {n}")
        personne_donneur_index = randint(0, n-1)
        # on s'assure de prendre deux individus différents
        # si on se place sur Z/nZ, si je retire à personne_donneur_index un nombre entre 1 et n
        # je ne peux lui retirer un tour complet, donc je ne peux pas revenir sur personne_donneur_index
        personne_receveur_index = (personne_donneur_index - randint(1, n-1) ) % n
        # H3(f"personne_donneur_index : {personne_donneur_index}")
        # on récupère le nom et l'email de chaque personne
        personne_receveur = Receveurs.pop(personne_receveur_index)
        # chacun doit donner une seule fois
        personne_donneur = Donneurs.pop(personne_donneur_index)
        """
        print(personne_donneur)
        H2("TIRAGE")
        """
        tirage = ( personne_donneur, personne_receveur )
        # print(tirage)
        
        Tirages.append(tirage)

        n = len(Donneurs)
        """
        H2('LIST')
        pprint(List_of_name_and_mail)
        H3("DONNEURS")
        pprint(Donneurs)
        H3("RECEVEURS")
        pprint(Receveurs)
        print("\n\n")
        """
    # il ne reste plus qu'à assigner les deux personnes restantes
    """
    pprint(Donneurs)
    pprint(Receveurs)
    print("\n\n")
    """
    Tirages.append( (Donneurs[0], Receveurs[0]) )
    """
    pprint(Tirages)
    """
    return Tirages



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
    # pprint(L)
    M = creerListeDeCouples(L)
    # pprint(M)
    K = tirageAuSort(M)
    # print(Fore.GREEN + 'Permutation  =  ' + str(Permutation) + '\n\n' + 'K = ' + str(K) + Fore.WHITE + '\n\n\n' + Fore.YELLOW)
    for n in range(len(K)):
        # print(K[n][personne1][nom], K[n][personne2][nom])
        envoyer_email(K[n][personne1], K[n][personne2], message_subject, message_body, mail_config_json_path )
    print(Fore.WHITE)
    wait = input('ENTER')
    return
