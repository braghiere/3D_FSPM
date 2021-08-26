from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file('test_run1c_stl.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()

from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

filename = 'test_run1c_stl.stl'

# Create a new plot
figure = pyplot.figure()
axes = figure.gca(projection='3d')

# Load the STL files and add the vectors to the plot
mesh = mesh.Mesh.from_file(filename)

axes.add_collection3d(mplot3d.art3d.Poly3DCollection(mesh.vectors, color='green'))
#axes.plot_surface(mesh.x,mesh.y,mesh.z)
# Auto scale to the mesh size
scale = mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

#turn off grid and axis from display      
#pyplot.axis('off')

#set viewing angle
axes.view_init(azim=120)

# Show the plot to the screen
pyplot.show()


