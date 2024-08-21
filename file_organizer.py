import os
import shutil
from pathlib import Path

# Define the directory to organize
DIRECTORY_TO_ORGANIZE = Path("C:\\Users\\agrit\\Downloads\\Python\\Dump")

# Define categories and corresponding file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    # "Videos": [".mp4", ".mov", ".avi"],
    # "Music": [".mp3", ".wav", ".aac"],
}

# Create directories for each category
for category in FILE_CATEGORIES:
    category_path = DIRECTORY_TO_ORGANIZE/category
    category_path.mkdir(exist_ok=True)

# Organize files
for file_path in DIRECTORY_TO_ORGANIZE.iterdir():
    if file_path.is_file():
        file_extension = file_path.suffix.lower()
        moved=False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                shutil.move(str(file_path), str(DIRECTORY_TO_ORGANIZE/category/file_path.name))
                print(f'Moved {file_path.name} to {category} folder.')
                moved=True
                break
        if not moved:
            print(f'No category found for {file_path.name}. Leaving it in place.')

print('File organization complete!')