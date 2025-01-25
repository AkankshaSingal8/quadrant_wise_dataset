import os

def rename_folder(folder_path, num):
    try:
        for i in range (len(os.listdir(folder_path))):
            # Get the parent directory of the folder
            parent_dir = os.path.join(folder_path, f"bag{i + 1}")
            
            # Construct the new folder path
            new_folder_path = os.path.join(folder_path, str(i + 1 + num))
            
            # Rename the folder
            os.rename(parent_dir, new_folder_path)
            print(f"Folder renamed: {parent_dir} -> {new_folder_path}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage Example
folder_path = "mix_goal_heights"
rename_folder(folder_path, 0)
