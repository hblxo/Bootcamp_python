from ScrapBooker import ScrapBooker
from ImageProcessor import ImageProcessor
import numpy as np

imp = ImageProcessor()
arr = imp.load("../resources/42AI.png")
print(arr)
# imp.display(arr)

print("---------Crop-------")
sb = ScrapBooker()
slice_arr = sb.crop(arr, (3, 3))
print(slice_arr)

print("---------Thin-------")
arr = np.arange(49).reshape(7, 7)
print(arr)
thin_arr = sb.thin(arr, 3, 1)
print(thin_arr)

print("---------Juxtapose-------")
juxt_arr = sb.juxtapose(arr, 3, axis=1)
imp.display(juxt_arr)

print("---------Mosaic-------")
mos_arr = sb.mosaic(arr, (2, 3))
imp.display(mos_arr)
