import glob, os
i = 0
for filename in glob.glob("style/*"):
    i += 1
    os.system(f"mv smooth/{filename.split('/')[1]} s/{hex(i)}.{filename.split('/')[1].split('.')[1]}")
    os.system(f"mv {filename} s2/{hex(i)}.{filename.split('/')[1].split('.')[1]}")
