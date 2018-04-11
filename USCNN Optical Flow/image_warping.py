# Warp image using motion(translation)

import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate
interp2d = interpolate.interp2d

class Warp:
	def __init__(self, img):
		assert(len(img.shape) == 2)
		self.img = img
		self.shape = img.shape
		self.height, self.width = img.shape
		gridx = np.arange(0, self.width, 1)
		gridy = np.arange(0, self.height, 1)
		self.f = interp2d(gridx, gridy, self.img)
	def __call__(self, u, v):
		'''Warp image using meshgrid-like location (u,v)'''
		assert( (u.shape == self.shape) and (v.shape == self.shape) )
		warped_img = [[ self.f(u[i][j], v[i][j]) for j in range(self.width) ] for i in range(self.height)]
		return np.squeeze(np.array( warped_img ))

def demo():
	test_img = np.array([[0,1,2,3,4,5,6], [7,8,9,10,11,12,13], [14,15,16,17,18,19,20]])
	print("Test image for demo : \n{}".format( test_img ))
	# >> Demo use of Warp class
	warpper = Warp(test_img)
	tmpx = np.arange(0, test_img.shape[1], 1)
	tmpy = np.arange(0, test_img.shape[0], 1)
	x, y = np.meshgrid(tmpx, tmpy)
	print("Before wrapping : \n{}".format( warpper(x,y) ))
	# >> Demo use of motion (u,v)
	u = np.ones( (test_img.shape) ) * -0.5
	v = np.zeros( (test_img.shape) )
	print("After wrapping : \n{}\n u : \n{}\n v : \n{}".format( warpper(x+u,y+v), u, v ))

	u = np.ones( (test_img.shape) ) * 1.5
	v = np.ones( (test_img.shape) ) * -1
	print("After wrapping : \n{}\n u : \n{}\n v : \n{}".format( warpper(x+u,y+v), u, v ))

	u = np.ones( (test_img.shape) ) * 1.5
	v = np.ones( (test_img.shape) ) * 1
	print("After wrapping : \n{}\n u : \n{}\n v : \n{}".format( warpper(x+u,y+v), u, v ))


def demo_II(test_img, u, v):
	warpper = Warp(test_img)
	tmpx = np.arange(0, test_img.shape[1], 1)
	tmpy = np.arange(0, test_img.shape[0], 1)
	x, y = np.meshgrid(tmpx, tmpy)
	uu = np.ones( (test_img.shape) ) * u
	vv = np.ones( (test_img.shape) ) * v
	
	fig, ax = plt.subplots(1,2)
	ax[0].imshow(test_img)
	ax[0].set_xlabel("original image")
	ax[1].imshow(warpper(x+uu,y+vv))
	ax[1].set_xlabel("image warpped using (u,v) = ({},{})".format(u,v))
	fig.suptitle("image warping demo II")
	fig.tight_layout()
	fig.show()