import imageio
import os
import numpy as np

filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))
#filenames=sorted((fn for fn in os.listdir('.') if fn.startswith('anom')))

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
    kwargs = {'fps': 2}
imageio.mimsave('RSD.gif', images, **kwargs)
