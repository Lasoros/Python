from pathlib import Path

path = Path("packages_as_scripts")

# path.exists() #returns a boolean
# path.mkdir() #creates directory
# path.rmdir() #removes directory
# path.rename() #renames directory

print(path.iterdir()) #gets list of files and directories in path

# for p in path.iterdir():
#     print(p)

paths = [p for p in path.iterdir()]
print(paths)

#applied filtering

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths, "iterdir")

#path.iterdir() cannot search for patters or recursively
#path.glob() can do the above

py_files = [p for p in path.glob("*.py")]
print(py_files, "glob")

#recersive search .rglob
py_files = [p for p in path.rglob("*.py")]
print(py_files, "rglob")