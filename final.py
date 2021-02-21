"""
LIBRAIRIES
"""


from __future__ import print_function, unicode_literals

import time

import regex

"""
CLI Libraries
"""

# PyInquirer 1
#from PyInquirer import style_from_dict, Token, prompt, Separator
#from PyInquirer import Validator, ValidationError
#from pprint import pprint


#PyInquirer2 support
from inquirer2 import prompt, Separator
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.styles import Style as prompt_toolkit_style


"""
COOL INSANE TITLE
"""

from pyfiglet import Figlet


"""
CLEAR FUNCTION
"""

clear = lambda: os.system('cls')


#   PRESENTATION
#       Couleurs

from colorama import Fore, Back, Style

#   DEBUG FUNCTIONS
#       os.sys("pause")

import os

#   Email related LIBRAIRIES
#       SMTP Protocol

import smtplib

#       SSL encryption

import ssl

#       EMAIL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#   Random FUNCTIONS
from random import randint
#   CSV files libraries
import csv

import json
































"""

GLOBAL VARIABLES

"""



data_json = './data/data.json'
data_participants = './data/participants.csv'



#       Files
#           destination du csv
f_participants = open( data_participants, encoding='utf-8')


simulation_path = './simulation/simulation.csv'


simulation_utf8 = open(simulation_path, 'w+' ,encoding='utf-8')



#           fichier csv des noms et emails
csv_participants = csv.reader(f_participants)

simulation_file = csv.reader(simulation_utf8)


#       connections
#           Port GMAIL ssl
port = 465
smtp_server = "smtp.gmail.com"

#port = 1025
#smtp_server = "localhost"














































"""
CSV TOOLS
"""




#   convertir le csv en une liste
#   facile à naviguer

def from_csv_to_list(csv_file):
    L = []
    for row in csv_file:
        L.append(row)
    return L



#   Crée une liste de couples
#   (Nom de la personne, son email)

def creerListeDeCouples(L):

    print(len(L))

    print(Fore.GREEN + str(L) + Fore.WHITE)
    M = []

    #   on parcourt l'ensemble des noms et emails, sachant que la première ligne est réservée aux titres
    for k in range(1, len(L) ):
        print(Fore.YELLOW +"nom : " + str(L[k][0]) + "   |    mail : " + str(L[k][1]) + Fore.WHITE)
        couple = (L[k][0], L[k][1])
        M.append( couple )
    return M















































"""
MAIL
"""
# txt format
def messageBodyFromFile():
    f = open('./message_body.txt', 'r')
    lines = f.readlines()
    body = ""
    for k in range(len(lines)):
        body += lines[k]
    return body

def messageTitleFromFile():
    f = open('./message_title.txt')
    lines = f.readlines()
    return lines[0]


def dev_account_mail_and_password():
    f.open('./login.txt', 'r')
    lines = f.readlines()
    mail = lines[7]
    password = lines[10]
    return (mail, password)



#json format
def DataFromJSON(file_path):

    with open(file_path, 'r') as json_file :
        data = json.load(json_file)
    return data



def envoyer_email(destinataire, personneAttriubee, message_subject, message_body):
    #   create a secure SSL context
    #       "This will load the system’s trusted CA certificates, enable host name checking and certificate validation, and try to choose reasonably secure protocol and cipher settings" - Real Python
    context = ssl.create_default_context()


    data = DataFromJSON(data_json)


    #   MDP MAIL DEV

    password = data['login']['password']

    #   MAILS

    mail_dev = data['login']['dev_email']
    mail_destinataire = destinataire[1]

    #   NOMS

    nom_destinataire = destinataire[0]
    nom_personneAtribuee = personneAttriubee[0]

    #   MESSAGE

    message = MIMEMultipart()

    message['From'] = mail_dev
    message['To'] = mail_destinataire
    message['Subject'] =  message_subject + ' | %(nom_destinataire)s'%{'nom_destinataire' : nom_destinataire}


    entree = """\
    Salut, %(nom_destinataire)s !

    """ %{'nom_destinataire' : nom_destinataire}


    annonce = """\
    la personne qui t'a été attribuée est : %(nom_personneAtribuee)s
    """ %{ 'nom_personneAtribuee' : nom_personneAtribuee }


    body = entree + message_body + annonce



    message.attach(MIMEText(body, 'plain'))





    """
    print(message)
    """


    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # attach the instance 'p' to instance 'msg'
    message.attach(p)

    # Converts the Multipart msg into a string
    final_text = message.as_string()

    # makes sure you're ending the connection at the end
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server :

        print("\n\nlogging in...")
        server.login(mail_dev, password)
        print("\nlogged in!\n")
        print("sending mail...\n")
        server.sendmail(mail_dev, mail_destinataire, final_text.encode("utf-8"))
        print("mail sent to", mail_destinataire, " from ", mail_dev)
    return 0



























































