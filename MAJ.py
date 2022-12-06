import os 
import time
import getpass

username = getpass.getuser()
#source : https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python

from requests_html import HTMLSession



# ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ #

expired_version = 'NTool-V01.py'
version = 'NTool-V01'
last_version = 'FiveM.exe'

path = os.getcwd()
os.system('mode con: cols=80 lines=20')
# ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ #


def tool_update():
    


    ## Execution probable sur la version suivante.
    ## A chaque démarage on supprime l'ancienne version.
    ## Lors de la mise a jour, vue que le lancement de la nouvelle version est automatique alors celle-ci supprime la précedente.
    print('Please wait, checking for updates. 1/2')

    os.chdir(path)
    print(path) # Debug : Print cd
    try:
        os.remove(eexpired_version)
    except:
        print('none')

    # get last version // instalation 

    print('Please wait, checking for updates. 2/2')

    s = HTMLSession()
    link = "https://github.com/Nuxhi" # on regarde.
    link_update = "https://github.com/Nuxhi/NTool/blob/main/README.md" # Si une version est disponible, alors on la télécharge grace à "link_update"
    rqt = s.get(link)
    

    #Vérification de la disponibilité des serveurs.

    if rqt.ok:
        print('Connection to the update server')
    else:
        print('[Console] : Serveur indisponible : ', rqt,'\nDirigez-vous sur notre discord !')
        time.sleep(2), main_menu()

    #Si le serveur est disponbile alors on essaye de vérifié.

    try:
        title = rqt.html.find('.p-org')[0].text
    except:
        title = ('UKN')
    
    if title != version:
        print('update disponible !\nVersion : ',title,'disponible,\nTéléchargement en cours...')
        r_upt = s.get(link_update, allow_redirects=True)
        open('README.md', 'wb').write(r_upt.content)
        


        time.sleep(5)
        os.startfile(last_version)
        print('start', last_version)




    else:
        print('Aucune update disponible !')
    time.sleep(1)
    




tool_update()

def main_menu():

    print("\n                          Bienvenu sur :", version)
    print("\n                       ╔══════════════════════════════╗")
    print("                       ║                              ║")
    print("                       ║        1.  Main menu         ║")
    print("                       ║                              ║")
    print("                       ╚══════════════════════════════╝\n")
    choix = input(" [CONSOLE]   :  ")
    if choix == '1':
        main_menu() 

    return 'menu', time.sleep(2), main_menu()


main_menu()
