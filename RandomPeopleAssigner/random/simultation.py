import csv
from RandomPeopleAssigner.random.cycle import LaBoucle, PermutationAleatoire
from RandomPeopleAssigner.random.tirage import tirageAuSort
from colorama.ansi import Fore
from RandomPeopleAssigner.tools.csv import creerListeDeCouples, from_csv_to_list


def ligne(numero_tableau, numero_ligne):
    return 1 + 8*(numero_tableau - 1) + numero_ligne



def prochaineSimulation(K, nbr, simulation_path):
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



def simulation_random(Participants, N, simulation_path):

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



def simulation_cycle(Participants, N, simulation_path):

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




def mainSimulations(nbr_sim, mode, user_mail_list_path, simulation_path = "./simulation/simulation.csv"):

    Participants = from_csv_to_list(user_mail_list_path)
    print(Participants)


    if mode == 'tirage' :
        simulation_random(Participants, nbr_sim, simulation_path)

    elif mode == 'cycle':
        simulation_cycle(Participants, nbr_sim, simulation_path)

    wait = input('ENTER')

    return None
