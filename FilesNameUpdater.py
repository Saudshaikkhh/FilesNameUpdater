import os

# Set the folder path
folder_path = r"C:\Users\Shaikh Mohammed Saud\Desktop\insta\beautiful_landscapes"

def rename_files_in_folder(folder_path):
    # Get the folder name (use it as the base for filenames)
    folder_name = os.path.basename(folder_path)

    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate through all files in the folder
    for i, file in enumerate(files):
        # Check if it's a file (not a subfolder)
        if os.path.isfile(os.path.join(folder_path, file)):
            # Construct the new filename based on the folder name and index
            new_filename = f"{folder_name}_{i+1}.jpg"
            old_file_path = os.path.join(folder_path, file)
            new_file_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {file} to {new_filename}")

    print(f"Files in folder '{folder_name}' have been renamed.")

def main():
    # Call the rename function with the folder path
    rename_files_in_folder(folder_path)

if __name__ == "__main__":
    main()
