import numpy as np
import cv2
import glob

images = glob.glob('*.JPG')

for fname in images: 
   if "_calibrated" in fname: # Only process calibrated images
       img = cv2.imread(fname, 0) # 0 - Gives gray scale image
       
       # Non-adaptive histogram equilazation
       #hist_equ = cv2.equalizeHist(img)
       #res = np.hstack((img, hist_equ)) # Stacking images side-by-side
       fname_ = fname.split("_calibrated", 1)
       # CLAHE (Contrast Limited Adaptive Histogram Equalization)
       clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(5,5))
       clahed_img = clahe.apply(img)
       # Apply Adaptive Thresholding
       #aptv_img = cv2.adaptiveThreshold(clahed_img, 255,
       #                                 cv2.ADAPTIVE_THRESH_MEAN_C,
       #                                 cv2.THRESH_BINARY, 5, 0)
       
       cv2.imwrite('%s_histogram.JPG' % fname_[0], clahed_img)
       # Do we need morphological filtering?
       # Atm correction (not now for digital image)?