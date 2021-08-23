from PIL import Image
import pylab
import numpy as np
from scipy.spatial import Delaunay
import heapq

img = Image.open('D:/Download/2297633-kg.jpeg')
img = img.convert('L')
fig, ax = pylab.subplots()
ax.contour(img, origin='image', levels=[100])
pylab.show()
