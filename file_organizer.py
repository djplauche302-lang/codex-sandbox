#!/usr/bin/env python3
"""Organize files in a folder into type-based subfolders."""

from pathlib import Path
import shutil

# File extensions to organize
PDF_EXTENSIONS = {".pdf"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff"}
DOC_EXTENSIONS = {".doc", ".docx", ".txt", ".rtf", ".odt", ".md"}


def get_category(file_path: Path) -> str | None:
    """Return the destination folder name for a file, or None if unknown type."""
    extension = file_path.suffix.lower()

    if extension in PDF_EXTENSIONS:
        return "PDF"
    if extension in IMAGE_EXTENSIONS:
        return "Images"
    if extension in DOC_EXTENSIONS:
        return "Docs"

    return None


def move_file_to_category(file_path: Path, destination_folder: Path) -> None:
    """Move file into the destination folder, avoiding name collisions."""
    destination_folder.mkdir(exist_ok=True)

    target_path = destination_folder / file_path.name
    counter = 1

    while target_path.exists():
        target_path = destination_folder / f"{file_path.stem}_{counter}{file_path.suffix}"
        counter += 1

    shutil.move(str(file_path), str(target_path))


def organize_folder(folder_path: Path) -> None:
    """Organize supported files in a folder by category."""
    if not folder_path.exists() or not folder_path.is_dir():
        print("Error: The folder path does not exist or is not a folder.")
        return

    moved_count = 0

    for item in folder_path.iterdir():
        if not item.is_file():
            continue

        category = get_category(item)
        if category is None:
            continue

        destination = folder_path / category
        move_file_to_category(item, destination)
        moved_count += 1
        print(f"Moved: {item.name} -> {category}/")

    if moved_count == 0:
        print("No supported files were found to organize.")
    else:
        print(f"Done! Organized {moved_count} file(s).")


def main() -> None:
    """Ask the user for a folder path and organize files."""
    print("File Organizer")
    print("This script organizes files into PDF, Images, and Docs folders.")

    folder_input = input("\nEnter the full path of the folder to organize: ").strip()
    folder = Path(folder_input).expanduser()

    organize_folder(folder)


if __name__ == "__main__":
    main()
