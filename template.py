import os


file_dir = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebook",
    "src",
    "saved_model"
]

for dir_ in file_dir:
    #also we have to save gitkeep file in each directory
    os.makedirs(dir_, exist_ok = True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


#we need to create dvc , param.yaml(for parametrs), gitignore(to ingore certain file from uploading into github), init for initialization and readme.md

file_name = [
    "dvc",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py"),
    "README.md"
]

for file in file_name:
    with open(file,"w") as f:
        pass