import glob, os
i = 0
for filename in glob.glob("train_photo/*.*"):
    i += 1
    suffix = filename.split('.')[1]
    os.system(f"mv '{filename}' train_photo/{hex(i)}.{suffix}")