"""
TIRAGE
"""


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









def mainTirage():
    """
    message
    """

    data = DataFromJSON(data_json)

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


    csv_file = data_participants

    # Participants Brute
    L = from_csv_to_list(csv_file)
    M = creerListeDeCouples(L)

    K = tirageAuSort(M)

    print(Fore.GREEN + 'Permutation  =  ' + str(Permutation) + '\n\n' + 'K = ' + str(K) + Fore.WHITE + '\n\n\n' + Fore.YELLOW)


    for n in range(len(K)):
        print(K[n][personne1][nom], K[n][personne2][nom])
        envoyer_email(K[n][personne1], K[n][personne2], message_subject, message_body)

    f.close()

    print(Fore.WHITE)
    return






































"""

cycle

"""


"""
cycle aleatoire de [1,n]
"""

def PermutationAleatoire(nbre=7):
    P = []

    intervalle = [ k for k in range(nbre) ]


    for k in range(nbre):

        NbreAleat = randint(0, len(intervalle) - 1)
        #print(NbreAleat)
        P.append( intervalle[NbreAleat] )
        intervalle.pop(NbreAleat)

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

def mainBoucle():


    """
    message
    """

    data = DataFromJSON(data_json)

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

    # Participants Brute
    L = from_csv_to_list(file)
    M = creerListeDeCouples(L)

    """
    La boucle
    """
    Permutation = PermutationAleatoire(len(M))

    K = LaBoucle(M, Permutation)

    print(Fore.GREEN + 'Permutation  =  ' + str(Permutation) + '\n\n' + 'K = ' + str(K) + Fore.WHITE + '\n\n\n' + Fore.YELLOW)


    for n in range(len(K)):
        print(K[n][personne1][nom], K[n][personne2][nom])
        envoyer_email(K[n][personne1], K[n][personne2], message_subject, message_body)

    f.close()

    print(Fore.WHITE)
    return None

















































"""
Simulations
"""



def ligne(numero_tableau, numero_ligne):
    return 1 + 8*(numero_tableau - 1) + numero_ligne



def prochaineSimulation(K, nbr):
    print(simulation_path)


    with open(simulation_path, 'w', newline='', encoding='utf8') as csvfile:
        fieldnames = ['Nom', 'Personne attribuée']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for numero_simulation in range(nbr) :
            writer.writerow( {"Nom": "///  ESSAI NUMERO " + str(numero_simulation) + "   ///"})
            for n in range (len(K)):
                personne1 = K[n][0][0]
                personne2 = K[n][1][0]


                print(Fore.CYAN + 'K[' + str(n) + ']' + '[personne1] = ' +  Fore.YELLOW + str(personne1) + Fore.CYAN + '    K[' + str(n) + ']' + '[personne2] = ' + Fore.YELLOW + str(personne2))

                writer.writerow({'Nom': personne1, 'Personne attribuée': personne2})
    return None



