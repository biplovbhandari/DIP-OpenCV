"""
    CCP = Camera Calibration Parameters
    
    This file stores the CCP of different digital camera available
    
    Focal length is normally in mm
    K1, K2 and K3: are the radial distortion parameters
    P1 and P2: are the tangential distortion parameters
"""

CCP = {"Trimble UX-5": {"Focal Length": 15.5172, # mm
                        "K1": -0.000202911,
                        "K2": 0.000000681845,
                        "K3": -0.000000000864898,\
                        "P1": -0.0000296516,
                        "P2": -0.000050424,
                        },
       }
