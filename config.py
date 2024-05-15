import os
import shutil

def duplicate_project(src_path, dest_path):
    # Create the new project directory
    if os.path.exists(dest_path):
        print(f"Le répertoire de destination '{dest_path}' existe déjà. Veuillez le supprimer ou le renommer avant de continuer.")
    else:
        os.makedirs(dest_path)

    # Copy all files and directories except Library and Logs
    for root, dirs, files in os.walk(src_path):
        if 'Library' not in root and 'Logs' not in root:
            for file in files:
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_path, os.path.relpath(src_file, src_path))
                if os.path.exists(dest_file):
                    print(f"Le répertoire de destination '{dest_file}' existe déjà. Veuillez le supprimer ou le renommer avant de continuer.")
                else:
                    os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                shutil.copy2(src_file, dest_file)

    # Copy ProjectSettings if it doesn't exist
    src_settings = os.path.join(src_path, 'ProjectSettings')
    dest_settings = os.path.join(dest_path, 'ProjectSettings')
    if not os.path.exists(dest_settings):
        os.makedirs(dest_settings, exist_ok=True)
        shutil.copy2(os.path.join(src_settings, 'EditorBuildSettings.asset'), dest_settings)
        shutil.copy2(os.path.join(src_settings, 'ProjectSettings.asset'), dest_settings)

    # Copy Assets if it doesn't exist
    src_assets = os.path.join(src_path, 'Assets')
    dest_assets = os.path.join(dest_path, 'Assets')
    if not os.path.exists(dest_assets):
        os.makedirs(dest_assets, exist_ok=True)
        shutil.copytree(src_assets, dest_assets)
        
if __name__ == '__main__':
    src_path = "F:\\YDAYS\\UNITY\\AI_WATCHER_2D\\AiWatcher2D"
    dest_path = "F:\\YDAYS\\UNITY\\duplicateProject"
    duplicate_project(src_path, dest_path)