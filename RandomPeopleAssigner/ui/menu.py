"""
CLI Libraries
"""
import regex

#PyInquirer2 support
from inquirer2 import prompt, Separator
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.styles import Style as prompt_toolkit_style

import os

"""
COOL INSANE TITLE
"""
from pyfiglet import Figlet

#   PRESENTATION
#       Couleurs
from colorama import Fore, Back, Style





import RandomPeopleAssigner.random.cycle as cycle
import RandomPeopleAssigner.random.simultation as sim
import RandomPeopleAssigner.random.tirage as tirage




clear = lambda: os.system('cls')


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

def action(mail_config_json_path, user_mail_list_path):

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
        tirage.mainTirage(mail_config_json_path, user_mail_list_path)

    elif answer['app_choice'] == 'Assign Cycle' :
        cycle.mainBoucle()

    elif answer['app_choice'] == 'Simulations' :
        if answer['mode_simulation'] == 'Random Picker'  :
            sim.mainSimulations(nbr_sim = int(answer['nbre_sim']), mode = 'tirage', user_mail_list_path = user_mail_list_path)
        elif answer['mode_simulation'] == 'Assign Cycle'  :
            sim.mainSimulations(nbr_sim = int(answer['nbre_sim']), mode = 'cycle', user_mail_list_path = user_mail_list_path)

    return True







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



def loop(mail_config_json_path, user_mail_list_path):
    running = True
    while running :
        running = action(mail_config_json_path, user_mail_list_path)
        print("running")
    return


def start_menu():
    clear()
    mail_config_json_path = "./data/data.json"
    user_mail_list_path = "./data/participants.csv"
    loop(mail_config_json_path= mail_config_json_path, user_mail_list_path= user_mail_list_path)
