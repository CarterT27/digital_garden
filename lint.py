import os
import pathlib
import re

def add_double_spaces(filepath: pathlib.Path) -> None:
    if os.path.isdir(filepath):
        print(f"{filepath} is not a file")
        return
    with open(filepath, "r") as f:
        lines = f.readlines()
        try:
            frontmatter_start_index = lines.index("---\n")
            frontmatter_end_index = lines.index("---\n", frontmatter_start_index + 1)
        except ValueError:
            print(f"Warning: {filepath} does not have frontmatter")
            frontmatter_start_index = -1
            frontmatter_end_index = -1
        updated_lines = []
        for i, line in enumerate(lines):
            line = line.strip()
            if frontmatter_start_index <= i <= frontmatter_end_index:
                if line == "":
                    pass
                else:
                    updated_lines.append(line)
            elif i == frontmatter_end_index + 1 and line == "":
                try:
                    if lines[i+1].strip() == "":
                        pass
                except IndexError:
                    print(f"{filepath} does not have content after frontmatter.")
            else:
                if line == "":
                    updated_lines.append(line)
                else:
                    updated_lines.append(line + "  ")
    with open(filepath, "w") as f:
        new_lines = [line + "\n" for line in updated_lines]
        f.writelines(new_lines)

if __name__ == "__main__":
    folder = pathlib.Path("content")
    all_files = os.listdir(folder)
    all_files = [folder / file for file in all_files]
    for file in all_files:
        if str(file).endswith('.md'):
            try:
                add_double_spaces(file)
            except Exception as e:
                print(file)
                raise e
