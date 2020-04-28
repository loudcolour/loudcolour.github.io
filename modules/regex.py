import re

re_dict = {
    'math_display': re.compile(r"^(\${2}\s+.+?\s+\${2})$", flags=re.M|re.S),
    'math': re.compile(r"(\$.+?\$)"),
    'code': re.compile(r"^`{3}([a-z]+?)\s+(.+?)\s+`{3}$", flags=re.M|re.S),
    'japanese_exception': re.compile(r"([^\n]{2})\n([^\n])"),
    'html_repl': re.compile(r'{% (\S+?) %}'),
    'ruby': re.compile(r'\[\[(.+?)\|(.+?)\]\]'),
    'jump_to': re.compile(r'<h([1-6]) id="(.+?)">(.+?)<\/h[1-6]>'),
}
