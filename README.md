# FilesNameUpdater

## Description
**FilesNameUpdater** is a simple Python script designed to rename all files in a specified folder. The script uses the folder's name as a prefix and assigns sequential numbers to the files (e.g., `foldername_1.jpg`, `foldername_2.jpg`, etc.). This is particularly useful for organizing large collections of files such as images, media, or datasets, ensuring a consistent and structured naming convention.

---

## Features
- Renames all files in a specified folder using a standardized format.
- Automatically adds a sequential index to each file name.
- Ignores subfolders, processing only files within the folder.
- Provides a log of renamed files for easy tracking.

---

## How It Works
1. The script takes the folder path as an input.
2. Retrieves the folder name and lists all files in the directory.
3. Renames each file in sequence, using the format `<folder_name>_<index>.jpg`.
4. Prints a log of all renamed files in the console.

---

## Setup
1. Ensure you have Python installed on your system.
2. Place the script file (`FilesNameUpdater.py`) in a desired location.

---

## Usage
1. Update the `folder_path` variable in the script with the absolute path of your target folder:
```python
   folder_path = r"C:\path\to\your\folder"
```
2. Run the script:
```bash
python FilesNameUpdater.py
```
3. The files in the folder will be renamed, and the changes will be displayed in the console.


## Example
Assume the folder is named beautiful_landscapes and contains:
- `IMG001.jpg`
- `IMG002.jpg`
- `IMG003.jpg`
After running the script, the files will be renamed to:
- `beautiful_landscapes_1.jpg`
- `beautiful_landscapes_2.jpg`
- `beautiful_landscapes_3.jpg`

## Notes
- Only files in the specified folder are renamed; subfolders are ignored.
- Ensure you have the necessary permissions to modify files in the target folder.

## License
This script is open-source and free to use.




