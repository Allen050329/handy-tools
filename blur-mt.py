import glob, os
from multiprocessing.dummy import Pool as ThreadPool

def ab(i):
    print(f"starting thread {i}")
    os.system(f"source ~/modeltraining/bin/activate && export PYTHONPATH=$PYTHONPATH:~/AnimeGANv2/tools:~/AnimeGANv2:~/modeltraining/lib/python3.8/site-packages && cd ~/AnimeGANv2/tools && python ~/AnimeGANv2/tools/edge_smooth.py --dataset L{i}")
    print(f"thread {i} done")

t =[]

for j in range (1,13):
    t.append(j)

pool = ThreadPool(12)
blurring = pool.map(ab,t)
pool.close()
pool.join()