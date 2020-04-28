class format_HTML():
    def __init__(self):
        self.f = lambda tag : (lambda content : ('<' + tag + '>' + content + '</' + tag + '>'))
        li = self.f('li')
        span = self.f('span')
        ruby = self.f('ruby')
