import os
import shutil
import zipfile
import subprocess

def zip_directory(source_dir, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_dir):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, source_dir)
                zipf.write(abs_path, rel_path)
    print(f"Created zip file: {zip_name}")

def copy_file(src, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    dest = shutil.copy(src, dest_dir)
    print(f"Copied to: {dest}")
    return dest

def git_commit_and_push(repo_dir, file_to_commit, commit_message="Add zipped file"):
    os.chdir(repo_dir)
    subprocess.run(["git", "add", file_to_commit], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Committed and pushed to repository.")

if __name__ == '__main__':
    # === USER INPUT SECTION ===
    source_dir = "/home/deck/.local/share/Steam/steamapps/compatdata/2215430/pfx/drive_c/users/steamuser/My Documents/Ghost of Tsushima DIRECTOR'S CUT/76561199688034403/"
    zip_file_path = "/home/deck/.local/share/Steam/steamapps/compatdata/2215430/pfx/drive_c/users/steamuser/My Documents/Ghost of Tsushima DIRECTOR'S CUT/76561199688034403.zip"
    destination_dir = "/home/deck/Desktop/game_saver/"
    repo_dir = "/path/to/repo"
    relative_path_in_repo = os.path.relpath(os.path.join(destination_dir, os.path.basename(zip_file_path)), repo_dir)

    # === MAIN EXECUTION ===
    zip_directory(source_dir, zip_file_path)
    copied_file = copy_file(zip_file_path, destination_dir)
    # git_commit_and_push(repo_dir, relative_path_in_repo)
