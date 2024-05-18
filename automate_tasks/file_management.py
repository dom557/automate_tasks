import os
import shutil

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def delete_directory(path):
    shutil.rmtree(path)

def copy_file(src, dest):
    shutil.copy2(src, dest)

def move_file(src, dest):
    shutil.move(src, dest)
