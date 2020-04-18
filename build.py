from os import listdir, path
from sys import argv
from datetime import datetime
from termcolor import colored
import yaml

debug_mode = False
if len(argv) == 2 and argv[1] == 'debug':
    debug_mode = True
    print(colored("Debug mode is ON", "red"))

def debug_msg(name, value):
    print(colored("Debug message, "+name+": "+str(value), "grey"))
    

# Coverts unix timestamp into ISO 8601 date.
def format_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')                            # fix to local time plz

# Gets the first 4 lines from a markdown note,
# which contains the language, title, date created, category' of the notes on each line,
# then returns a dictionary.
#
# Example of markdown note document:
# ctime: 1587159587
# category: mathematics
# title: Order of a group and the class equation
# language: english
# 
def get_meta_from_md(FILE_PATH):
    with open(FILE_PATH, 'r') as MD_FILE:             # open markdown note
        yaml_str = "\n".join(MD_FILE.readlines()[:4]) # get 4 lines of yaml data
        return yaml.safe_load(yaml_str)               # load yaml data and return it.

# Updates the list of notes in list.yaml.
# Changes in notes directory will be automatically detected and applied to list.yaml.
# If there's any change applied to list, the function will return True.
# If there's no change applied, the function will return False.
def update_list():
    NOTES_PATH = 'notes'                            # path of notes
    FILE_EXT   = '.md'                              # extension of files
    LIST_PATH  = 'list.yaml'                        # path of list.yaml
    YAML_FILE  = open(LIST_PATH, 'r')               # open list.yaml file as readable and writable
    YAML_LOAD  = yaml.safe_load(YAML_FILE)          # load yaml data

    YAML_FILE.close()

    # Create list of current notes in directory, and load notes list on list.yaml to compare.
    dir_list = list(map(lambda s : NOTES_PATH+"/"+s, listdir(path=NOTES_PATH)))
    new_list = list(map(lambda s : {'perm' : s[len(NOTES_PATH)+1:-len(FILE_EXT)], 'mtime': int(path.getmtime(s))}, dir_list))
    new_list.sort(key=lambda dic : dic['mtime'] )
    old_list = [{'perm': note['perm'], 'mtime': note['mtime']} for note in YAML_LOAD]
    old_perm_list = [note['perm'] for note in YAML_LOAD]
    
    if debug_mode:
        debug_msg("new_list", new_list)
        debug_msg("old_list", old_list)

    # If there are some changes in note directory,
    if new_list != old_list:
        modified_or_added = list(filter(lambda dic : dic['mtime'] > old_list[-1]['mtime'], new_list))
        modified_or_added_perm = [note['perm'] for note in modified_or_added]

        modified = []
        added = []

        for note in modified_or_added:
            if note['perm'] in old_perm_list:
                modified.append(note)
            else:
                added.append(note)

        len_modified = len(modified)
        len_added = len(added)

        if debug_mode:
            debug_msg("modified_or_added", modified_or_added)
            debug_msg("modified_or_added_perm", modified_or_added_perm)
            debug_msg("modified", modified)
            debug_msg("added", added)

        if len_modified != 0:
            print(str(len_modified) + " MODIFICATION(S):")
            for note in modified:
                modified_date = format_date(note['mtime'])
                print(" - " + note["perm"] + FILE_EXT + " at " + modified_date)
        if len_added != 0:
            print(str(len_added) + " ADDITION(S):")
            for note in added:
                added_date = format_date(note['mtime'])
                print(" - " + note["perm"] + FILE_EXT + " at " + added_date)

        base_list_old = list(filter(lambda dic : (not (dic['perm'] in modified_or_added_perm )), old_list))
        base_list_new = list(filter(lambda dic : (not (dic['perm'] in modified_or_added_perm )), new_list))
        base_list_new_perm = [ note['perm'] for note in base_list_new ]
        removed = []

        if debug_mode:
            debug_msg("base_list_old", base_list_old)
            debug_msg("base_list_new", base_list_new)

        for note in base_list_old:
            if not (note['perm'] in base_list_new_perm):
                removed.append(note)

        if debug_mode:
            debug_msg("removed", removed)

        removed_perm = [note['perm'] for note in removed]
        len_removed = len(removed)

        if len_removed != 0:
            print(str(len_removed) + " REMOVE(S):")
            for note in removed:
                print (" - " + note["perm"] + FILE_EXT)

        # Add not changed notes.
        BASE_YAML_LOAD = list(filter(lambda dic : (not (dic['perm'] in modified_or_added_perm )
                                                   and not (dic['perm'] in removed_perm) ), YAML_LOAD))

        if debug_mode:
            debug_msg("modified_or_added", modified_or_added)

        # Add changed notes.
        for note in modified_or_added:
            base_note = get_meta_from_md(NOTES_PATH+"/"+note['perm']+FILE_EXT)
            base_note.update(note)
            BASE_YAML_LOAD.append(base_note)

        BASE_YAML_FILE = yaml.dump(BASE_YAML_LOAD)

        if debug_mode:
            debug_msg("BASE_YAML_LOAD", BASE_YAML_LOAD)
            debug_msg("BASE_YAML_FILE", BASE_YAML_FILE)

        YAML_FILE = open(LIST_PATH,"w")
        YAML_FILE.write(BASE_YAML_FILE)
        YAML_FILE.close()

        print(colored("Total " + str(len_modified+len_added+len_removed) + " change(s) applied.", 'green'))
        return True
    else:
        print(colored("There's nothing changed.", "green"))
        return False

def update_category():
    return 0

def create_article(head,tail,article):
    return 0

if update_list():
    update_category()
    create_article()
