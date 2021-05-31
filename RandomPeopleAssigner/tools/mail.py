#   Email related LIBRAIRIES
#       SMTP Protocol
from RandomPeopleAssigner.tools.colors import H1
import smtplib
#       SSL encryption
import ssl
#       EMAIL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json



#       connections
#           Port GMAIL ssl
port = 465
smtp_server = "smtp.gmail.com"

#port = 1025
#smtp_server = "localhost"





# txt format
def messageBodyFromFile():
    with open('./message_body.txt', 'r') as f :
        lines = f.readlines()
        body = ""
        for k in range(len(lines)):
            body += lines[k]
    return body

def messageTitleFromFile():
    with open('./message_title.txt') as f:
        line = f.readline()
    return line


def dev_account_mail_and_password():
    with open('./login.txt', 'r') as f :
        lines = f.readlines()
        mail = lines[7]
        password = lines[10]
    return (mail, password)



#json format
def DataFromJSON(file_path):
    with open(file_path, 'r') as json_file :
        data = json.load(json_file)
    return data



def envoyer_email(destinataire, personneAttriubee, message_subject, message_body, mail_config_json_path):
    #   create a secure SSL context
    #       "This will load the system’s trusted CA certificates, enable host name checking and certificate validation, and try to choose reasonably secure protocol and cipher settings" - Real Python
    context = ssl.create_default_context()
    data = DataFromJSON(mail_config_json_path)
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
        try :
            server.login(mail_dev, password)
            print("\nlogged in!\n")
            print("sending mail...\n")
            server.sendmail(mail_dev, mail_destinataire, final_text.encode("utf-8"))
            print("mail sent to", mail_destinataire, " from ", mail_dev)
        except :
            H1("COULD NOT LOG IN, PLEASE CHECK LOGIN INFO")
    return 0
