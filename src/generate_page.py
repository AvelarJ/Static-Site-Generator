import os
from pathlib import Path

from markdown_to_html import markdown_to_html_node


def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None
    
    
def generate_page(from_path, template_path, dest_path):
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
    final_template = ''
    for line in template.splitlines():
        if "{{ Title }}" in line:
            #print('Found Title in template')
            line = line.replace("{{ Title }}", title)
            final_template += "".join(line)
        elif "{{ Content }}" in line:
            #print('Found Content in template')
            line = line.replace("{{ Content }}", full_html)
            final_template += "".join(line)
        else:
            final_template += "".join(line)
            
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(final_template)
        
        
def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_page_recursive(from_path, template_path, dest_path)
    
        

"""if __name__ == "__main__":
    f_path = './content/index.md'
    t_path = './template.html'
    d_path = './public/index.html'
    
    generate_page(f_path, t_path, d_path)"""