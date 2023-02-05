import pandas as pd
import shutil


def get_random_files(n):
    df = pd.read_csv("data.csv")
    train_idx = df[df["split"] == "train"].sample(n=n)["img_index"].to_list()
    val_idx = df[df["split"] == "val"].sample(n=int(n * 0.1))["img_index"].to_list()
    test_idx = df[df["split"] == "test"].sample(n=int(n * 0.1))["img_index"].to_list()

    return train_idx, val_idx, test_idx


def move_random_files(source, destination, n):
    """Move n random files from source to destination"""
    # Get n random files from df
    train_idx, val_idx, test_idx = get_random_files(n)
    # Move files
    for idx in train_idx:
        shutil.move(source + "train/" + idx, destination + "train/" + idx)
    for idx in val_idx:
        shutil.move(source + "val/" + idx, destination + "val/" + idx)
    for idx in test_idx:
        shutil.move(source + "test/" + idx, destination + "test/" + idx)


if __name__ == "__main__":
    move_random_files("images/", "images/exp/", 100)
