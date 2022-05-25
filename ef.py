import glob, os
def ffmpeg():
    for filename in glob.glob("./*/*.mkv"):
        folder = filename.split("/")[1]
        file = filename.split("/")[2].split(".")[0]
        os.system(f"mkdir ./{folder}/'{file}' && ffmpeg -hwaccel cuda -i '{filename}' -r 6 ./{folder}/'{file}'/out-%05d.png && mv '{filename}' ~/Downloads/{folder}_storage/")

ffmpeg()