# Basic Tools for Web Developers
- These tools are made in Python and are used to make the life of a web developer easier, like converting image files to webp format, markdown to html, etc.

## Tools

### 1. [Markdown to HTML](Tools/convertmd2html.py)
- This tool is used to convert markdown files to html files. It uses the `markdown` library to convert the markdown to html.
> **Note:** Code blocks are not supported in this tool.

### 2. [Image to WebP](Tools/convertimg2webp.py)
- This tool is used to convert image files to webp format. It uses the `PIL` library to convert the image to webp.
> **Note:** This tool only supports `.jpg` and `.png` files.

### 3. [Image to Base64](Tools/convertimg2base64.py)
- This tool is used to convert image files to base64 format and copies it to your clipboard. It uses the `base64` library to convert the image to base64.
> **Note:** This tool only supports `.jpg` and `.png` files.

### 4. [HTML to PDF](Tools/converthtml2pdf.py)
- This tool is used to convert html files to pdf files. It uses the `pdfkit` library to convert the html to pdf.
> **Note:** This tool only supports `.html` files.