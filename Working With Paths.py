from pathlib import Path

# Path("C:\\Program Files\\Microsoft") #sometimes names/locations can get long so you can use a "raw string"
#
# Path(r"C:\Program Files\Microsoft") #in a "raw string" \ is not an escape character, it is taken literally as is
# Path("/usr/local/bin") #<--- on linux absolute path
# Path() # <----- path object representing current folder
#
# Path("packages_as_scripts/__init__.py") #<---- navigating to subfolder of path
#
# Path() / Path("packages_as_scripts") #can use the / to combine path objects with other path objects
#
# Path() / "packages_as_scripts" / "__init__.py" # or strings
#
# Path.home() #returns the home directory of the current user

path = Path("packages_as_scripts/__init__.py")

path.exists()
path.is_file()
path.is_dir()

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

path.with_name("file.txt")
print(path.absolute())
path = path.with_suffix(".txt")
print(path)
