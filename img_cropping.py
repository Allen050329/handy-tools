from PIL import Image
import glob, os


for image in glob.glob(f"Adjusted/*"):
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
        k.save(f"train_photo/{image.split('/')[1].split('.')[0].replace(' ','')}-c.png", format="png")
    except Exception as e:
        print(e)
        pass