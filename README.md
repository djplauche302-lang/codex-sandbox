# File Organizer (Beginner Friendly)

This project includes a simple Python script that organizes files in a folder by type:

- **PDF** files (`.pdf`) go to a `PDF` folder
- **Image** files (`.jpg`, `.jpeg`, `.png`, etc.) go to an `Images` folder
- **Document** files (`.doc`, `.docx`, `.txt`, etc.) go to a `Docs` folder

---

## 1) Check that Python is installed

Open Terminal (macOS/Linux) or Command Prompt (Windows) and run:

```bash
python --version
```

If that does not work, try:

```bash
python3 --version
```

You should see a version like `Python 3.x.x`.

---

## 2) Save or open this project folder

Make sure `file_organizer.py` is in a folder you can access.

---

## 3) Run the script

In your terminal, move to this project folder:

```bash
cd path/to/this/folder
```

Run:

```bash
python file_organizer.py
```

If needed, use:

```bash
python3 file_organizer.py
```

---

## 4) Enter the folder path to organize

The script will ask:

```text
Enter the full path of the folder to organize:
```

Type the full path to the folder containing your files, then press Enter.

Example:

- Windows: `C:\Users\YourName\Downloads`
- macOS/Linux: `/Users/yourname/Downloads`

---

## 5) What happens next?

The script scans files in that folder and moves supported file types into:

- `PDF/`
- `Images/`
- `Docs/`

Unsupported file types are left unchanged.

---

## Notes

- The script only organizes files in the selected folder (not subfolders).
- If a file with the same name already exists in a destination folder, the script renames the new file (for example `file_1.txt`) to avoid overwriting.
