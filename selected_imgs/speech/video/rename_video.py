import os

file_path = 'D:\\stable_diffusion_playground\\selected_imgs\\speech\\video'  #当前文件路径
file_index = 0   #文件初始序号
for file in os.listdir(file_path):
    path = os.path.join(file_path,file)
    if os.path.splitext(path)[-1] == '.png':
        new_path = '.'+'/'.join(os.path.splitext(path)[0].split()[:-1])+'/{:0>3}.png'.format(file_index)   #最终文件格式    
        file_index += 1
        os.rename(path, new_path)
