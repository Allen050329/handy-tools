import glob, os
i = 0
for filename in glob.glob("*.*"):
    i += 1
    suffix = filename.split('.')[1]
    if suffix != "py":
        os.system(f"mv '{filename}' ./0x{i}.{suffix}")