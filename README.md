# Rename
Small python script to quickly rename files in a folder (with a customizable increment)

## Liste des commandes :
```
aide
```
This command displays help (coming soon)

Alias : "help", "?"
```
clear
```
This command clears the console.

Alias : "cls"
```
show
```
This command displays the list of files processed by the script.

Alias : "view", "list"
```
define key<String> value<Int or String>(?)
```
This command allows you to temporarily redefine the configuration variables. "key" can be: ``index``, ``prefixe``, ``suffixe`` or ``confirmation``. If "key" is ``index`` so "value" is required and is a number. If "key" is ``confirmation`` "value" is "True" else confirmation will be set to "False". For ``prefixe`` and ``suffixe`` "value" can be omitted / empty (caution, white space are taken).

Alias : "set"
```
delete index<Int>
```
This command deletes the file located at the indicated "index" position.

Alias : "suppr", "del"
```
swap first<Int> second<Int>
```
This command interchange the positions of the files located at the "first" and "second" indexes

Alias : "permute", "rotate", "echange"
```
move first<Int> second<Int>
```
This command moves the position of the file located at the "first" index to the "second" index

Alias : "insert", "mv"

## Update variables in the code
To modify the variables "definitely", line 3 to 9:
```python
CONFIGURATION= {
    'index': 1, #Starting number for the increment.
    'prefixe': 'Épisode - ', #Text that appears before the index
    'suffixe': '', #Texte qui s'affiche après l'index
    'extensions': ('mp4', 'ogm', 'mkv', 'avi'), #Text that appears after the index
    'confirmation': False #If True, you will be asked for confirmation before renaming a file
}
```
