# Static Site Generator

A Python-based static site generator that converts Markdown files into a fully-structured HTML website. It reads your content and a single HTML template, then outputs a ready-to-deploy static site.

## Live Demo

Visit the deployed site: [https://avelarj.github.io/Static-Site-Generator/](https://avelarj.github.io/Static-Site-Generator/)

## Features

- Converts Markdown files to HTML pages recursively
- Supports headings, paragraphs, bold/italic text, inline code, links, images, blockquotes, ordered and unordered lists, and fenced code blocks
- Uses a single `template.html` to give every page a consistent layout
- Copies static assets (CSS, images, etc.) to the output directory automatically
- Adjustable base path for deployment to subdirectories (e.g., GitHub Pages)
       
  - ## Project Structure
       
    - ```
      .
      ├── content/          # Your Markdown source files go here
      ├── static/           # Static assets (CSS, images, fonts, etc.)
      ├── src/              # Python source code
      │   ├── main.py           # Entry point
      │   ├── generate_page.py  # Page generation logic
      │   ├── markdown_to_html.py   # Markdown → HTML conversion
      │   ├── markdown_utilities.py # Inline Markdown parsing
      │   ├── block_utilities.py    # Block-level type detection
      │   ├── htmlnode.py           # HTML node classes
      │   └── textnode.py           # Text node classes
      ├── docs/             # Generated output (served by GitHub Pages)
      ├── template.html     # HTML template used for every page
      ├── main.sh           # Run locally with a dev server
      ├── build.sh          # Build for GitHub Pages deployment
      └── test.sh           # Run all unit tests
      ```

## Requirements

  - Python 3.x
  - [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) (`pip install beautifulsoup4`)
           
      - ## How to Use
           
      - ### 1. Clone the repository
           
        - ```bash
          git clone https://github.com/AvelarJ/Static-Site-Generator.git
          cd Static-Site-Generator
          ```

      - ### 2. Install dependencies

          ```bash
          pip install beautifulsoup4
          ```

      - ### 3. Add your content

          Place your Markdown (`.md`) files inside the `content/` folder. Each file must include at least one `# H1` heading, which is used as the page title. You can organise content in subdirectories and they will be mirrored in the output.

          Place any CSS, images, or other static files inside the `static/` folder.

      - ### 4. Customise the template

          Edit `template.html` to change the overall look of every page. The two special placeholders are:

          - `{{ Title }}` — replaced with the `# H1` heading of each Markdown file
          - `{{ Content }}` — replaced with the full HTML body converted from Markdown
               
      - ### 5. Build and preview locally
               
              - ```bash
                bash main.sh
                ```

                This generates the site into the `docs/` folder and starts a local HTTP server at [http://localhost:8888](http://localhost:8888).

      - ### 6. Build for deployment (GitHub Pages)

                ```bash
                bash build.sh
                ```

                This generates the site with `/Static-Site-Generator/` as the base path, ready for GitHub Pages hosting.

                ## Running the Tests

                ```bash
                bash test.sh
                ```

                This runs all unit tests found in the `src/` directory using Python's built-in `unittest` framework.

                ## Supported Markdown Syntax

                | Element | Syntax |
                |---|---|
                | Heading | `# H1` through `###### H6` |
                | Bold | `**bold text**` |
                | Italic | `*italic text*` |
                | Inline code | `` `code` `` |
                | Link | `[text](url)` |
                | Image | `![alt](url)` |
                | Blockquote | `> quote` |
                | Unordered list | `- item` |
                | Ordered list | `1. item` |
                | Code block | ` ``` ` fenced block |
