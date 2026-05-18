import os, re  
repo_root = os.getcwd()  
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')  
allowed_paths = ['docs/screenshots', 'static/img/crown.png']  
all_images = []  
for root, dirs, files in os.walk(repo_root):  
    if '.git' in dirs: dirs.remove('.git')  
    if 'venv' in dirs: dirs.remove('venv')  
    if 'staticfiles' in dirs: dirs.remove('staticfiles')  
    for file in files:  
        if file.lower().endswith(image_extensions):  
            all_images.append(os.path.relpath(os.path.join(root, file), repo_root))  
outside_images = []  
for img in all_images:  
    normalized_img = img.replace('\\\\', '/')  
    if not (normalized_img.startswith('docs/screenshots/') or normalized_img == 'static/img/crown.png'):  
        outside_images.append(img)  
md_files = []  
for root, dirs, files in os.walk(repo_root):  
    if '.git' in dirs: dirs.remove('.git')  
    if 'venv' in dirs: dirs.remove('venv')  
    for file in files:  
        if file.lower().endswith('.md'):  
            md_files.append(os.path.join(root, file))  
broken_refs = []  
checked_count = 0  
for md_path in md_files:  
    with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:  
        content = f.read()  
    links = re.findall(r'^!\[.*?\]\((.*?)\)', content, re.MULTILINE)  
    links += re.findall(r'^!\[.*?\]:\s*(.*)', content, re.MULTILINE)  
