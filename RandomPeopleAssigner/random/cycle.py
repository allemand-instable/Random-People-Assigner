"""

cycle

"""

from RandomPeopleAssigner.tools.csv import creerListeDeCouples, from_csv_to_list
from RandomPeopleAssigner.tools.mail import DataFromJSON, envoyer_email
from colorama import Fore, Back, Style


#   Random FUNCTIONS
from random import randint


"""
cycle aleatoire de [1,n]
"""

def PermutationAleatoire(nbre):
    P = []

    intervalle = [ k for k in range(nbre) ]


    for k in range(nbre):

        NbreAleat = randint(0, len(intervalle) - 1)
        #print(NbreAleat)
        P.append( intervalle[NbreAleat] )
        intervalle.pop(NbreAleat)

    print(Fore.YELLOW + 'done' + Fore.WHITE)
    return P




"""
création de la boucle
"""



def LaBoucle(Personnes, Permutation):

    M = []


    longueur = len(Permutation)

    print('\n\n\n' + Fore.CYAN + str(Personnes) + '\n\n' + Fore.YELLOW + str(Permutation) + Fore.WHITE)
    for k in range(longueur):
        # si c est le dernier, on l'assigne au premier
        if (k == longueur - 1):
            Couple = (Personnes[ Permutation[ longueur - 1] ], Personnes[ Permutation[0] ] )
            M.append(Couple)

        # sinon on l'assigne juste au suivant
        else:
            Couple = ( Personnes[ Permutation[k] ], Personnes[ Permutation[ k + 1 ] ] )
            M.append(Couple)
    return M


"""
processus de Bouclage
"""

def mainBoucle(user_mail_list_path = "./data/participants.csv", data_json_path = "./data/data.json"):
    """
    message
    """
    data = DataFromJSON(data_json_path)
    message_body = data['message']['message_body']
    message_subject = data['message']['message_title']
    """
    Variables d'esthetique
    """
    personne1 = 0
    personne2 = 1
    """
    Listes
    """
    # Participants Brute
    L = from_csv_to_list(user_mail_list_path)
    M = creerListeDeCouples(L)
    """
    La boucle
    """
    Permutation = PermutationAleatoire(len(M))
    K = LaBoucle(M, Permutation)
    # print(Fore.GREEN + 'Permutation  =  ' + str(Permutation) + '\n\n' + 'K = ' + str(K) + Fore.WHITE + '\n\n\n' + Fore.YELLOW)
    for n in range(len(K)):
        # print(f"mail envoyé : {K[n][personne1][nom]} | {K[n][personne2][nom]}")
        envoyer_email(K[n][personne1], K[n][personne2], message_subject, message_body, data_json_path)
    print(Fore.WHITE)
    wait = input('ENTER')
    return None
