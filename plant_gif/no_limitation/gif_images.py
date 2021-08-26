import imageio
import os

filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images)
