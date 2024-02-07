import os
import pathlib
import re

def add_double_spaces(filename: pathlib.Path) -> None:
    print(filename)
    if os.path.isdir(filename):
        print("Not a file")
        return
    with open(filename, "r") as f:
        lines = f.readlines()
        lines = [line.strip() + "  "
                 if "---" not in line
                 else line.strip()
                 # if line.startswith("> ") 
                 # and not re.match(r"> \[![^\]]+\]", line)
                 # else line.strip()
                 for line in lines]
    with open(filename, "w") as f:
        lines = [line + "\n" for line in lines]
        f.writelines(lines)

if __name__ == "__main__":
    folder = pathlib.Path("content")
    all_files = os.listdir(folder)
    all_files = [folder / file for file in all_files]
    for file in all_files:
        add_double_spaces(file)
