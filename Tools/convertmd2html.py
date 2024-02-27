# Note: Can't convert code block of markdown to html so write md file without any code block
import markdown
import webbrowser
import os
import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()
            html = markdown.markdown(content, extensions=['codehilite'])
            with open('preview.html', 'w') as f:
                f.write(html)
            webbrowser.open('preview.html')
    else:
        print('File does not exist')
else:
    print('Usage: python convertmd2html.py <file>')
