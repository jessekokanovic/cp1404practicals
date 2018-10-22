import shutil
import os


# VERSION 1
# Get to correct directory
os.chdir('FilesToSort_V1')

# Find all the file extensions we need and store in a list
extensions = []
for file in os.listdir('.'):
    try:
        file_extension = file.split(".")[1]
    except IndexError:
        pass
    if file_extension not in extensions:
        extensions.append(file_extension)

# Make new directories based on these extensions
for extension in extensions:
    try:
        os.mkdir(extension)
    except FileExistsError:
        pass

# Move files to correct directory
for filename in os.listdir('.'):
    if os.path.isdir(filename):
        continue
    else:
        for extension in extensions:
            if filename.endswith(extension):
                shutil.move(filename, extension)

