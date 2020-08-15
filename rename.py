INPUT_BUFFER= ''
FILES= []
CONFIGURATION= {
    'index': 1,
    'prefixe': 'Épisode - ',
    'suffixe': '',
    'extensions': ('mp4', 'ogm', 'mkv', 'avi'),
    'confirmation': False
}

import os
import glob

# Fonction Interne pour l'affichage des différents textes.
# @Param action : L'identifiant du textes à afficher.
#   @action header => Affiche le titre en ASCII art.
#   @action configuration => Affiche la configuration actuel.
#   @action aide => Affiche l'aide.
#   @action err_param => Affiche un message d'erreur pour les fonctions qui reçoivent trop ou les mauvais paramètres.
#   @action err_nparam => Affiche un message d'erreur pour les fonctions qui ne reçoivent pas suffisamment de paramètres.
#   @action type_error => Affiche un message d'erreur pour les fonctions qui reçoivent un paramètre mal typé.
# @OptionalParam err_param : Tuple contenant les paramètres excédent pour l'action "err_param".
# @OptionalParam expected_type : String contenant le type attendu pour l'action "type_error".
def fi_print(action, err_param = (), expected_type = ''):
    if action == "header":
        print('''
 :::::::::  :::::::::: ::::    :::     :::     ::::    ::::  ::::::::::
 :+:    :+: :+:        :+:+:   :+:   :+: :+:   +:+:+: :+:+:+ :+:
 +:+    +:+ +:+        :+:+:+  +:+  +:+   +:+  +:+ +:+:+ +:+ +:+
 +#++:++#:  +#++:++#   +#+ +:+ +#+ +#++:++#++: +#+  +:+  +#+ +#++:++#
 +#+    +#+ +#+        +#+  +#+#+# +#+     +#+ +#+       +#+ +#+
 #+#    #+# #+#        #+#   #+#+# #+#     #+# #+#       #+# #+#
 ###    ### ########## ###    #### ###     ### ###       ### ##########''')
    elif action == "configuration":
        print('index: {} | préfixe: \u0027{}\u0027 | suffixe: \u0027{}\u0027 | confirmation: {}'.format(
            CONFIGURATION['index'],
            CONFIGURATION['prefixe'],
            CONFIGURATION['suffixe'],
            CONFIGURATION['confirmation']
        ))
    elif action == "aide":
        print('''Help''')
    elif action == "err_param":
        if len(err_param) > 0:
            s_pluriel = 's' if len(err_param)>1 else '' #sujet
            v_pluriel = 'ent' if len(err_param)>1 else 't' #verbe
            c_pluriel = s_pluriel #complément
            print('Le{} paramètre{} "{}" n\u0027étai{} pas attendu{}.'.format(s_pluriel, s_pluriel, '", "'.join(err_param), v_pluriel, c_pluriel))
        else:
            print('Ce paramètre n\u0027était pas attendu.')
    elif action == "err_nparam":
        print('Un ou plusieurs paramètre(s) étai(en)t attendu(s).')
    elif action == "type_error":
        print('Le type attendu de la valeur était {}.'.format(expected_type))
    return

# Fonction interne qui supprime les blancs multiple.
# @Param chaine : La chaîne de caractères à nettoyer.
def fi_megatrim(chaine):
    return ' '.join(chaine.split()).strip()

# Fonction Interne qui formate dynamiquement un index en fonction de la longueur du tableau.
# @Param tableau : Le tableau de référence.
# @Param nombre : Le nombre à formater.
def fi_realindex(tableau, nombre):
    length= len(str(len(tableau)))
    return str.zfill(str(nombre), length)

# Fonction utilisateur dont le rôle est d'afficher l'aide
def aide(*a):
    if len(a)>0:
        fi_print("err_param", err_param = a)
    else:
        fi_print("aide")
    return
help = globals()['?'] = aide

# Fonction utilisateur dont le rôle et de vider l'écran
def clear(*a):
    if len(a)>0:
        fi_print("err_param", err_param = a)
    else:
        os.system("cls")
        fi_print("header")
        fi_print("configuration")
    return
globals()['cls'] = clear

