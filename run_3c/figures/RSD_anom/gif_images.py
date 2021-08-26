import imageio
import os

filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))


print filenames

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('run_3_anom.gif', images)
