from os import listdir, path, system, remove
from sys import argv
from datetime import datetime, timezone
from termcolor import colored
from functools import reduce

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

import re
import yaml
import tzlocal
import subprocess as sp

LOCAL_TZ = tzlocal.get_localzone()

# Modes.

debug_mode = False
regenerate_mode = False

if 'debug' in argv:
    debug_mode = True
    print(colored("Debug mode is ON.", "red"))

if 'regenerate' in argv:
    regenerate_mode = True
    print(colored("Regenerating all notes.", "yellow"))

# Misc. Functions.

def debug_message(name, value):
    print(colored("Debug message, "+name+": "+str(value), "grey"))

def format_date(timestamp):
    return datetime.fromtimestamp(timestamp, LOCAL_TZ).strftime('%Y-%m-%dT%H:%M:%S%z')

def math_tex_to_html(tex_str, display_mode=False):
    katex_command = ["./node_modules/.bin/katex"]
    
    if display_mode:
        katex_command.append('-d')

    if debug_mode:
        debug_message("tex_str", tex_str)
        debug_message("display_mode", display_mode)

    APPLY_KATEX = sp.Popen(katex_command, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
    STDOUT, STDERR = APPLY_KATEX.communicate(input=tex_str.encode("utf-8"))

    if debug_mode:
        debug_message("STDOUT", STDOUT.decode("utf-8"))
    
    if STDERR != b'':
            print(STDERR.decode("utf-8"))
            exit(1)
    
    return STDOUT.decode("utf-8")[:-1]

MD_MATH_RE = re.compile(r"\$`(.+?)`\$")
MD_MATH_DISPLAY_RE = re.compile(r"^`{3}math\s+(.+?)\s+`{3}$", flags=re.M|re.S)

def apply_math(md_str):
    md_str = MD_MATH_RE.sub(repl=lambda obj: math_tex_to_html(obj.group(1), display_mode=False), string=md_str)
    md_str = MD_MATH_DISPLAY_RE.sub(repl=lambda obj: math_tex_to_html(obj.group(1), display_mode=True), string=md_str)
    return md_str

def highlight_code(code, lang):
    lexer = get_lexer_by_name(lang, stripAll=True)
    formatter = HtmlFormatter(linenos=False, cssclass="highlight", lineseparator="<br>")
    return highlight(code, lexer, formatter)

MD_CODE_RE = re.compile(r"^`{3}([a-z]+?)\s+(.+?)\s+`{3}$", flags=re.M|re.S)

def apply_code_highlight(md_str):
    md_str = MD_CODE_RE.sub(repl=lambda obj: highlight_code(obj.group(2), obj.group(1)), string=md_str)
    return md_str

# Variables.

TITLE = "S. Hyeon"

NOTES_PATH          = 'md'
BLOG_PATH           = 'notes'
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
ARTICLE_LIST_PATH   = 'article_list.html'
LIST_HTML_PATH      = 'list.html'
MORE_PATH           = 'more.html'
CATEGORIES_PATH     = 'categories.html'
LANGUAGES_PATH      = 'languages.html'
STYLESHEET_PATH     = 'style.css'
CATEGORY_PATH       = 'category'
LANGUAGE_PATH       = 'language'
KATEX_PATH          = 'katex'
HIGHLIGHT_PATH      = 'highlight.css'
LICENSE             = 'LICENSE_NOTE'
GITHUB_URL          = 'https://github.com/loudcolour/loudcolour.github.io'
RECENT_NOTES_AMOUNT = 5

# Load files.

HEAD_FILE = open(HTML_PATH + '/' + HEAD_PATH, 'r')
HEAD_LOAD = HEAD_FILE.read()
HEAD_FILE.close()

TAIL_FILE = open(HTML_PATH + '/' + TAIL_PATH, 'r')
TAIL_LOAD = TAIL_FILE.read()
TAIL_FILE.close()

ARTICLE_LIST_FILE = open(HTML_PATH + '/' + ARTICLE_LIST_PATH, 'r')
ARTICLE_LIST_LOAD = ARTICLE_LIST_FILE.read()
ARTICLE_LIST_FILE.close()

LIST_HTML_FILE = open(HTML_PATH + '/' + LIST_HTML_PATH, 'r')
LIST_HTML_LOAD = LIST_HTML_FILE.read()
LIST_HTML_FILE.close()

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

        ARTICLE_RAW = open(INPUT_PATH, 'r')
        ARTICLE_MATH_APPLIED = apply_math(ARTICLE_RAW.read())
        ARTICLE_RAW.close()
        ARTICLE_HIGHLIGHT_APPLIED = apply_code_highlight(ARTICLE_MATH_APPLIED)
        
        pandoc_command = ["pandoc", "-f", "gfm", "-t", "html"]

        PARSED = sp.Popen(pandoc_command, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        STDOUT, STDERR = PARSED.communicate(input=ARTICLE_HIGHLIGHT_APPLIED.encode("utf-8"))

        ARTICLE = STDOUT.decode("utf-8")

        if STDERR != b'':
            print(STDERR.decode("utf-8"))
            exit(1)

        REPLACEMENT = BASE_YAML_LOAD[perm].copy()
        REPLACEMENT['mtime_formatted'] = format_date(REPLACEMENT['mtime'])
        REPLACEMENT.update({
            'language_url': "../" + LANGUAGE_PATH + "/" + REPLACEMENT['language'] + HTML_EXT, 
            'category_url': "../" + CATEGORY_PATH + "/" + REPLACEMENT['category'] + HTML_EXT,
            'blame_url': GITHUB_URL + '/blame/master/' + INPUT_PATH,
            'home_url': "../",
            'more_url': "../" + MORE_PATH,
            'issue_url': GITHUB_URL + '/issues/new?title=' + REPLACEMENT['title'],
            'stylesheet': "../" + STYLESHEET_PATH,
            'icons': "../" + ICONS_PATH,
            'katex': "../" + KATEX_PATH,
            'highlight': "../" + HIGHLIGHT_PATH,
            'visibility': "",
            'github_url': GITHUB_URL,
            'license_url': GITHUB_URL + '/blob/master/' + LICENSE,
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)],string=HEAD_LOAD)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)],string=TAIL_LOAD) 

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + ARTICLE + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    def delete_blog_note(perm):
        INPUT_PATH = BLOG_PATH + "/" + perm + HTML_EXT

        if path.isfile(INPUT_PATH):
            remove(INPUT_PATH)
            print(colored("Removed " + INPUT_PATH + ".", "red"))
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

    # Generate index.html, more.html, category pages, and tag pages.

    html_link_lambda = lambda link, content : '<a href="' + link + '">' + content + '</a>'
    html_span_lambda = lambda css_class, content : '<span class="' + css_class + '">' + content + '</span>'
    html_li_lambda = lambda content : '<li>' + content + '</li>'

    line_combine_lambda = lambda li_1, li_2: li_1 + "\n" + li_2

    make_html_list = lambda l : reduce(line_combine_lambda, map(html_li_lambda, l))

    def get_recent_notes(perm_list, note_amount, location):
        notes_perm_title_mdate = [{'perm': perm,
                                   'title': BASE_YAML_LOAD[perm]['title'],
                                   'mtime': BASE_YAML_LOAD[perm]['mtime'],
                                   'category': BASE_YAML_LOAD[perm]['category']} for perm in perm_list]
        notes_perm_title_mdate.sort(key=lambda dic : dic['mtime'], reverse=True)

        link_lambda = lambda dic : location + '/' + BLOG_PATH + '/' + dic['perm'] + HTML_EXT
        category_link_lambda = lambda dic : location + '/' + CATEGORY_PATH + '/' + dic['category'] + HTML_EXT

        dict_to_html_li_lambda = lambda dic : html_li_lambda(
                                        html_span_lambda('category-button', html_link_lambda(category_link_lambda(dic),dic['category']))
                                        + " " + html_link_lambda(link_lambda(dic), dic['title']))

        list_of_recent_notes = notes_perm_title_mdate[:note_amount]
        return reduce(line_combine_lambda, map(dict_to_html_li_lambda, list_of_recent_notes))

    def generate_index():
        INPUT_PATH = README + MD_EXT
        OUTPUT_PATH = INDEX

        ARTICLE_RAW = open(INPUT_PATH, 'r')
        ARTICLE_MATH_APPLIED = apply_math(ARTICLE_RAW.read())
        ARTICLE_RAW.close()
        ARTICLE_HIGHLIGHT_APPLIED = apply_code_highlight(ARTICLE_MATH_APPLIED)

        pandoc_command = ["pandoc", "-f", "gfm", "-t", "html"]

        PARSED = sp.Popen(pandoc_command, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        STDOUT, STDERR = PARSED.communicate(input=ARTICLE_HIGHLIGHT_APPLIED.encode("utf-8"))

        ARTICLE = STDOUT.decode("utf-8")

        if STDERR != b'':
            print(STDERR.decode("utf-8"))
            exit(1)

        REPLACEMENT = {'title': TITLE, 'category': "", 'language': ""}
        REPLACEMENT.update({
            'blame_url': GITHUB_URL + '/blame/master/' + INPUT_PATH,
            'issue_url': GITHUB_URL + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "./",
            'more_url': "./" + MORE_PATH,
            'stylesheet': "./" + STYLESHEET_PATH,
            'icons': "./" + ICONS_PATH,
            'katex': "./" + KATEX_PATH,
            'highlight': "./" + HIGHLIGHT_PATH,
            'visibility': "display: none;",
            'github_url': GITHUB_URL,
            'license_url': GITHUB_URL + '/blob/master/' + LICENSE,
            'list': get_recent_notes(BASE_YAML_LOAD.keys(), RECENT_NOTES_AMOUNT, '.'),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=HEAD_LOAD)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=TAIL_LOAD)

        RECENT_NOTES_FILLED = ""

        with open(HTML_PATH+"/"+RECENT_NOTES_PATH, 'r') as RECENT_NOTES_FILE:
            RECENT_NOTES_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=RECENT_NOTES_FILE.read())

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + ARTICLE + RECENT_NOTES_FILLED + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    def generate_more():
        OUTPUT_PATH = MORE_PATH

        REPLACEMENT = {'title': 'More notes', 'category': "", 'language': ""}
        REPLACEMENT.update({
            'blame_url': '',
            'issue_url': GITHUB_URL + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "./",
            'more_url': "./" + MORE_PATH,
            'stylesheet': "./" + STYLESHEET_PATH,
            'icons': "./" + ICONS_PATH,
            'katex': "./" + KATEX_PATH,
            'highlight': "./" + HIGHLIGHT_PATH,
            'visibility': "display: none;",
            'github_url': GITHUB_URL,
            'license_url': GITHUB_URL + '/blob/master/' + LICENSE,
            'list': get_recent_notes(BASE_YAML_LOAD.keys(), len(BASE_YAML_LOAD), '.'),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=HEAD_LOAD)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=TAIL_LOAD)

        ARTICLE_LIST_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=ARTICLE_LIST_LOAD)

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + ARTICLE_LIST_FILLED + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    generate_index()
    generate_more()

    CATEGORIES_DICT = {}
    LANGUAGES_DICT = {}

    for perm in BASE_YAML_LOAD.keys():
        category_of_perm = BASE_YAML_LOAD[perm]['category']
        
        if not (category_of_perm in CATEGORIES_DICT.keys()):
            CATEGORIES_DICT[category_of_perm] = [perm]
        else:
            CATEGORIES_DICT[category_of_perm].append(perm)
    
    for perm in BASE_YAML_LOAD.keys():
        language_of_perm = BASE_YAML_LOAD[perm]['language']
        
        if not (language_of_perm in LANGUAGES_DICT.keys()):
            LANGUAGES_DICT[language_of_perm] = [perm]
        else:
            LANGUAGES_DICT[language_of_perm].append(perm)

    def generate_category_page():
        OUTPUT_PATH = CATEGORIES_PATH

        REPLACEMENT = {'title': 'Categories', 'category': '', 'language': ''}
        REPLACEMENT.update({
            'blame_url': '',
            'issue_url': GITHUB_URL + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "./",
            'more_url': "./" + MORE_PATH,
            'stylesheet': "./" + STYLESHEET_PATH,
            'icons': "./" + ICONS_PATH,
            'katex': "./" + KATEX_PATH,
            'highlight': "./" + HIGHLIGHT_PATH,
            'visibility': "display: none;",
            'github_url': GITHUB_URL,
            'license_url': GITHUB_URL + '/blob/master/' + LICENSE,
            'list': make_html_list(list(map(lambda key: '<a href="'+CATEGORY_PATH+'/'+key+HTML_EXT+'">'+key+'</a>', CATEGORIES_DICT.keys()))),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=HEAD_LOAD)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=TAIL_LOAD)

        LIST_HTML_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=LIST_HTML_LOAD)

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + LIST_HTML_FILLED + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    def generate_language_page():
        OUTPUT_PATH = LANGUAGES_PATH

        REPLACEMENT = {'title': 'Languages', 'category': '', 'language': ''}
        REPLACEMENT.update({
            'blame_url': '',
            'issue_url': GITHUB_URL + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "./",
            'more_url': "./" + MORE_PATH,
            'stylesheet': "./" + STYLESHEET_PATH,
            'icons': "./" + ICONS_PATH,
            'katex': "./" + KATEX_PATH,
            'highlight': "./" + HIGHLIGHT_PATH,
            'visibility': "display: none;",
            'github_url': GITHUB_URL,
            'license_url': GITHUB_URL + '/blob/master/' + LICENSE,
            'list': make_html_list(list(map(lambda key: '<a href="'+LANGUAGE_PATH+'/'+key+HTML_EXT+'">'+key+'</a>', LANGUAGES_DICT.keys()))),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=HEAD_LOAD)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=TAIL_LOAD)

        LIST_HTML_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=LIST_HTML_LOAD)

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + LIST_HTML_FILLED + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    def generate_category_pages(category):
        OUTPUT_PATH = CATEGORY_PATH + '/' + category + HTML_EXT

        REPLACEMENT = {'title': category, 'category': '', 'language': ''}
        REPLACEMENT.update({
            'blame_url': '',
            'issue_url': GITHUB_URL + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "../",
            'more_url': "../" + MORE_PATH,
            'stylesheet': "../" + STYLESHEET_PATH,
            'icons': "../" + ICONS_PATH,
            'katex': "../" + KATEX_PATH,
            'highlight': "../" + HIGHLIGHT_PATH,
            'visibility': "display: none;",
            'github_url': GITHUB_URL,
            'license_url': GITHUB_URL + '/blob/master/' + LICENSE,
            'list': get_recent_notes(CATEGORIES_DICT[category], len(CATEGORIES_DICT[category]), '..'),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=HEAD_LOAD)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=TAIL_LOAD)

        ARTICLE_LIST_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=ARTICLE_LIST_LOAD)
        CATEGORY_LINK = "<a href='"+ "../" + CATEGORIES_PATH +"'>List of categories</a>"

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + ARTICLE_LIST_FILLED + CATEGORY_LINK + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    def generate_language_pages(language):
        OUTPUT_PATH = LANGUAGE_PATH + '/' + language + HTML_EXT

        REPLACEMENT = {'title': language, 'category': '', 'language': ''}
        REPLACEMENT.update({
            'blame_url': '',
            'issue_url': GITHUB_URL + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "../",
            'more_url': "../" + MORE_PATH,
            'stylesheet': "../" + STYLESHEET_PATH,
            'icons': "../" + ICONS_PATH,
            'katex': "../" + KATEX_PATH,
            'highlight': "../" + HIGHLIGHT_PATH,
            'visibility': "display: none;",
            'github_url': GITHUB_URL,
            'license_url': GITHUB_URL + '/blob/master/' + LICENSE,
            'list': get_recent_notes(LANGUAGES_DICT[language], len(LANGUAGES_DICT[language]), '..'),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=HEAD_LOAD)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=TAIL_LOAD)

        ARTICLE_LIST_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=ARTICLE_LIST_LOAD)
        LANGUAGE_LINK = "<a href='"+ "../" + LANGUAGES_PATH +"'>List of languages</a>"

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + ARTICLE_LIST_FILLED + LANGUAGE_LINK + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    generate_category_page()
    generate_language_page()

    for category in CATEGORIES_DICT.keys():
        generate_category_pages(category)
    
    for language in LANGUAGES_DICT.keys():
        generate_language_pages(language)

    # Update list.yaml.

    BASE_YAML_FILE = yaml.safe_dump(BASE_YAML_LOAD)

    with open(LIST_PATH, 'w') as YAML_FILE:
        YAML_FILE.write(BASE_YAML_FILE)
        if not regenerate_mode:
            print(colored("Total " + str(len_modified+len_added+len_removed) + " change(s) applied.", 'green'))

else:
    print(colored("There's nothing changed.", "green"))
