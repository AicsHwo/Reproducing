import fnmatch
import os.path							# using os.path.isfile()
from PIL import Image

def mkNewFolder(tgtPath):
	# directory = os.path.dirname(filepath)
	directory = tgtPath
	if not os.path.exists(directory):
		os.makedirs(directory)

def resizeImages(inDir, postfix='*.bmp', height=227, width=227, toGray=True):
	# _1stfilePath = path + '0000' + postfix
	# total_files = len([name for name in os.listdir()])
	# Ex. dir = './' , postfix = '*.bmp'
	all_files = fnmatch.filter( os.listdir(inDir), postfix )
	total_files = len( all_files )
	tgtPath = inDir + '\\out\\'
	mkNewFolder( tgtPath )
	print("Tgt path : {}".format(tgtPath))
	i = 0
	for file in all_files:
		img = Image.open( inDir + '\\' + file )
		img = img.resize( (width, height), Image.ANTIALIAS )
		if toGray:
			img = img.convert('LA')
		img.save( tgtPath + "%04d" % i + '.png' )
		i += 1

# Example of usage : 
# shrinkToSmallImages(r' <path> ', '*.bmp')
# 

