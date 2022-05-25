import os
for i in range(1,13):
    os.system(f"mkdir ~/AnimeGANv2/dataset/L{i} && mkdir ~/AnimeGANv2/dataset/L{i}/style")
    os.system(f"shuf -zn552 -e L{i}/style/* | xargs -0 cp -t ~/AnimeGANv2/dataset/L{i}/style/ ")
