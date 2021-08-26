import imageio
import os

#filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))

filenames=sorted((fn for fn in os.listdir('/home/renato/groimp_efficient/run_1d/figures/RSD/') if fn.endswith('.png')))

print filenames

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('/home/renato/groimp_efficient/run_1d/figures/RSD/run_1d.gif', images)
