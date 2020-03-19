# from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter
import numpy as np

imp = ImageProcessor()
arr = imp.load("../resources/42AI.png")
print(arr)
# imp.display(arr)

cl = ColorFilter()
inv = cl.celluloid(arr)
print(inv)
imp.display(inv)
