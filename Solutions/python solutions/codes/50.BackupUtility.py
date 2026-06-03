import shutil
import os

def main():
    source_dir = "source_folder"
    backup_dir = "backup_folder"
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(backup_dir, exist_ok=True)
    
    with open(os.path.join(source_dir, "test.txt"), "w") as f:
        f.write("test")

    try:
        backed_up_files = set(os.listdir(backup_dir))
        for file in os.listdir(source_dir):
            if file not in backed_up_files:
                shutil.copy(os.path.join(source_dir, file), backup_dir)
                print(f"Backed up {file}")
            else:
                print(f"Skipped {file} (Duplicate)")
    except Exception as e:
        with open("backup.log", "a") as log:
            log.write(f"Error: {e}\n")

if __name__ == "__main__":
    main()
