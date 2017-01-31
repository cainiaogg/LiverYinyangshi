#coding=utf-8
import os
import cv2
import numpy as np

def find_picture(main_picture, pattern_picture):
	main_img = cv2.imread(main_picture)
	pattern_img =  cv2.imread(pattern_picture)
	main_h = main_img.shape[0]
	main_w = main_img.shape[1]
	pattern_h = pattern_img.shape[0]
	pattern_w = pattern_img.shape[1]
	print main_h, main_w, pattern_h, pattern_w
	xx = -1
	yy = -1
	Min = 100000000
	cc = 0
	for x in range(0, main_h - pattern_h + 1):
		for y in range(0, main_w - pattern_w + 1):
			print x, y
			mat = main_img[x: x + pattern_h, y: y + pattern_w:] - pattern_img
			np_sum = np.sum(mat)
			print np_sum
			if np_sum < Min:
				Min = np_sum
				xx = x
				yy = y
	print Min, xx, yy
	cv2.rectangle(main_img, (yy, xx), (yy + pattern_w, xx + pattern_h),(0,0,255))
	cv2.imshow("", main_img)
	cv2.waitKey(1000000)


from PIL import Image

def get_matrix(img):
	h, w = img.size
	img_new = img.convert('1').getdata()
	mat = np.matrix(img_new)
	mat.resize(w, h)
	return mat

def find_picture(main_picture=u'./组队.jpg', pattern_picture=u'./1.jpg'):
	img_main = Image.open(main_picture)
	w, h = img_main.size
	print h, w
	mat_main = get_matrix(img_main)

	img_pattern = Image.open(pattern_picture)
	h_t, w_t = img_pattern.size
	mat_main = get_matrix(img_pattern)
	mat_main.resize(1, h_t * w_t)
	mat_np = np.array(mat_main)

	for x in range(0, h - h_t + 1):
		for y in range(0, w - w_t + 1):


	print mat_main.shape
	# img_mat = Image.fromarray(mat)
	# img_mat.show()

if __name__ == '__main__':
	find_picture()
	dir_path = os.path.realpath(__file__)
	# find_picture(u'./组队.jpg', u'组队.jpg')
