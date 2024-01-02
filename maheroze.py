import shutil
import os

def backup(source_path, destination_path):
    print(f"Backing up files from {source_path} to {destination_path}")
    if not os.path.exists(source_path):
        print("Source path does not exist.")
        return
    os.makedirs(destination_path, exist_ok=True)

    try:
        
        shutil.copytree(source_path, os.path.join(destination_path, os.path.basename(source_path)))
        print("Backup completed successfully!")
    except Exception as e:
        print(f"An error occurred during backup: {e}")
source_path = '......path to your source files..........'
destination_path = '........path to your backup destination..............'
backup(source_path, destination_path)
