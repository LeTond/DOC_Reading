"""
Алгоритм, отвечающий за конвертацию документов формата .doc в формат .docx через libreoffice
"""
import glob
import os
import shutil
import subprocess


def docx_ct(root, path):
    current_path = root + path
    os.chdir(current_path)
    new_current_path = current_path + 'copy'
    os.mkdir(new_current_path)
    # for filename in os.walk(path=path):
    for filename in glob.glob("**/*.doc", recursive=True):
        # if filename.endswith('.doc'):
        subprocess.call(['soffice', '--headless', '--convert-to', 'docx', filename])
    for filename in glob.glob("**/*.odt", recursive=True):
        # if filename.endswith('.odt'):
        subprocess.call(['soffice', '--headless', '--convert-to', 'docx', filename])
    for filename in glob.glob("**/*.rtf", recursive=True):
        # if filename.endswith('.rtf'):
        subprocess.call(['soffice', '--headless', '--convert-to', 'docx', filename])

    # copy files in docx format in to new directory
    for directs, direct, files in os.walk(current_path):
        for file in files:
            if file.endswith(".docx"):
                shutil.copy(os.path.join(directs, file), new_current_path)




