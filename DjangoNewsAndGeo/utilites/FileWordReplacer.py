import os
import re

def replace_in_file(file_path, pattern, replacement):
    if file_path.endswith(".py"):
        with open(file_path, 'r') as file:
            content = file.read()
    
        new_content = re.sub(pattern, replacement, content)
    
        with open(file_path, 'w') as file:
            file.write(new_content)

def replace_in_directory(directory_path, pattern, replacement):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            replace_in_file(file_path, pattern, replacement)

# Заданный шаблон и замены
patterns = [
    (r'ugettext', 'gettext'),
    (r'ugettext_lazy', 'gettext_lazy'),
    (r'ungettext_lazy', 'ngettext_lazy'),
    (r'force_text', 'force_str')
]

# Папка, в которой нужно выполнить замены
directory_path = 'C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python39_64\Lib\site-packages\djeym'

# Выполняем замены для каждого шаблона
for pattern, replacement in patterns:
    replace_in_directory(directory_path, pattern, replacement)

print("Замены выполнены")
input()
