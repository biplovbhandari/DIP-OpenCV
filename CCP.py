"""
    CCP = Camera Calibration Parameters
        - global object

    This file stores the CCP of different digital camera available

    f is normally in mm
    fx and fy: focal length in x and y directions
        fx and fy exists for rectangular image (normal)
        for square pixel size fx=fy=f
    sx and sy: Image Size in x and y direction (pixels per millimeter)
    K1, K2 and K3: are the radial distortion parameters
    P1 and P2: are the tangential distortion parameters
    PPx and PPy: are the Principal point coordinates
"""

CCP = {"Trimble UX-5": {"f": 15.5172, # mm
                        "sx": 4912,
                        "sy": 3264,
                        "K1": -0.000202911,
                        "K2": 0.000000681845,
                        "K3": -0.000000000864898,
                        "P1": -0.0000296516,
                        "P2": -0.000050424,
                        "PPx": 0,
                        "PPy": 0,
                        },
       }
