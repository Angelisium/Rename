# Rename
Script Python pour renomer rapidement les fichiers d'un dossier.
Pour les question&suggestion https://discord.gg/8Qyg9Q7

## Liste des commandes :
```
aide
```
Cette commande affiche l'aide (prochainement)

Alias : "help", "?"
```
clear
```
Cette commande vide la console.

Alias : "cls"
```
show
```
Cette commande affiche la liste des fichiers traité par le script.

Alias : "view", "list"
```
define clef<String> valeur<Int or String>(?)
```
Cette commande permet de redéfinir temporairement les variables de configuration. "clef" peut être : ``index``, ``prefixe``, ``suffixe`` ou ``confirmation``. Si "clef" est ``index`` alors "valeur" est requis et est un chiffre. Si "clef" est ``confirmation`` "valeur" doit être "True" sinon la confirmation sera défini à "False". Pour ``prefixe`` et ``suffixe`` "valeur" peut être omis / vide (attention, les caractères blancs sont pris en compte).

Alias : "set"
```
delete index<Int>
```
Cette commande permet de supprimer le fichier situé à la position "index" indiqué.

Alias : "suppr", "del"
```
swap permier<Int> deuxieme<Int>
```
Cette commande permet d'interchangé les positions des fichiers situé aux index "premier" et "deuxieme"

Alias : "permute", "rotate", "echange"
```
move element<Int> position<Int>
```
Cette commande permet de déplacer l'élément à la position "element" en position "position".

Alias : "insert", "mv"

## Modification dans le code
Pour modifier en dure les variables, ligne 3 à 9:
```python
CONFIGURATION= {
    'index': 1, #Nombre de départ pour l'incrémentation.
    'prefixe': 'Épisode - ', #Texte qui s'affiche avant l'index
    'suffixe': '', #Texte qui s'affiche après l'index
    'extensions': ('mp4', 'ogm', 'mkv', 'avi'), #Liste des formats de fichier pris en compte par le script
    'confirmation': False #Si à True, une confirmation vous sera demandez avant de renommer un fichier
}
```
