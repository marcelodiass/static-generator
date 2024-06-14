import os
import shutil
from copy_dir import copy_files_recursive

dir_path_public = "./public"
dir_path_static = "./static"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying static directory to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
        
    return
    
if __name__ == "__main__":
    main()
