import glob, os
i = 0
for filename in glob.glob("./*.png"):
    if i < 7000:
        folder = filename.split("/")[1]
        file = filename.split("/")[2]
        os.system(f"mv {filename} ../../train/real{file}")
        i += 1
    else:
        exit(0)