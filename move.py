import os
os.system(f"mkdir ~/PaddleGAN/data/animedataset/Love/smooth && mkdir ~/PaddleGAN/data/animedataset/Love/style")
for i in range(1,13):
    os.system(f"mv ~/AnimeGANv2/dataset/L{i}/style/* ~/PaddleGAN/data/animedataset/Love/style && mv ~/AnimeGANv2/dataset/L{i}/smooth/* ~/PaddleGAN/data/animedataset/Love/smooth")
