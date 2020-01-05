# Rename
Script Python pour renomer rapidement les fichiers d'un dossier.
Pour les question&suggestion https://discord.gg/aqYXZYE 

Actuellement:
```"show", "view", "list" => Affiche la liste des fichiers traiter par le script
"help", "?", "aide" => Affiche l'aide
"clear", "cls" => clear la console
"run" => lance le renomage
"exit", "bye" => ferme la fenetre
"prefixe <?String>", "pfx <?String>" => modifie le prefixe (argument optionnel)
"suffixe <?String>", "sfx <?String>" => modifie le suffixe (argument optionnel)
"index <?Int>", "idx <?Int>" => modifie l'index de départ (argument optionnel)
"confirm <String>" => false pour ne pas avoir de confirmation a chaque fichier
"del <Int>", "delete <Int>", "suppr <Int>" => Retire un fichier de la liste
"reverse <Int1> <Int2>", "rvs <Int1> <Int2>" => échange la position de Int1 et Int2
"move <Int1> <Int2>", "mve <Int1> <Int2>" => place Int1 devant Int2
```

Pour modifier en dure les variables, ligne 5 à 9:
```python
CONFIGURATION['index']= 1 #Nombre de départ pour l'incrémentation.
CONFIGURATION['prefixe']= 'Épisode - ' #Texte qui s'affiche avant l'index
CONFIGURATION['suffixe']= '' #Texte qui s'affiche après l'index
CONFIGURATION['extensions']= ('mp4', 'ogm', 'mkv', 'avi') #Liste des formats de fichier pris en compte par le script
CONFIGURATION['confirmation']= False #A true, une confirmation vous sera demandez avant de renommer un fichier
```
