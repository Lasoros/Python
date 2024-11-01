from pathlib import Path
from time import ctime
import shutil

path = Path("packages_as_scripts/__init__.py")

# path.exists()
# path.rename("init.txt")
# path.unlink()

print(path.stat()) #returns quite a few things, to make readable must import ctime and use as below

print(ctime(path.stat().st_ctime))

print(path.read_text()) #much easier than using open as all happens in function

# path.write_text(". . . .") #used to write textual data to file
# path.write_bytes() #path. is not great for using to copy a file. Use below

source = Path("packages_as_scripts/__init__.py")
target = Path() / "__init__.py"

target.write_text(source.read_text()) #<---- can use this but it is rather clunky to copy file. Can instead use shutil

shutil.copy(source, target) #<--- cleaner and easier to use. Must import shutil to use