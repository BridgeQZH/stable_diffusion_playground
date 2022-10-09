import numpy as np

num_imgs = 10
for i, t in enumerate(np.concatenate([[0], np.linspace(0, 1, num_imgs)])):
    print(i)
    print(t)