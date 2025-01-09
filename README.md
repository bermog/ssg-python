# Static Site Generator

SSG that converts markdown files into HTML. Developed and tested in
Python `3.12.8`.


## Overview

The `main.sh` script will run `main.py` and serve the public directory contents
in `localhost:8888`.

Sample content is provided, we can break it down into:

- **static**: The CSS, images and other assets used in your website.
- **content**: The markdown files that will be converted to HTML pages.
- **template.html**: HTML that will wrap your converted content.
- **public**: The program will generate (or overwrite) this directory in the
project root with the final website files.

At least one main markdown title is required (e.g. "# My Title"). This will be
inserted into the `{{ Title }}` element of the template.

The rest of your converted content will be inserted into the `{{ Content }}`
element of the template.


## Usage

1. Edit the contents of `static`, `content` and `template.html` as you see fit.
2. Run `main.sh`, preview your website at `localhost:8888` (Ctrl-C to stop the
HTTP server).
3. Your final website files will be in the `public` directory.
