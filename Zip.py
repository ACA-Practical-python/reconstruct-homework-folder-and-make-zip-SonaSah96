import tempfile
import os
import shutil

tem_dr = tempfile.TemporaryDirectory(prefix="Temp", dir=r"C:\Users\User")
os.chdir(r"C:\Users\User\Homework")
for root, directories, files in os.walk("."):
    if all(False for item in root.split("\\") if item.startswith(".g")):
        if files:
            for file in files:
                if file.endswith(".py"):
                    path_for_folder = os.path.join(tem_dr.name, root[2:])
                    if not os.path.exists(path_for_folder):
                        os.makedirs(path_for_folder)
                    path_for_file = os.path.join(root, file)
                    shutil.copy2(path_for_file, path_for_folder)

shutil.make_archive(r"C:\Users\User\Homework", "zip", tem_dr.name)
tem_dr.cleanup()
