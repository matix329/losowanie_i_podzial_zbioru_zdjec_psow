import os
import random
import shutil

selected_folders_path = '/Users/matix329/PycharmProjects/Deep lerning/selected_folders.txt'
with open(selected_folders_path, 'r') as file:
    selected_folders = file.read().splitlines()

base_path = '/Users/matix329/PycharmProjects/Deep lerning/Images'
train_folder_base = '/Users/matix329/PycharmProjects/Deep lerning/train_set'
test_folder_base = '/Users/matix329/PycharmProjects/Deep lerning/test_set'

os.makedirs(train_folder_base, exist_ok=True)
os.makedirs(test_folder_base, exist_ok=True)

for folder in selected_folders:
    folder_path = os.path.join(base_path, folder)
    train_folder = os.path.join(train_folder_base, folder)
    test_folder = os.path.join(test_folder_base, folder)

    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    files = os.listdir(folder_path)

    if len(files) >= 150:
        random.shuffle(files)
        selected_files = files[:150]

        split_point = int(0.6 * 150)
        train_files = selected_files[:split_point]
        test_files = selected_files[split_point:]

        for file in train_files:
            shutil.copy(os.path.join(folder_path, file), os.path.join(train_folder, file))

        for file in test_files:
            shutil.copy(os.path.join(folder_path, file), os.path.join(test_folder, file))
    else:
        print(f"Folder {folder} nie zawiera wystarczającej liczby plików (min. 150).")