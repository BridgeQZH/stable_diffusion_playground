# import numpy as np

# num_imgs = 10
# for i, t in enumerate(np.concatenate([[0], np.linspace(0, 1, num_imgs)])):
#     print(i)
#     print(t)
number_imgs = 125
for i in range(number_imgs):
    src_img_path = "/content/stable_diffusion_playground/selected_imgs/speech/real_speech_{:0>3}.png".format(i)
    print(src_img_path)
    print("finish loading the image_{:0>3}.png".format(i))
# for i in range(125):
#     print(i)