# Fonction utilisateur dont le rôle est d'afficher la liste des fichiers
def show(*a):
    for index, fichier in enumerate(FILES): 
        print("[{}] {}".format(fi_realindex(FILES, index+CONFIGURATION['index']), fichier[0]))
    return
view = globals()['list'] = show

# Fonction utilisateur dont le rôle est de redéfinir temporairement les variables de configuration.
def define(clef = False, *valeurs):
    global CONFIGURATION
    if clef != False and clef != "extensions":
        if clef in CONFIGURATION:
            valeur = ' '.join(valeurs)
            if clef == "index":
                try:
                    valeur = int(valeur)
                except ValueError:
                    fi_print("type_error", expected_type = "<Int>")
                    return
            elif clef == "confirmation":
                valeur = True if valeur == "True" else False
            else:
                valeur = ' '.join(INPUT_BUFFER.split(' ')[2:])
            CONFIGURATION[clef] = valeur
            clear()
        else:
            fi_print("err_param", err_param = (clef,))
    else:
        fi_print("err_nparam")
    return
globals()['set'] = define

# Fonction utilisateur dont le rôle est de supprimer l'un des fichiers de la liste.
def delete(*valeurs):
    global FILES
    try:
        valeur = int(''.join(valeurs))-CONFIGURATION['index']
    except ValueError:
        fi_print("type_error", expected_type = "<Int>")
        return
    del FILES[valeur]
    show()
    return
suppr = globals()['del'] = delete

# Fonction utilisateur dont le rôle est d'échanger la position de deux fichiers dans la liste.
def swap(premier = False, second = False, *a):
    global FILES
    if premier == False and second == False:
        fi_print("err_nparam")
        return
    try:
        premier = int(premier)-CONFIGURATION['index']
        second = int(second)-CONFIGURATION['index']
    except ValueError:
        fi_print("type_error", expected_type = "<Int>")
        return
    FILES[premier], FILES[second] = FILES[second], FILES[premier]
    show()
    return
permute = rotate = echange = swap

# Fonction utilisateur dont le rôle est de déplacer un élément à une autre position dans la liste.
def move(element = False, position = False, *a):
    global FILES
    if element == False and position == False:
        fi_print("err_nparam")
        return
    try:
        element = int(element)-CONFIGURATION['index']
        position = int(position)-CONFIGURATION['index']
    except ValueError:
        fi_print("type_error", expected_type = "<Int>")
        return
    telement = FILES.pop(element)
    FILES.insert(position, telement)
    show()
    return
insert = mv = move

# Fonction qui lance le renomer les fichiers un par un
def run(*a):
    for index, fichier in enumerate(FILES):
        chemin = "\\".join(fichier[0].split('\\')[0:-1])
        rindex = fi_realindex(FILES, CONFIGURATION['index']+index)
        flname = "{}{}{}{}.{}".format((chemin+'\\', '')[chemin == ''], CONFIGURATION['prefixe'], rindex, CONFIGURATION['suffixe'], fichier[1])
        if CONFIGURATION['confirmation'] == True:
            print("Renommage de `{}` en `{}` ?".format(fichier[0], flname))
            confirm = input("Continuer [O/N]? ").lower()
            if confirm != "o":
                break
        os.rename(fichier[0], flname)
        if CONFIGURATION['confirmation'] == True:
            print("fichier renomée !")
        else:
            print("Fichier `{}` renommé en `{}`".format(fichier[0], flname))
    return

# Fonction Interne d'interaction avec l'utilisateur.
def fi_console():
    global INPUT_BUFFER
    INPUT_BUFFER= input('> ')
    instructions= fi_megatrim(INPUT_BUFFER).split(' ')
    commande= instructions.pop(0)
    if commande == "exit":
        os.system("pause")
        return
    elif commande.startswith('fi_') == False and commande in globals():
        globals()[commande](*instructions)
    else:
        print("Commande inconnue")
    fi_console()

for fichier in glob.glob('*'):
    extension= fichier.split('.')[-1]
    if extension in CONFIGURATION['extensions']:
        FILES.append([fichier, extension])

os.system("cls")
os.system("color 09")
fi_print("header")
fi_print("configuration")
fi_print("aide")
fi_console()
