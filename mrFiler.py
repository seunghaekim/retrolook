import os

cwd = os.getcwd()
target_folder = cwd + "/archive"
cherryField = os.listdir(target_folder)

print(os.path.splitext(cherryField)[-1])
