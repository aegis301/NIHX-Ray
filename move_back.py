import os
import shutil

# move files from images/train to images/, images/val to images/, images/test to images/
def move_files(target):
    # Get all files in images/
    files = os.listdir(f"images/{target}")
    # Move files
    for file in files:
        shutil.move(src=f"images/{target}/" + file, dst="images/" + file)
        print(f"Moved {file} to images/{file}.")


if __name__ == "__main__":
    targets = ["train", "val", "test"]
    for target in targets:
        move_files(target)
