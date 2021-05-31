"""
CSV TOOLS
"""
from colorama import Fore, Back, Style
import csv



#   convertir le csv en une liste
#   facile à naviguer

def from_csv_to_list(csv_file_path):
    L = []
    with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
        lines = csv.reader(csv_file, delimiter = ",")
        for row in lines:
            L.append(row)
        return L



#   Crée une liste de couples
#   (Nom de la personne, son email)

def creerListeDeCouples(L):
    #print(len(L))
    #print(Fore.GREEN + str(L) + Fore.WHITE)
    M = []
    #   on parcourt l'ensemble des noms et emails, sachant que la première ligne est réservée aux titres
    for k in range(1, len(L) ):
        print(Fore.YELLOW +"nom : " + str(L[k][0]) + "   |    mail : " + str(L[k][1]) + Fore.WHITE)
        couple = (L[k][0], L[k][1])
        M.append( couple )
    return M
