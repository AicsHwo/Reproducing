# Ref. Determine Optical Flow, Berthold K.P. Horn and Brian G. Schunck, MIT

import numpy as np
import matplotlib.pyplot as plt

# - - - - - - - ~ - - - - - - - ~ - - - - - - - 
#                Using Function
# - - - - - - - ~ - - - - - - - ~ - - - - - - - 

def Ex(img):
	# Assume 2 gray image
	assert(img.shape[0] == 2)
	img_k0_i0_j0 = img[0,:-1,:-1]
	img_k0_i0_j1 = img[0,:-1,1:]
	img_k0_i1_j0 = img[0,1:,:-1]
	img_k0_i1_j1 = img[0,1:,1:]
	img_k1_i0_j0 = img[1,:-1,:-1]
	img_k1_i0_j1 = img[1,:-1,1:]
	img_k1_i1_j0 = img[1,1:,:-1]
	img_k1_i1_j1 = img[1,1:,1:]
	return ((img_k0_i0_j1-img_k0_i0_j0) + 
			(img_k0_i1_j1-img_k0_i1_j0) + 
			(img_k1_i0_j1-img_k1_i0_j0) + 
			(img_k1_i1_j1-img_k1_i1_j0))/4.

def Ey(img):
	# Assume 2 gray image
	assert(img.shape[0] == 2)
	img_k0_i0_j0 = img[0,:-1,:-1]
	img_k0_i1_j0 = img[0,1:,:-1]
	img_k0_i0_j1 = img[0,:-1,1:]
	img_k0_i1_j1 = img[0,1:,1:]
	img_k1_i0_j0 = img[1,:-1,:-1]
	img_k1_i1_j0 = img[1,1:,:-1]
	img_k1_i0_j1 = img[1,:-1,1:]
	img_k1_i1_j1 = img[1,1:,1:]
	return ((img_k0_i1_j0-img_k0_i0_j0) + 
			(img_k0_i1_j1-img_k0_i0_j1) + 
			(img_k1_i1_j0-img_k1_i0_j0) + 
			(img_k1_i1_j1-img_k1_i0_j1))/4.

def Et(img):
	# Assume 2 gray image
	assert(img.shape[0] == 2)
	img_k0_i0_j0 = img[0,:-1,:-1]
	img_k1_i0_j0 = img[1,:-1,:-1]
	img_k0_i0_j1 = img[0,:-1,1:]
	img_k1_i0_j1 = img[1,:-1,1:]
	img_k0_i1_j0 = img[0,1:,:-1]
	img_k1_i1_j0 = img[1,1:,:-1]
	img_k0_i1_j1 = img[0,1:,1:]
	img_k1_i1_j1 = img[1,1:,1:]
	return ((img_k1_i0_j0-img_k0_i0_j0) + 
			(img_k1_i0_j1-img_k0_i0_j1) + 
			(img_k1_i1_j0-img_k0_i1_j0) + 
			(img_k1_i1_j1-img_k0_i1_j1))/4.

def EstPartialDerivative(img):
	# Assume 2 gray image
	assert(img.shape[0] == 2)
	# num, height, width = img.shape
	return [Ex(img), Ey(img), Et(img)]


# - - - - - - - ~ - - - - - - - ~ - - - - - - - 
#                  Using Class
# - - - - - - - ~ - - - - - - - ~ - - - - - - - 

class PartialDerivative():
	def __init__(self, img):
		# Assume 2 gray image
		assert(img.shape[0] == 2)
		self.img = img
		self.img_k0_i0_j0 = img[0,:-1,:-1]
		self.img_k1_i0_j0 = img[1,:-1,:-1]
		self.img_k0_i0_j1 = img[0,:-1,1:]
		self.img_k1_i0_j1 = img[1,:-1,1:]
		self.img_k0_i1_j0 = img[0,1:,:-1]
		self.img_k1_i1_j0 = img[1,1:,:-1]
		self.img_k0_i1_j1 = img[0,1:,1:]
		self.img_k1_i1_j1 = img[1,1:,1:]
	def __call__(self):
		return [self.Ix(), self.Iy(), self.It()]
	def Ix(self):
		return ((self.img_k0_i0_j1-self.img_k0_i0_j0) + 
				(self.img_k0_i1_j1-self.img_k0_i1_j0) + 
				(self.img_k1_i0_j1-self.img_k1_i0_j0) + 
				(self.img_k1_i1_j1-self.img_k1_i1_j0))/4.
	def Iy(self):
		return ((self.img_k0_i1_j0-self.img_k0_i0_j0) + 
				(self.img_k0_i1_j1-self.img_k0_i0_j1) + 
				(self.img_k1_i1_j0-self.img_k1_i0_j0) + 
				(self.img_k1_i1_j1-self.img_k1_i0_j1))/4.
	def It(self):
		return ((self.img_k1_i0_j0-self.img_k0_i0_j0) + 
				(self.img_k1_i0_j1-self.img_k0_i0_j1) + 
				(self.img_k1_i1_j0-self.img_k0_i1_j0) + 
				(self.img_k1_i1_j1-self.img_k0_i1_j1))/4.
	def dbg(self):
		dx, dy, dt = self.__call__()

		fig, ax = plt.subplots(1,5)
		ax[0].imshow(self.img[0])
		ax[0].set_xlabel("image t")
		ax[1].imshow(self.img[0])
		ax[1].set_xlabel("image t+1")
		ax[2].imshow(dx)
		ax[2].set_xlabel("Ix")
		ax[3].imshow(dy)
		ax[3].set_xlabel("Iy")
		ax[4].imshow(dt)
		ax[4].set_xlabel("It")
		fig.suptitle("image derivative demo")
		fig.tight_layout()
		fig.show()


def test(inPath):
	from PIL import Image
	img0 = Image.open( inPath + '\\' + '0000.png' )
	np_img0 = np.array(img0.getdata())[:,0:-1].reshape( (img0.size[1], img0.size[0]) )
	img1 = Image.open( inPath + '\\' + '0001.png' )
	np_img1 = np.array(img1.getdata())[:,0:-1].reshape( (img1.size[1], img1.size[0]) )

	calc = PartialDerivative(np.array([np_img0, np_img1]))
	calc.dbg()

# Ex.
# import estimate_partial_derivative as estDx
# estDx.test(r".\out")