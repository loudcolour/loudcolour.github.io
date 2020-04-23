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

tz = tzlocal.get_localzone()

# Modes.

debug_mode = False
regenerate_mode = False

if 'debug' in argv:
    debug_mode = True
    print(colored("Debug mode is ON.", "red"))

if 'regenerate' in argv:
    regenerate_mode = True
    print(colored("Regenerating all notes.", "yellow"))

# Regex dictionary

re_dict = {
    'math_display': re.compile(r"^(\${2}\s+.+?\s+\${2})$", flags=re.M|re.S),
    'math': re.compile(r"(\$.+?\$)"),
    'code': re.compile(r"^`{3}([a-z]+?)\s+(.+?)\s+`{3}$", flags=re.M|re.S),
}

# Global functions.

def debug_message(name, value):
    print(colored("Debug message, "+name+": "+str(value), "grey"))

format_date = lambda ts, df : datetime.fromtimestamp(ts, tz).strftime(df)
codehl = lambda code, lang : highlight(code, get_lexer_by_name(lang, stripAll=True), HtmlFormatter(linenos=False, cssclass="highlight", lineseparator="<br>"))
md_to_html_codehl = lambda md_str : re_dict['code'].sub(repl=lambda obj: codehl(obj.group(2), obj.group(1)), string=md_str)

# Load settings.yaml

settings_f = open("settings.yaml", 'r')
settings = yaml.safe_load(settings_f.read())
settings_f.close()

# Load files.

head_f = open(settings['dir_path']['html_part'] + '/' + settings['path']['html_part']['head'], 'r')
head_l = head_f.read()
head_f.close()

tail_f = open(settings['dir_path']['html_part'] + '/' + settings['path']['html_part']['tail'], 'r')
tail_l = tail_f.read()
tail_f.close()

note_list_f = open(settings['dir_path']['html_part'] + '/' + settings['path']['html_part']['note_list'], 'r')
note_list_l = note_list_f.read()
note_list_f.close()

html_part_list_f = open(settings['dir_path']['html_part'] + '/' + settings['path']['html_part']['list'], 'r')
html_part_list_l = html_part_list_f.read()
html_part_list_f.close()

note_list_yaml_f = open(settings['path']['note_list_yaml'], 'r')
note_list_yaml_l = yaml.safe_load(note_list_yaml_f)
note_list_yaml_f.close()

if debug_mode:
    debug_message("note_list_yaml_l", note_list_yaml_l)

new_list_perm = list(filter(lambda s : s[-len(settings['ext']['md']):] == settings['ext']['md'], listdir(path=settings['dir_path']['md'])))
new_list_perm_mtime = list(map(lambda s : {'perm' : s[:-len(settings['ext']['md'])], 'mtime': int(path.getmtime(settings['dir_path']['md']+"/"+s))}, new_list_perm))
new_list_perm_mtime.sort(key=lambda dic : dic['mtime'])

