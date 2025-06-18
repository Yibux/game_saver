import zipfile
import os
import shutil

# Ścieżki
zip_path = r'D:\granie steam deck\game_saver\76561199688034403.zip'
extract_path = r"C:\Users\kubas\Documents\Ghost of Tsushima DIRECTOR'S CUT\76561199688034403"

def delete_files_in_folder(folder_path=extract_path):
    """Usuwa wszystkie pliki w podanej ścieżce (nie usuwa folderów)."""
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)

def unpack_zip(zip_path, extract_path):
    """Rozpakowuje plik ZIP do podanej ścieżki."""
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

if __name__ == "__main__":
    # Sprawdzenie, czy plik ZIP istnieje
    if not os.path.exists(zip_path):
        print(f"Plik ZIP nie istnieje: {zip_path}")
    else:
        # Usunięcie plików w folderze docelowym
        delete_files_in_folder()
        print(f"Usunięto pliki w folderze: {extract_path}")

        # Rozpakowanie pliku ZIP
        unpack_zip(zip_path, extract_path)
        print(f"Rozpakowano plik ZIP do: {extract_path}")
