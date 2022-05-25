from PIL import Image
from random import randrange
import glob, os
from multiprocessing.dummy import Pool as ThreadPool


def crop(image):
    img = Image.open(f"{image}")  
    x, y = img.size

    sample = 8

    for i in range(sample):
        matrix = int(min(x,y)*7/8)
        x1 = randrange(0, x - matrix)
        y1 = randrange(0, y - matrix)
        k = img.crop((x1, y1, x1 + matrix, y1 + matrix))
        k = k.resize([256,256])
        k.save(f"L{image.split('/')[1]}/style/{image.split('/')[3].split('.')[0]}-{i}.png", format="png")

def ac(i):
    print(f"starting thread {i}")
    for filename in glob.glob(f"./{i}/style/*"):
        try:
            crop(filename)
        except Exception:
            print(filename)
            continue
    print(f"thread {i} done")

t =[]

for j in range (1,13):
    t.append(j)
    os.system(f"mkdir L{j} && mkdir L{j}/style")

pool = ThreadPool(16)
cropping = pool.map(ac,t)
pool.close()
pool.join()