from os import listdir, path, system, rename
from sys import argv
from datetime import datetime
from termcolor import colored
import yaml
import subprocess as sp

# Modes.

debug_mode = False

if len(argv) == 2 and argv[1] == 'debug':
    debug_mode = True
    print(colored("Debug mode is ON.", "red"))

regenerate_mode = False

if len(argv) == 2 and argv[1] == 'regenerate':
    regenerate_mode = True
    print(colored("Regenerating all notes.", "yellow"))

# Misc. Functions.

def debug_message(name, value):
    print(colored("Debug message, "+name+": "+str(value), "grey"))

def format_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S+0000')

# Variables.

TITLE = "S. Hyeon"

NOTES_PATH          = 'notes'
BLOG_PATH           = 'blog'
HTML_PATH           = 'html'
ICONS_PATH          = 'icons'
MD_EXT              = '.md'
HTML_EXT            = '.html'
INDEX               = 'index.html'
README              = 'README'
LIST_PATH           = 'list.yaml'
HEAD_PATH           = 'head.html'
TAIL_PATH           = 'tail.html'
RECENT_NOTES_PATH   = 'recent_notes.html'
MORE_PATH           = 'more.html'
STYLESHEET_PATH     = 'style.css'
CATEGORIES_PATH     = 'categories.yaml'
CATEGORY_PATH       = 'category'
LANGUAGE_PATH       = 'language'
BIN                 = '~/.Trash'
GITHUB_URL          = 'https://github.com/loudcolour/loudcolour.github.io'
RECENT_NOTES_AMOUNT = 5

# Load files.

HEAD_FILE = open(HTML_PATH + '/' + HEAD_PATH, 'r')
HEAD_LOAD = HEAD_FILE.read()
HEAD_FILE.close()

TAIL_FILE = open(HTML_PATH + '/' + TAIL_PATH, 'r')
TAIL_LOAD = TAIL_FILE.read()
TAIL_FILE.close()

YAML_FILE = open(LIST_PATH, 'r')
YAML_LOAD = yaml.safe_load(YAML_FILE)
YAML_FILE.close()

if debug_mode:
    debug_message("YAML_LOAD", YAML_LOAD)

new_list_perm = list(filter(lambda s : s[-len(MD_EXT):] == MD_EXT, listdir(path=NOTES_PATH)))
new_list_perm_mtime = list(map(lambda s : {'perm' : s[:-len(MD_EXT)], 'mtime': int(path.getmtime(NOTES_PATH+"/"+s))}, new_list_perm))
new_list_perm_mtime.sort(key=lambda dic : dic['mtime'])

old_list_perm = list(YAML_LOAD.keys())
old_list_perm_mtime = [{'perm': perm, 'mtime': YAML_LOAD[perm]['mtime']} for perm in old_list_perm]
old_list_perm_mtime.sort(key=lambda dic : dic['mtime'])

if debug_mode:
    debug_message("new_list_perm_mtime", new_list_perm_mtime)
    debug_message("old_list_perm_mtime", old_list_perm_mtime)

