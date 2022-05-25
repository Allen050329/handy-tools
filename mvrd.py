#!/usr/bin/python
import random, os
import tqdm, glob

images = glob.glob("style/*")
random.shuffle(images)
for image in tqdm.tqdm(images[:2048]):
    path = image.split("/")
    os.system(f"cp {image} TLove/style/{path[2]}")
    path[1] = "smooth" # I'm lazy lol
    os.system(f"cp {'/'.join(path)} TLove/smooth/{path[2]}")