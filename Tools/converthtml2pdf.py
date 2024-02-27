# convert html to pdf

import pdfkit
import os
import sys

if len(sys.argv) > 1:
    file = sys.argv[1]
    if os.path.exists(file):
        pdfkit.from_file(file, 'output.pdf')
        print('PDF created successfully.')
    else:
        print('File does not exist')
else:
    print('Usage: python converthtml2pdf.py <file>')