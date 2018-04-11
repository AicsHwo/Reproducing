# DEMO

from imp import reload

# 1. resize_images.py
print("1. Demo resize_images.py usage")
import resize_images as rz
reload(rz)
rz.resizeImages(r'./TestData', r'*.JPG')
print("See if tiny gray image were produced")

# 2. npz_save_load_images.py
print("\n2. Demo npz_save_load_images.py usage")
import npz_save_load_images as npz_sl
reload(npz_sl)
npz_sl.saveGrayImagesToNPZ(r'./TestData/out', npz_name = 'npzed_images')
data = npz_sl.loadImagesFromNPZ(r'./TestData/out/npzed_images.npz')
npz_sl.imshow(data[0], "test read data from .npz")
print("See if a .npz file has been created")

# 3. estimate_partial_derivative.py
print("\n3. Demo estimate_partial_derivative.py usage")
import estimate_partial_derivative as estDx
reload(estDx)
estDx.test(r"./TestData/out")
print("See Ix, Iy, and It")

# 4. image_warping.py
print("\n4. Demo image_warping.py usage")
import image_warping as wp
reload(wp)
wp.demo_II(data[0], u = -10, v = 30)
print("See warpped image")
