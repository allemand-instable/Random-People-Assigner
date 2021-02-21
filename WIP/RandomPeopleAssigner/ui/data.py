"""
IMPORT JSON
"""


import json



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

from shutil import copyfile


def est_non_vide(fpath):
    # print(Fore.RED + str(os.stat(fpath).st_size) +Fore.WHITE)
    return os.path.isfile(fpath) and os.stat(fpath).st_size > 0


j_location_file = './data/data.json'











def WriteToJSON(file, data):

    # on vérifie si le fichier est vide

    JSON_non_vide = est_non_vide(file)
    # print(JSON_non_vide)


    with open(file, 'r+', encoding='utf-8') as f:

        print(os.path.isfile(file))

        # data is already stored
        if JSON_non_vide :
            # we read the existing Data
            # note : this call is the reason why we need to
            # have 2 cases : file empty or not
            pre_data = json.load(f)

            print(Fore.YELLOW + 'OLD JSON DATA : ' + Fore.CYAN, pre_data, '\n')

            # updating the data
            pre_data.update( data )
            print(Fore.YELLOW + 'NEW JSON DATA : ' + Fore.CYAN, pre_data,  '\n')

            wait = input('enter')
            # erasing previous
            f.truncate(0)

            # writing updated json
            f.seek(0)
            json.dump(pre_data, f, ensure_ascii=False, indent=4)


        # JSON file is empty

        else :
            print(Fore.YELLOW + '[EMPTY] NEW JSON DATA : ' + Fore.CYAN, data,  '\n')
            json.dump(data, f, ensure_ascii=False, indent=4)


    return













def ReadJson(file):

    with open(file) as json_file :
        data = json.load(json_file)

        print(Fore.YELLOW + 'JSON DATA : ' + Fore.CYAN)
        print(json.dumps(data, indent = 4, sort_keys=True))
        if 'login' in data :
            a = data['login']['dev_email'] ; b= data['login']['password']
            print(Fore.RED + "===============================================================================================" + Fore.WHITE)
            print(Fore.YELLOW + 'dev email : ' + Fore.CYAN + a)
            print(Fore.RED + "===============================================================================================" + Fore.WHITE)
            print(Fore.YELLOW + 'password  : ' + Fore.CYAN + b)
            print(Fore.RED + "===============================================================================================" + Fore.WHITE)
        if 'message' in data :
            c = data['message']['message_title'] ; d = data['message']['message_body']
            print(Fore.YELLOW + 'message title : ' + Fore.CYAN + c )
            print(Fore.RED + "===============================================================================================" + Fore.WHITE)
            print(Fore.YELLOW + 'message body : ' + Fore.CYAN + d)
            print(Fore.RED + "===============================================================================================" + Fore.WHITE)
    wait = input(Fore.WHITE + "PRESS ENTER TO CONTINUE.")

    return











def ConstruireQuestions():

    Q = [


    {
        'type': 'list',
        'name': 'app_choice',
        'message': 'What do you want to do ?',
        'choices': ['DEV-MAIL Account Login Info', 'Message Info', 'Current Info','Quit']


    },




    # QUIT CONFIRM

    {
        'type': 'confirm',
        'name': 'quit_confirm',
        'message': 'Do you want to Exit ?',
        'default': False,
        'when': lambda answers: answers['app_choice'] == 'Quit'
    },

    {
        'type' : 'input',
        'name' : 'login_mail',
        'message' : 'please enter your mail in the format email@gmail.com : ',
        'when' : lambda answers: answers['app_choice'] == 'DEV-MAIL Account Login Info'

    },

    {
        'type' : 'password',
        'name' : 'login_password',
        'message' : 'please enter your mail password : ',
        'when' : lambda answers: answers['app_choice'] == 'DEV-MAIL Account Login Info' and answers['login_mail']

    },

    {
        'type' : 'input',
        'name' : 'message_title',
        'message' : 'please enter the email\'s title : ',
        'when' : lambda answers: answers['app_choice'] == 'Message Info'
    },

    {
        'type' : 'editor',
        'name' : 'message_body',
        'message' : 'please enter the email\'s title : ',
        'when' : lambda answers: answers['app_choice'] == 'Message Info' and answers['message_title']
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
    print(Fore.GREEN + f.renderText('RPA - ') + Fore.YELLOW + f.renderText('LOGIN & MESSAGE INFO') + Fore.WHITE)

    print(Fore.CYAN + "A simple toolbox to randomly assign people to each other for party games, projects and more... written in Python 3\n\n " + Fore.WHITE)

    print("---   " + Fore.YELLOW + "Github/allemand-instable" + Fore.WHITE + "   ---\n\n\n")

    answer = menu()

    print(answer)


    if answer["app_choice"] == 'Quit' and answer["quit_confirm"] == True  :
        clear()
        return False

    elif answer['app_choice'] == 'DEV-MAIL Account Login Info' :

        data = {}
        data['login'] =  {

            'dev_email' : answer['login_mail'],
            'password' : answer['login_password']

        }
        WriteToJSON(j_location_file, data)
        ReadJson(j_location_file)
    elif answer['app_choice'] == 'Message Info' :

        data = {}
        data['message'] = {

            'message_title' : answer['message_title'],
            'message_body' : answer['message_body']

        }
        WriteToJSON(j_location_file, data)
        ReadJson(j_location_file)

        pass

    elif answer['app_choice'] == 'Current Info' :
        ReadJson(j_location_file)

    return True

def loop():
    running = True
    while running :
        running = action()
        print("running")
    return

def main():
    loop()
    return

# Définie la main
if __name__ == "__main__" :
    main()
