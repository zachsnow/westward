PATH = os.path.dirname(os.path.abspath(__file__))
THEME_PATH = os.path.join(PATH, 'theme')
HTML = ['index.html', 'iphone-theme.html']
SCSS_PATH = os.path.join(THEME_PATH, 'css/style.scss')
OUTPUT_PATH = os.path.join(PATH, 'output')

SCSS_EXECUTABLE = 'scss --style expanded %(input)s %(output)s'

def compile(input):
    
def main():
    # Step 1: compile SCSS.
    css = compile(SCSS_PATH)

    # Step 2: Template HTML, once for main theme and once for iphoe.
    for html in HTML:
        input = os.path.join(PATH, html)
        output = template(input, {
            'css': css
        })
        save(html, output)


# Step 3.