old_list_perm = list(note_list_yaml_l.keys())
old_list_perm_mtime = [{'perm': perm, 'mtime': note_list_yaml_l[perm]['mtime']} for perm in old_list_perm]
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
            modified_date = format_date(dic['mtime'], '%Y-%m-%dT%H:%M:%S%z')
            print(colored(" - " + dic["perm"] + settings['ext']['md'] + " at " + modified_date,"yellow"))
        print("")
    if len_added != 0:
        print(colored(str(len_added) + " ADDITION(S):", "green"))
        for dic in added_perm_mtime:
            added_date = format_date(dic['mtime'], '%Y-%m-%dT%H:%M:%S%z')
            print(colored(" - " + dic["perm"] + settings['ext']['md'] + " at " + added_date,"green"))
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
            print(colored(" - " + note["perm"] + settings['ext']['md'], "red"))
        print("")

    # Get new tag data.

    def get_meta_from_md(perm):
        INPUT_PATH = settings['dir_path']['md'] + "/" + perm + settings['ext']['md']
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
        BASE_YAML_LOAD[perm] = note_list_yaml_l[perm]

    for dic in modified_or_added_perm_mtime:
        base_dic = get_meta_from_md(dic['perm'])
        base_dic['mtime'] = dic['mtime']
        BASE_YAML_LOAD[dic['perm']] = base_dic
        BASE_YAML_LOAD_perm.append(dic['perm'])

    if debug_mode:
        debug_message("BASE_YAML_LOAD", BASE_YAML_LOAD)
    
    # Generate or delete notes.

    def generate_blog_note(perm):
        INPUT_PATH = settings['dir_path']['md'] + "/" + perm + settings['ext']['md']
        OUTPUT_PATH = settings['dir_path']['notes'] + "/" + perm + settings['ext']['html']

        ARTICLE_RAW = open(INPUT_PATH, 'r')
        ARTICLE_HIGHLIGHT_APPLIED = md_to_html_codehl(ARTICLE_RAW.read())
        ARTICLE_RAW.close()

        MATH_DISPLAY_PH = "{{%%%%}}"
        MATH_PH = "{{%%}}"

        T_MATH_DISPLAY = re_dict['math_display'].findall(string=ARTICLE_HIGHLIGHT_APPLIED)
        MATH_SAFE = re_dict['math_display'].sub(repl=MATH_DISPLAY_PH, string=ARTICLE_HIGHLIGHT_APPLIED)
        T_MATH = re_dict['math'].findall(string=MATH_SAFE)
        MATH_SAFE = re_dict['math'].sub(repl=MATH_PH, string=MATH_SAFE)

        pandoc_command = ["pandoc", "-f", "gfm", "-t", "html"]

        PARSED = sp.Popen(pandoc_command, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        STDOUT, STDERR = PARSED.communicate(input=MATH_SAFE.encode("utf-8"))

        ARTICLE = STDOUT.decode("utf-8")

        for math in T_MATH_DISPLAY:
            ARTICLE = ARTICLE.replace(MATH_DISPLAY_PH, math.replace('&', '&amp;')
                                                           .replace('<', '&lt;')
                                                           .replace('>', '&gt;'), 1)
        for math in T_MATH:
            ARTICLE = ARTICLE.replace(MATH_PH, math.replace('&', '&amp;')
                                                   .replace('<', '&lt;')
                                                   .replace('>', '&gt;'), 1)

        if STDERR != b'':
            print(STDERR.decode("utf-8"))
            exit(1)

        REPLACEMENT = BASE_YAML_LOAD[perm].copy()
        REPLACEMENT['mtime_formatted'] = format_date(REPLACEMENT['mtime'], '%Y-%m-%dT%H:%M:%S%z')
        REPLACEMENT.update({
            'language_url': "../" + settings['dir_path']['language'] + "/" + REPLACEMENT['language'] + settings['ext']['html'], 
            'category_url': "../" + settings['dir_path']['category'] + "/" + REPLACEMENT['category'] + settings['ext']['html'],
            'blame_url': settings['github_repo'] + '/blame/master/' + INPUT_PATH,
            'home_url': "../",
            'more_url': "../" + settings['path']['more'],
            'issue_url': settings['github_repo'] + '/issues/new?title=' + REPLACEMENT['title'],
            'stylesheet': "../" + settings['path']['stylesheet'],
            'icons': "../" + settings['dir_path']['icons'],
            'katex': "../" + settings['dir_path']['katex'],
            'highlight': "../" + settings['path']['highlight'],
            'visibility': "",
            'github_url': settings['github_repo'],
            'license_url': settings['github_repo'] + '/blob/master/' + settings['license']['notes'],
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)],string=head_l)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)],string=tail_l) 

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + ARTICLE + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    def delete_blog_note(perm):
        INPUT_PATH = settings['dir_path']['notes'] + "/" + perm + settings['ext']['html']

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

        link_lambda = lambda dic : location + '/' + settings['dir_path']['notes'] + '/' + dic['perm'] + settings['ext']['html']
        category_link_lambda = lambda dic : location + '/' + settings['dir_path']['category'] + '/' + dic['category'] + settings['ext']['html']

        dict_to_html_li_lambda = lambda dic : html_li_lambda(
                                        html_span_lambda('modified-date', format_date(dic['mtime'], '%Y-%m-%d'))
                                        + " " + html_span_lambda('category-button', html_link_lambda(category_link_lambda(dic),dic['category']))
                                        + " " + html_link_lambda(link_lambda(dic), dic['title']))

        list_of_recent_notes = notes_perm_title_mdate[:note_amount]
        return reduce(line_combine_lambda, map(dict_to_html_li_lambda, list_of_recent_notes))

    def generate_index():
        INPUT_PATH = settings['path']['readme']
        OUTPUT_PATH = settings['path']['index']

        ARTICLE_RAW = open(INPUT_PATH, 'r')
        ARTICLE_HIGHLIGHT_APPLIED = md_to_html_codehl(ARTICLE_RAW.read())
        ARTICLE_RAW.close()

        MATH_DISPLAY_PH = "{{%%%%}}"
        MATH_PH = "{{%%}}"

        T_MATH_DISPLAY = re_dict['math_display'].findall(string=ARTICLE_HIGHLIGHT_APPLIED)
        MATH_SAFE = re_dict['math_display'].sub(repl=MATH_DISPLAY_PH, string=ARTICLE_HIGHLIGHT_APPLIED)
        T_MATH = re_dict['math'].findall(string=MATH_SAFE)
        MATH_SAFE = re_dict['math'].sub(repl=MATH_PH, string=MATH_SAFE)

        pandoc_command = ["pandoc", "-f", "gfm", "-t", "html"]

        PARSED = sp.Popen(pandoc_command, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        STDOUT, STDERR = PARSED.communicate(input=MATH_SAFE.encode("utf-8"))

        ARTICLE = STDOUT.decode("utf-8")

        for math in T_MATH_DISPLAY:
            ARTICLE = ARTICLE.replace(MATH_DISPLAY_PH, math, 1)
        for math in T_MATH:
            ARTICLE = ARTICLE.replace(MATH_PH, math, 1)

        if STDERR != b'':
            print(STDERR.decode("utf-8"))
            exit(1)

        REPLACEMENT = {'title': settings['title'], 'category': "", 'language': ""}
        REPLACEMENT.update({
            'blame_url': settings['github_repo'] + '/blame/master/' + INPUT_PATH,
            'issue_url': settings['github_repo'] + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "./",
            'more_url': "./" + settings['path']['more'],
            'stylesheet': "./" + settings['path']['stylesheet'],
            'icons': "./" + settings['dir_path']['icons'],
            'katex': "./" + settings['dir_path']['katex'],
            'highlight': "./" + settings['path']['highlight'],
            'visibility': "display: none;",
            'github_url': settings['github_repo'],
            'license_url': settings['github_repo'] + '/blob/master/' + settings['license']['notes'],
            'list': get_recent_notes(BASE_YAML_LOAD.keys(), settings['recent_notes_amount'], '.'),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=head_l)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=tail_l)

        RECENT_NOTES_FILLED = ""

        with open(settings['dir_path']['html_part']+"/"+settings['path']['html_part']['recent_notes'], 'r') as RECENT_NOTES_FILE:
            RECENT_NOTES_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=RECENT_NOTES_FILE.read())

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + ARTICLE + RECENT_NOTES_FILLED + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    def generate_more():
        OUTPUT_PATH = settings['path']['more']

        REPLACEMENT = {'title': 'More notes', 'category': "", 'language': ""}
        REPLACEMENT.update({
            'blame_url': '',
            'issue_url': settings['github_repo'] + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "./",
            'more_url': "./" + settings['path']['more'],
            'stylesheet': "./" + settings['path']['stylesheet'],
            'icons': "./" + settings['dir_path']['icons'],
            'katex': "./" + settings['dir_path']['katex'],
            'highlight': "./" + settings['path']['highlight'],
            'visibility': "display: none;",
            'github_url': settings['github_repo'],
            'license_url': settings['github_repo'] + '/blob/master/' + settings['license']['notes'],
            'list': get_recent_notes(BASE_YAML_LOAD.keys(), len(BASE_YAML_LOAD), '.'),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=head_l)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=tail_l)

        ARTICLE_LIST_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=note_list_l)

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
        OUTPUT_PATH = settings['path']['categories']

        REPLACEMENT = {'title': 'Categories', 'category': '', 'language': ''}
        REPLACEMENT.update({
            'blame_url': '',
            'issue_url': settings['github_repo'] + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "./",
            'more_url': "./" + settings['path']['more'],
            'stylesheet': "./" + settings['path']['stylesheet'],
            'icons': "./" + settings['dir_path']['icons'],
            'katex': "./" + settings['dir_path']['katex'],
            'highlight': "./" + settings['path']['highlight'],
            'visibility': "display: none;",
            'github_url': settings['github_repo'],
            'license_url': settings['github_repo'] + '/blob/master/' + settings['license']['notes'],
            'list': make_html_list(list(map(lambda key: '<a href="'+settings['dir_path']['category']+'/'+key+settings['ext']['html']+'">'+key+'</a>', CATEGORIES_DICT.keys()))),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=head_l)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=tail_l)

        LIST_HTML_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=html_part_list_l)

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + LIST_HTML_FILLED + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    def generate_language_page():
        OUTPUT_PATH = settings['path']['languages']

        REPLACEMENT = {'title': 'Languages', 'category': '', 'language': ''}
        REPLACEMENT.update({
            'blame_url': '',
            'issue_url': settings['github_repo'] + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "./",
            'more_url': "./" + settings['path']['more'],
            'stylesheet': "./" + settings['path']['stylesheet'],
            'icons': "./" + settings['dir_path']['icons'],
            'katex': "./" + settings['dir_path']['katex'],
            'highlight': "./" + settings['path']['highlight'],
            'visibility': "display: none;",
            'github_url': settings['github_repo'],
            'license_url': settings['github_repo'] + '/blob/master/' + settings['license']['notes'],
            'list': make_html_list(list(map(lambda key: '<a href="'+settings['dir_path']['language']+'/'+key+settings['ext']['html']+'">'+key+'</a>', LANGUAGES_DICT.keys()))),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=head_l)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=tail_l)

        LIST_HTML_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=html_part_list_l)

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + LIST_HTML_FILLED + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    def generate_category_pages(category):
        OUTPUT_PATH = settings['dir_path']['category'] + '/' + category + settings['ext']['html']

        REPLACEMENT = {'title': category, 'category': '', 'language': ''}
        REPLACEMENT.update({
            'blame_url': '',
            'issue_url': settings['github_repo'] + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "../",
            'more_url': "../" + settings['path']['more'],
            'stylesheet': "../" + settings['path']['stylesheet'],
            'icons': "../" + settings['dir_path']['icons'],
            'katex': "../" + settings['dir_path']['katex'],
            'highlight': "../" + settings['path']['highlight'],
            'visibility': "display: none;",
            'github_url': settings['github_repo'],
            'license_url': settings['github_repo'] + '/blob/master/' + settings['license']['notes'],
            'list': get_recent_notes(CATEGORIES_DICT[category], len(CATEGORIES_DICT[category]), '..'),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=head_l)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=tail_l)

        ARTICLE_LIST_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=note_list_l)
        CATEGORY_LINK = "<a href='"+ "../" + settings['path']['categories'] +"'>List of categories</a>"

        with open(OUTPUT_PATH, 'w') as BLOG_FILE:
            BLOG_FILE.write(HEAD_FILLED + ARTICLE_LIST_FILLED + CATEGORY_LINK + TAIL_FILLED)
            print(colored("Generated " + OUTPUT_PATH, "green"))

    def generate_language_pages(language):
        OUTPUT_PATH = settings['dir_path']['language'] + '/' + language + settings['ext']['html']

        REPLACEMENT = {'title': language, 'category': '', 'language': ''}
        REPLACEMENT.update({
            'blame_url': '',
            'issue_url': settings['github_repo'] + '/issues/new',
            'category_url': "",
            'language_url': "",
            'mtime_formatted': "",
            'home_url': "../",
            'more_url': "../" + settings['path']['more'],
            'stylesheet': "../" + settings['path']['stylesheet'],
            'icons': "../" + settings['dir_path']['icons'],
            'katex': "../" + settings['dir_path']['katex'],
            'highlight': "../" + settings['path']['highlight'],
            'visibility': "display: none;",
            'github_url': settings['github_repo'],
            'license_url': settings['github_repo'] + '/blob/master/' + settings['license']['notes'],
            'list': get_recent_notes(LANGUAGES_DICT[language], len(LANGUAGES_DICT[language]), '..'),
        })

        REPLACE_ON_HTML = re.compile(r'{% (\S+?) %}')

        HEAD_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=head_l)
        TAIL_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=tail_l)

        ARTICLE_LIST_FILLED = REPLACE_ON_HTML.sub(repl=lambda obj: REPLACEMENT[obj.group(1)], string=note_list_l)
        LANGUAGE_LINK = "<a href='"+ "../" + settings['path']['languages'] +"'>List of languages</a>"

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

    with open(settings['path']['note_list_yaml'], 'w') as note_list_yaml_f:
        note_list_yaml_f.write(BASE_YAML_FILE)
        if not regenerate_mode:
            print(colored("Total " + str(len_modified+len_added+len_removed) + " change(s) applied.", 'green'))

else:
    print(colored("There's nothing changed.", "green"))
