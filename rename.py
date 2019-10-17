import os
import re
import glob
CONFIGURATION= {}
CONFIGURATION['index']= 1
CONFIGURATION['prefixe']= 'Épisode - '
CONFIGURATION['suffixe']= ''
CONFIGURATION['extensions']= ('mp4', 'ogm', 'mkv', 'avi')
CONFIGURATION['confirmation']= False
FILES= []
def toInt(String):
	return int('0'+re.sub(r'\D', '', str(String)))
def toIndex(String):
	global FILES
	a= len(FILES)
	b= 1
	while a > 9:
		a/= 10
		b+= 1
	return str.zfill(str(String), b)
def show(Action, Parametre= False):
	if Action == "liste":
		global FILES
		a=0
		for b in FILES:
			print("[{}] {}".format(toIndex(a), b[0]))
			a+=1
	elif Action == "index":
		print("Les fichiers seront indenter à partir de {}".format(toIndex(Parametre)))
	elif Action == "config":
		global CONFIGURATION
		print('index: {}, préfixe: {}, suffixe: {}, confirmation: {}'.format(CONFIGURATION['index'], CONFIGURATION['prefixe'], CONFIGURATION['suffixe'], CONFIGURATION['confirmation']))
	elif Action == "header":
		print('''
 :::::::::  :::::::::: ::::    :::     :::     ::::    ::::  ::::::::::
 :+:    :+: :+:        :+:+:   :+:   :+: :+:   +:+:+: :+:+:+ :+:
 +:+    +:+ +:+        :+:+:+  +:+  +:+   +:+  +:+ +:+:+ +:+ +:+
 +#++:++#:  +#++:++#   +#+ +:+ +#+ +#++:++#++: +#+  +:+  +#+ +#++:++#
 +#+    +#+ +#+        +#+  +#+#+# +#+     +#+ +#+       +#+ +#+
 #+#    #+# #+#        #+#   #+#+# #+#     #+# #+#       #+# #+#
 ###    ### ########## ###    #### ###     ### ###       ### ##########''')
	elif Action == "help":
		print('''Help''')
def rename():
	global CONFIGURATION
	global FILES
	Index= CONFIGURATION['index']
	for f in FILES:
		path= "\\".join(f[0].split('\\')[0:-1])
		Fichier= "{}{}{}{}.{}".format((path+'\\', '')[path == ''], CONFIGURATION['prefixe'], CONFIGURATION['suffixe'], toIndex(Index), f[1])
		print("Renommage de `{}` en `{}`".format(f[0], Fichier))
		if CONFIGURATION['confirmation'] == True:
			Reponse= input("Continuer [O/N]? ").lower()
			if Reponse == "n":
				break
		os.rename(f[0], Fichier)
		print("fichier renomée !")
		Index+=1
def manager():
	Mots= input().lower().split(' ')
	global CONFIGURATION
	global FILES
	if Mots[0] in ("show", "view", "list"):
		show("liste")
	elif Mots[0] in ("help", "?", "aide"):
		show("help")
	elif Mots[0] in ("clear", "cls"):
		os.system("cls")
		show("header")
	elif Mots[0] in ("run"):
		rename()
	elif Mots[0] in ("exit", "bye"):
		os.system("pause")
		sys.exit()
	elif Mots[0] in ("prefixe", "pfx"):
		CONFIGURATION['prefixe']= ('', Mots[1])[len(Mots)>1]
		os.system("cls")
		show("header")
		show("config")
	elif Mots[0] in ("suffixe", "sfx"):
		CONFIGURATION['suffixe']= ('', Mots[1])[len(Mots)>1]
		os.system("cls")
		show("header")
		show("config")
	elif Mots[0] in ("index", "idx"):
		CONFIGURATION['index']= ('', toInt(Mots[1]))[len(Mots)>1]
		os.system("cls")
		show("header")
		show("config")
	elif Mots[0] in ("confirm") and len(Mots) > 1:
		CONFIGURATION['index']= (False, True)[Mots[1]=="false"]
		os.system("cls")
		show("header")
		show("config")
	elif Mots[0] in ("del", "delete", "suppr") and len(Mots) > 1 and toInt(mots[1]) > 0:
		del FILES[toInt(mots[1])]
		show("liste")
	elif Mots[0] in ("reverse", "rvs") and len(Mots) > 2:
		a= toInt(Mots[1])
		b= toInt(Mots[2])
		FILES[a], FILES[b] = FILES[b], FILES[a]
		show("liste")
	manager()
position= 1
for file in glob.glob('*'):
	extension= file.split('.')[-1]
	if extension in CONFIGURATION['extensions']:
		FILES.append([file, extension])
		position+= 1
os.system("cls")
os.system("color 09")
show("header")
show("config")
show("help")
manager()
