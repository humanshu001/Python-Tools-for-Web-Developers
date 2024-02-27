import sys
import base64
import pyperclip

if len(sys.argv) > 1:
    file = sys.argv[1]
    with open(file, 'rb') as f:
        content = f.read()
        base64_content = base64.b64encode(content)
        base64_string = base64_content.decode('utf-8')
        pyperclip.copy(base64_string)
        print('Base64 string copied to clipboard.')
else:
    print('Usage: python convertimg2base64.py <file>')


    