PATH = os.path.dirname(os.path.abspath(__file__))
THEME_PATH = os.path.join(PATH, 'theme')
HTML = ['index.html', 'iphone-theme.html']
SCSS_PATH = os.path.join(THEME_PATH, 'css/style.scss')
OUTPUT_PATH = os.path.join(PATH, 'output')

SCSS_EXECUTABLE = 'scss --style expanded %(input)s %(output)s'

def template(template, context):
    """
    Process the given `template` using the given `context`
    and return a string containing the output.
    """
    pass

def compile(input):
    """
    Compile the given SCSS and return a string containing
    the output.
    """
    pass

def main():
    css = compile(SCSS_PATH)

    for html in HTML:
        input = os.path.join(PATH, html)
        output = template(input, {
            'css': css
        })
        save(html, output)
