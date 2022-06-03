from PIL import Image
from random import randrange
import glob, os
from multiprocessing.dummy import Pool as ThreadPool


def crop(image):
    img = Image.open(f"{image}")  
    x, y = img.size
    z = min(x,y)
    try:
        assert z >= 256
        matrix = int(z)
        x1 = int((x-z)/2)
        y1 = int((y-z)/2)
        k = img.crop((x1, y1, x1 + matrix, y1 + matrix))
        k = k.resize([256,256],Image.LANCZOS)
        k.save(f"L{image.split('/')[1]}/style/{image.split('/')[3].split('.')[0]}-c.png", format="png")
    except Exception:
        os.system(f"rm -rf {image}")
        pass

def ac(i):
    print(f"starting thread {i}")
    for filename in glob.glob(f"./{i}/style/*"):
        crop(filename)
    print(f"thread {i} done")

t =[]

for j in range (1,13):
    t.append(j)
    os.system(f"mkdir L{j} && mkdir L{j}/style")

pool = ThreadPool(16)
cropping = pool.map(ac,t)
pool.close()
pool.join()