def simulation_random(Participants, N):

    personne1 = 0
    personne2 = 1

    M = creerListeDeCouples(Participants)

    print(Fore.CYAN + str(M) + Fore.WHITE)


    print(simulation_path)

    for n in range(N):
        with open(simulation_path, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['Nom', 'Personne attribuée']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for numero_simulation in range(N) :
                writer.writerow( {"Nom": "///  ESSAI NUMERO " + str(numero_simulation + 1) + "   ///"})

                K = tirageAuSort(M)
                print(Fore.RED + str(K) + Fore.WHITE)

                for n in range (len(K)):
                    personne1 = K[n][0][0]
                    personne2 = K[n][1][0]


                    print(Fore.CYAN + 'K[' + str(n) + ']' + '[personne1] = ' +  Fore.YELLOW + str(personne1) + Fore.CYAN + '    K[' + str(n) + ']' + '[personne2] = ' + Fore.YELLOW + str(personne2))

                    writer.writerow({'Nom': personne1, 'Personne attribuée': personne2})

    return None



def simulation_cycle(Participants, N):

    personne1 = 0
    personne2 = 1

    M = creerListeDeCouples(Participants)

    print(Fore.CYAN + str(M) + Fore.WHITE)


    print(simulation_path)

    for n in range(N):
        with open(simulation_path, 'w', newline='', encoding='utf8') as csvfile:
            fieldnames = ['Nom', 'Personne attribuée']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for numero_simulation in range(N) :
                writer.writerow( {"Nom": "///  ESSAI NUMERO " + str(numero_simulation + 1) + "   ///"})

                Permutation = PermutationAleatoire(len(M))

                K = LaBoucle(M, Permutation)
                print(Fore.RED + str(K) + Fore.WHITE)

                for n in range (len(K)):
                    personne1 = K[n][0][0]
                    personne2 = K[n][1][0]


                    print(Fore.CYAN + 'K[' + str(n) + ']' + '[personne1] = ' +  Fore.YELLOW + str(personne1) + Fore.CYAN + '    K[' + str(n) + ']' + '[personne2] = ' + Fore.YELLOW + str(personne2))

                    writer.writerow({'Nom': personne1, 'Personne attribuée': personne2})

    return None




def mainSimulations(nbr_sim, mode):

    Participants = from_csv_to_list(csv_participants)
    print(Participants)


    if mode == 'tirage' :
        simulation_random(Participants, nbr_sim)

    elif mode == 'cycle':
        simulation_cycle(Participants, nbr_sim)

    wait = input('ENTER')

    return None
















































"""
MENU
"""



def ConstruireQuestions():

    Q = [


    {
        'type': 'list',
        'name': 'app_choice',
        'message': 'What do you want to do ?',
        'choices': ['Random Picker', 'Assign Cycle', 'Simulations', 'LOGIN & MAIL INFO','Quit']


    },


    {
        'type' : 'list',
        'name' : 'mode_simulation',
        'message': 'what do you want to simulate : ',
        'choices' : ['Random Picker', 'Assign Cycle'],
        'when' : lambda answers: answers['app_choice'] == 'Simulations'

    },

    {
        'type' : 'input',
        'name' : 'nbre_sim',
        'message': 'type the number of simulations you want to do : ',
        'when' : lambda answers: answers['app_choice'] == 'Simulations' and answers['mode_simulation']

    },

    # QUIT CONFIRM

    {
        'type': 'confirm',
        'name': 'quit_confirm',
        'message': 'Do you want to Exit ?',
        'default': False,
        'when': lambda answers: answers['app_choice'] == 'Quit'
    }

    ]

    return Q




def menu():

    #PYINQUIRER1

    """
    style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })
    """

    #PyInquirer2

    style = prompt_toolkit_style.from_dict({
        'separator': '#E91E63',
        'questionmark': '#E91E63',
        'focus': '#2196f3',
        'checked': '#2196f3',  # default
        'pointer': '#ff8700',  # AWS orange
        'instruction': '#ff8700',  # default
        'answer': '#00ffd7',  # AWS orange
        'question': '#2196f3',
    })

    questions = ConstruireQuestions()

    # PYINQUIRER1
    # answers = prompt(questions, style=style)

    #PyInquirer2
    answers = prompt.prompt(questions, style=style)

    return answers


def action():

    clear()

    f = Figlet(font='slant')
    print(Fore.GREEN + f.renderText('RANDOM PEOPLE ASSIGNER') + Fore.WHITE)

    print(Fore.CYAN + "A simple toolbox to randomly assign people to each other for party games, projects and more... written in Python 3\n\n " + Fore.WHITE)

    print("---   " + Fore.YELLOW + "Github/allemand-instable" + Fore.WHITE + "   ---\n\n\n")

    answer = menu()

    print(answer)


    if answer["app_choice"] == 'Quit' and answer["quit_confirm"] == True  :
        clear()
        return False

    elif answer['app_choice'] == 'LOGIN & MAIL INFO' :
        os.system('data.py')

    elif answer['app_choice'] == 'Random Picker' :
        mainTirage()
        pass

    elif answer['app_choice'] == 'Assign Cycle' :
        mainBoucle()
        pass

    elif answer['app_choice'] == 'Simulations' :
        if answer['mode_simulation'] == 'Random Picker'  :
            mainSimulations(int(answer['nbre_sim']), 'tirage')
        elif answer['mode_simulation'] == 'Assign Cycle'  :
            mainSimulations(int(answer['nbre_sim']), 'cycle')
        pass

    return True


def loop():
    running = True
    while running :
        running = action()
        print("running")
    return















"""
MAIN FUNCTION
"""


def main():
    loop()
    return 0

# Définie la main
if __name__ == "__main__" :
    main()
