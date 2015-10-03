import cv2
print cv2.__version__

CCP = {"Trimble UX-5": {"Focal Length": 15.5172, # Focal Length in mm
                        # K1, K2 and K3 are radial distortion parameters
                        "K1": -0.000202911,
                        "K2": 0.000000681845,
                        "K3": -0.000000000864898,
                        # P1 and P2 are tangential distortion parameters
                        "P1": -0.0000296516,
                        "P2": -0.000050424,
                        },
       }