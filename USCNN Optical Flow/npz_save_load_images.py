import numpy as np
import fnmatch
import os.path							# using os.path.isfile()
from PIL import Image

import matplotlib.pyplot as plt

DBG = False

def images2nparray(inDir, all_files):
	allImgs = []
	for file in all_files:
		img = Image.open( inDir + '\\' + file )
		np_img = np.array(img.getdata())[:,0:-1].reshape( (img.size[1], img.size[0]) )
		# using Python list append()
		allImgs.append(np_img)
	if DBG:
		fig, ax = plt.subplots(1,2)
		ax[0].imshow(Image.open( inDir + '\\' + all_files[0] ))
		ax[0].set_xlabel("PIL image")
		ax[1].imshow(allImgs[0])
		ax[1].set_xlabel("Numpy image")
		fig.show()
	# and convert to Numpy array
	return np.array( allImgs )

def saveGrayImagesToNPZ(inDir, postfix='*.png', npz_name = ''):
	# Ex. dir = './' , postfix = '*.png'
	all_files = fnmatch.filter( os.listdir(inDir), postfix )
	total_files = len( all_files )
	print("total {} images".format(total_files))
	npz_name_use = npz_name if len(npz_name) else os.path.basename(os.path.normpath(inDir))
	tgtPNZ = inDir + '\\' + npz_name_use + '.npz'
	data = images2nparray(inDir, all_files)
	print("Storage data shape = {}".format(data.shape))
	np.savez_compressed(tgtPNZ, Data=data)

def loadImagesFromNPZ(inNpzPath):
	loaded = np.load(inNpzPath)
	return loaded['Data']

def imshow(img, suptitle=''):
	fig, ax = plt.subplots(1,1)
	ax.imshow(img)
	# ax.set_xlabel("~")
	fig.suptitle(suptitle)
	fig.show()

# Ex. 
# import npz_save_load_images as npz_sl
# npz_sl.saveGrayImagesToNPZ(r'./out', npz_name = 'test')
# data = npz_sl.loadImagesFromNPZ(r'./out/test.npz')
# npz_sl.imshow(data[0])
