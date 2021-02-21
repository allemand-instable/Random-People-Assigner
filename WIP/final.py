"""
LIBRAIRIES
"""
from __future__ import print_function, unicode_literals

"""
CLEAR FUNCTION
"""
#   DEBUG FUNCTIONS
#       os.sys("pause")
import csv

import RandomPeopleAssigner.random.cycle as cycle
import RandomPeopleAssigner.random.simultation as sim
import RandomPeopleAssigner.random.tirage as tirage

import RandomPeopleAssigner.tools.csv as csv_tools
import RandomPeopleAssigner.tools.mail as mail

import RandomPeopleAssigner.ui.data as data_module
import RandomPeopleAssigner.ui.menu as menu_module






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










"""
Questions and actions associated with the answers
"""





"""
MAIN FUNCTION
"""


def main():
    menu_module.loop( mail_config_json_path = data_json, user_mail_list_path = data_participants)
    return 0

# Définie la main
if __name__ == "__main__" :
    main()
