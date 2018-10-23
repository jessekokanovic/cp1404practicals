import shutil
import os


# VERSION 1
# Get to correct directory
os.chdir('FilesToSort_V2')

# Find all the file extensions we need and get what category they go in from the user
extensions = []
category_to_extension = {}

for file in os.listdir('.'):
    try:
        file_extension = file.split(".")[1]
    except IndexError:
        pass
    if file_extension not in extensions:
        extensions.append(file_extension)
for extension in extensions:
    new_category = input("What category would you like to sort {} files in to?".format(extension))
    if new_category in category_to_extension:
        category_to_extension[new_category] = category_to_extension[new_category] + [extension]
    else:
        category_to_extension[new_category] = [extension]

# Make new directories based on these categories
for category in category_to_extension:
    try:
        os.mkdir(category)
    except FileExistsError:
        pass

# # Move files to correct directory
# for filename in os.listdir('.'):
#     if os.path.isdir(filename):
#         continue
#     else:
#         for extension in extensions:
#             if filename.endswith(extension):
#                 shutil.move(filename, extension)
#
