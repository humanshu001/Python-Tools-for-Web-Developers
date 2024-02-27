# convert the image to webp format

import os
import sys
from PIL import Image

if len(sys.argv) > 1:
    file = sys.argv[1]
    if os.path.exists(file):
        img = Image.open(file)
        filename, extension = os.path.splitext(file)
        output_file = f"{filename}.webp"
        img.save(output_file, 'webp')
    else:
        print('File does not exist')
else:
    print('Usage: python convert2webp.py <file>')