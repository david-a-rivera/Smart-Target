import os
import json
import zipfile
import shutil

# Define selected folders
selected_folders = ['scripts', 'styles', 'assets', 'templates', 'lang', 'packs', 'storage']

def add_file_dist(file_name, ):
    shutil.copyfile(file_name, 'dist/' + file_name)

def create_dist_folder():
    if not os.path.exists('dist'):
        os.makedirs('dist')

def add_folder_to_zip(zip_file, folder):
    if os.path.exists(folder):
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder)
                zip_file.write(file_path, os.path.join(folder, relative_path))
    else:
        print(f"Warning: {folder} is missing. Skipping.")

def create_zip(folders):
    zip_filename = f'dist/module.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write('module.json')
        zip_file.write('LICENSE')

        for folder in folders:
            add_folder_to_zip(zip_file, folder)

    print(f"Zip file '{zip_filename}' created successfully.")

def main():    
    create_dist_folder()

    add_file_dist("module.json")

    create_zip(selected_folders)

if __name__ == "__main__":
    main()