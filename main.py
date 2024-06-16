import os
import random

random.seed(10)

path = '/Users/matix329/PycharmProjects/Deep lerning/Images'

all_folders = [folder for folder in os.listdir(path) if os.path.isdir(os.path.join(path, folder))]

selected_folders = random.sample(all_folders, 20)

output_file = '/Users/matix329/PycharmProjects/Deep lerning/selected_folders.txt'
with open(output_file, 'w') as file:
    for folder in selected_folders:
        file.write(folder + '\n')

output_file