if (new_list_perm_mtime != old_list_perm_mtime) or regenerate_mode:
    modified_or_added_perm_mtime = list(filter(lambda dic : dic['mtime'] > old_list_perm_mtime[-1]['mtime'], new_list_perm_mtime))
    modified_or_added_perm = [note['perm'] for note in modified_or_added_perm_mtime]
    modified_perm_mtime = []
    added_perm_mtime = []

    for dic in modified_or_added_perm_mtime:
        if dic['perm'] in old_list_perm:
            modified_perm_mtime.append(dic)
        else:
            added_perm_mtime.append(dic)

    len_modified = len(modified_perm_mtime)
    len_added = len(added_perm_mtime)

    if debug_mode:
        debug_message("modified_or_added_perm_mtime", modified_or_added_perm_mtime)
        debug_message("modified_or_added_perm", modified_or_added_perm)
        debug_message("modified_perm_mtime", modified_perm_mtime)
        debug_message("added_perm_mtime", added_perm_mtime)

    if len_modified != 0:
        print(colored(str(len_modified) + " MODIFICATION(S):", "yellow"))
        for dic in modified_perm_mtime:
            modified_date = format_date(dic['mtime'])
            print(colored(" - " + dic["perm"] + MD_EXT + " at " + modified_date,"yellow"))
        print("")
    if len_added != 0:
        print(colored(str(len_added) + " ADDITION(S):", "green"))
        for dic in added_perm_mtime:
            added_date = format_date(dic['mtime'])
            print(colored(" - " + dic["perm"] + MD_EXT + " at " + added_date,"green"))
        print("")

    base_list_old = list(filter(lambda dic : (not (dic['perm'] in modified_or_added_perm )), old_list_perm_mtime))
    base_list_new = list(filter(lambda dic : (not (dic['perm'] in modified_or_added_perm )), new_list_perm_mtime))
    base_list_new_perm = [note['perm'] for note in base_list_new]
    removed_perm_mtime = []

    if debug_mode:
        debug_message("base_list_old", base_list_old)
        debug_message("base_list_new", base_list_new)

    for dic in base_list_old:
        if not (dic['perm'] in base_list_new_perm):
            removed_perm_mtime.append(dic)

    if debug_mode:
        debug_message("removed_perm_mtime", removed_perm_mtime)

    removed_perm = [note['perm'] for note in removed_perm_mtime]
    len_removed = len(removed_perm_mtime)

    if len_removed != 0:
        print(colored(str(len_removed) + " REMOVE(S):", "red"))
        for note in removed_perm_mtime:
            print(colored(" - " + note["perm"] + MD_EXT, "red"))
        print("")

    # Get new tag data.

    def get_meta_from_md(perm):
        INPUT_PATH = NOTES_PATH + "/" + perm + MD_EXT
        with open(INPUT_PATH, 'r') as MD_FILE:
            yaml_str = "\n".join(MD_FILE.readlines()[1:4])
            meta = yaml.safe_load(yaml_str)
            if sorted(meta.keys()) == ['category','language','title']: 
                return meta
            else:
                print(colored("Metadata on note is not valid.", "red"))
                exit(1)

    BASE_YAML_LOAD_perm = list(filter(lambda perm : (not (perm in modified_or_added_perm )
                                                     and not (perm in removed_perm) ), old_list_perm))
    BASE_YAML_LOAD = {}
    for perm in BASE_YAML_LOAD_perm:
        BASE_YAML_LOAD[perm] = YAML_LOAD[perm]

    for dic in modified_or_added_perm_mtime:
        base_dic = get_meta_from_md(dic['perm'])
        base_dic['mtime'] = dic['mtime']
        BASE_YAML_LOAD[dic['perm']] = base_dic
        BASE_YAML_LOAD_perm.append(dic['perm'])

    if debug_mode:
        debug_message("BASE_YAML_LOAD", BASE_YAML_LOAD)
    
    # Generate or delete notes.

    def generate_blog_note(perm):
        INPUT_PATH = NOTES_PATH + "/" + perm + MD_EXT
        OUTPUT_PATH = BLOG_PATH + "/" + perm + HTML_EXT

        pandoc_command = ["pandoc", INPUT_PATH, "-f", "gfm", "-t", "html"]

        PARSED = sp.Popen(pandoc_command, stdout=sp.PIPE, stderr=sp.PIPE)
        STDOUT, STDERR = PARSED.communicate()

        if STDERR != b'':
            print(STDERR.decode("utf-8"))
            exit(1)

        full_meta = BASE_YAML_LOAD[perm]
        HEAD_FILLED = HEAD_LOAD
        TAIL_FILLED = TAIL_LOAD

        for tag in ['title', 'category', 'language']:
            HEAD_FILLED = HEAD_FILLED.replace('{% '+tag+' %}', str(full_meta[tag]))
            TAIL_FILLED = TAIL_FILLED.replace('{% '+tag+' %}', str(full_meta[tag]))

            if debug_mode:
                debug_message("replaced", '{% '+tag+' %}')
                debug_message("full_meta[tag]", full_meta[tag])
        
            HEAD_FILLED = HEAD_FILLED.replace('{% mtime_formatted %}', format_date(full_meta['mtime']))
            TAIL_FILLED = TAIL_FILLED.replace('{% mtime_formatted %}', format_date(full_meta['mtime']))

        urls_meta = {
            'language_url': "../" + LANGUAGE_PATH + "/" + full_meta['language'] + HTML_EXT, 
            'category_url': "../" + CATEGORY_PATH + "/" + full_meta['category'] + HTML_EXT,
            'blame_url': GITHUB_URL + '/blame/master/' + INPUT_PATH,
            'history_url': GITHUB_URL + '/commits/master/' + INPUT_PATH,
        }

        for key in urls_meta.keys():
            HEAD_FILLED = HEAD_FILLED.replace('{% '+key+' %}', urls_meta[key])
            TAIL_FILLED = TAIL_FILLED.replace('{% '+key+' %}', urls_meta[key])

        STYLESHEET = "../" + STYLESHEET_PATH
        HEAD_FILLED = HEAD_FILLED.replace('{% stylesheet %}', STYLESHEET)

        ICONS = "../" + ICONS_PATH
        HEAD_FILLED = HEAD_FILLED.replace('{% icons %}', ICONS)

        VISIBILITY = ""        
        HEAD_FILLED = HEAD_FILLED.replace('{% visibility %}', VISIBILITY)

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + STDOUT.decode("utf-8") + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    def delete_blog_note(perm):
        INPUT_PATH = BLOG_PATH + "/" + perm + HTML_EXT
        OUTPUT_PATH = BIN + "/" + perm + HTML_EXT

        if path.isfile(INPUT_PATH):
            rename(INPUT_PATH, OUTPUT_PATH)
            print(colored("Moved " + INPUT_PATH + " to bin.", "red"))
        else:
            print(colored("Couldn't find "+INPUT_PATH+".","yellow"))

    generate_list_perm = []

    if regenerate_mode:
        generate_list_perm = BASE_YAML_LOAD_perm
    else:
        generate_list_perm = modified_or_added_perm

    for perm in generate_list_perm:
        generate_blog_note(perm)

    for perm in removed_perm:
        delete_blog_note(perm)

    # Generate index.html. perm of index.html is README.

    def generate_index():
        INPUT_PATH = README + MD_EXT
        OUTPUT_PATH = INDEX

        pandoc_command = ["pandoc", INPUT_PATH, "-f", "gfm", "-t", "html"]

        PARSED = sp.Popen(pandoc_command, stdout=sp.PIPE, stderr=sp.PIPE)
        STDOUT, STDERR = PARSED.communicate()

        if STDERR != b'':
            print(STDERR.decode("utf-8"))
            exit(1)

        HEAD_FILLED = HEAD_LOAD
        TAIL_FILLED = TAIL_LOAD
        
        HEAD_FILLED = HEAD_FILLED.replace('{% title %}', TITLE)

        STYLESHEET = "./" + STYLESHEET_PATH
        HEAD_FILLED = HEAD_FILLED.replace('{% stylesheet %}', STYLESHEET)

        ICONS = "./" + ICONS_PATH
        HEAD_FILLED = HEAD_FILLED.replace('{% icons %}', ICONS)

        VISIBILITY = "display: none;"        
        HEAD_FILLED = HEAD_FILLED.replace('{% visibility %}', VISIBILITY)

        notes_perm_title_mdate = [{'perm': key,
                                   'title': BASE_YAML_LOAD[key]['title'],
                                   'mtime': BASE_YAML_LOAD[key]['mtime']} for key in BASE_YAML_LOAD.keys()]
        notes_perm_title_mdate.sort(key=lambda dic : dic['mtime'], reverse=True)
        list_of_recent_notes = notes_perm_title_mdate[:RECENT_NOTES_AMOUNT]
        list_of_recent_notes = list(map(lambda dic: '<li><a href="'
                                                    +BLOG_PATH+"/"+dic['perm']
                                                    +HTML_EXT+'">'+dic['title']
                                                    +"</a></li>",list_of_recent_notes))
        RECENT_NOTES = "\n".join(list_of_recent_notes)
        RECENT_NOTES_FILLED = ""

        with open(HTML_PATH+"/"+RECENT_NOTES_PATH, 'r') as RECENT_NOTES_FILE:
            RECENT_NOTES_FILLED = RECENT_NOTES_FILE.read().replace('{% list %}', RECENT_NOTES)
        
        RECENT_NOTES_FILLED = RECENT_NOTES_FILLED.replace('{% more %}', MORE_PATH)

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + STDOUT.decode("utf-8") + RECENT_NOTES_FILLED + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    generate_index()

    # Update list.yaml.

    BASE_YAML_FILE = yaml.safe_dump(BASE_YAML_LOAD)

    with open(LIST_PATH, 'w') as YAML_FILE:
        YAML_FILE.write(BASE_YAML_FILE)
        if not regenerate_mode:
            print(colored("Total " + str(len_modified+len_added+len_removed) + " change(s) applied.", 'green'))

else:
    print(colored("There's nothing changed.", "green"))
