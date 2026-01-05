import os
from pathlib import Path
from bs4 import BeautifulSoup

from markdown_to_html import markdown_to_html_node


def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
        else:
            raise Exception('Title not found')
    return None
    
    
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    #Open from_path markdown file
    try:
        with open(from_path, 'r', encoding='utf-8') as md_file:
            markdown = md_file.read()
            print(f'File {from_path} read successfully')
            
    except FileNotFoundError:
        print(f"Error: The file '{from_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    #Open template_path HTML file
    try:
        with open(template_path, 'r', encoding='utf-8') as template_file:
            template = template_file.read()
            print(f'File {template_path} read successfully')
            
    except FileNotFoundError:
        print(f"Error: The file '{template_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    #Convert the MD string to an HTML node
    full_html = markdown_to_html_node(markdown).to_html()
    
    #Extract title
    title = extract_title(markdown)
    
    #Replace Title and Content in template
    place_template = ''
    for line in template.splitlines():
        if "{{ Title }}" in line:
            #print('Found Title in template')
            line = line.replace("{{ Title }}", title)
            place_template += "".join(line)
        if "{{ Content }}" in line:
            #print('Found Content in template')
            line = line.replace("{{ Content }}", full_html)
            place_template += "".join(line)
        else:
            place_template += "".join(line)
            
    soup = BeautifulSoup(place_template, "html.parser")
            
    if basepath == '/': #Couldn't get working without skipping basepath replacement
        final_template = place_template
    else:   #Replace any links to start with basepath (defaults to /)
        for tag in soup.find_all(href=True):
            if tag["href"].startswith("/"):
                tag["href"] = basepath + tag["href"][1:]

        for tag in soup.find_all(src=True):
            if tag["src"].startswith("/"):
                tag["src"] = basepath + tag["src"][1:]

        final_template = str(soup)
        
        """ OG Attempt, was still exclusive
        final_template = ''
        for line in place_template.splitlines():
            print(f'\nLine = {line}\n')
            if "href=\"/" in line:
                line = line.replace("href=\"/", f"href=\"{basepath}")
                final_template += "".join(line)
            if "src=\"/" in line:
                line = line.replace("src=\"/", f"src=\"{basepath}")
                final_template += "".join(line)"""
    
            
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(final_template)
        
        
def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_page_recursive(from_path, template_path, dest_path, basepath)
    
        

"""if __name__ == "__main__":
    f_path = './content/index.md'
    t_path = './template.html'
    d_path = './public/index.html'
    
    generate_page(f_path, t_path, d_path)"""