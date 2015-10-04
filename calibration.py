import numpy as np
import cv2
import glob
from CCP import CCP as CCP

images = glob.glob('*.JPG')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Prepare the Distortion Coefficient Matrix
    parameters = CCP["Trimble UX-5"]
    fx = parameters["f"] * parameters["sx"]
    fy = parameters["f"] * parameters["sy"]
    
    row_1 = [fx, 0, parameters["PPx"]]
    row_2 = [0, fy, parameters["PPy"]]
    row_3 = [0, 0, 1]
    cam_mtx = np.array((row_1, row_2, row_3), dtype = float)
    dist = [[parameters["K1"], parameters["K2"], parameters["P1"], parameters["P2"], parameters["K3"]]]
    dist = np.array(dist, dtype = float)
    # Compensate radial and tangential lens distortion and save it
    dst = cv2.undistort(img, cam_mtx, dist)
    cv2.imwrite("%s_calibrated.JPG" % fname, dst)
    