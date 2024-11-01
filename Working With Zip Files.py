from pathlib import Path
from zipfile import ZipFile

# zip = ZipFile("files.zip", "w")
# for path in Path("packages_as_scripts").rglob("*.*"):
#     zip.write(path)
# zip.close()
#
# #can do this cleaner using a with statement
#
with ZipFile("files.zip", "w") as zip:
    for path in Path("packages_as_scripts").rglob("*.*"):
        zip.write(path)
zip.close()

with ZipFile("files.zip") as zip:
    print(zip.namelist()) #namelist returns a list of all the files in zip file
    info = zip.getinfo("packages_as_scripts/sales.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract") #creates new zip, see third gitcommit extract folder