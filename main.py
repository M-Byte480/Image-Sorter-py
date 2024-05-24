import shutil
from datetime import datetime
import os
import sys
import platform

def set_creation_time(dest_path, src_path):
    if platform.system() == 'Windows':

        creation_time = os.path.getctime(src_path)
        # Set the creation time on the destination file
        os.utime(dest_path, (creation_time, creation_time))


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python main.py <absolute_source_folder_root> <absolute_destination_folder_root>")
        exit(1)

    sourceFolderRoot = sys.argv[1]
    destinationFolderRoot = sys.argv[2]

    if not os.path.exists(sourceFolderRoot):
        print("Source folder provided does not exists")
        exit(1)

    if not os.path.exists(destinationFolderRoot):
        os.mkdir(destinationFolderRoot)

    created_dirs = set()


    for (dirPath, subDir, filenames) in os.walk(sourceFolderRoot):
        for filename in filenames:
            filePath = os.path.join(dirPath, filename)

            # Get file object
            try:
                creation_time = os.path.getctime(filePath)
                modified_time = os.path.getmtime(filePath)
            except OSError as e:
                print(f"Error accessing {filePath}: {e}")
                continue

            # Get year and month

            creation_time_object = datetime.fromtimestamp(creation_time)
            modified_time_object = datetime.fromtimestamp(modified_time)

            if creation_time_object.year < modified_time_object.year:
                earlier_time = creation_time_object
            elif creation_time_object.year > modified_time_object.year:
                earlier_time = modified_time_object
            elif creation_time_object.month < modified_time_object.month:
                earlier_time = creation_time_object
            elif creation_time_object.month > modified_time_object.month:
                earlier_time = modified_time_object
            else:
                earlier_time = modified_time_object

            year_str = str(earlier_time.year)
            month_str = f"{earlier_time.month:02d}"

            # Create dirs if not exist
            dest_dir = os.path.join(destinationFolderRoot, year_str, month_str)

            if dest_dir not in created_dirs:
                try:
                    print("Looking for folder " + dest_dir)
                    os.makedirs(dest_dir, exist_ok=True)
                    created_dirs.add(dest_dir)
                except OSError as s:
                    print(f"Error creating directory {dest_dir}: {s}")
                    continue

            dest_file_path = os.path.join(dest_dir, filename)

            try:
                shutil.copy2(filePath, dest_file_path)
                set_creation_time(dest_file_path, filePath)
            except OSError:
                print(f"Error copying {filePath} to {dest_file_path}")



if __name__ == "__main__":
    main()
