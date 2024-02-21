import matlab.engine
import numpy as np
import os
import cv2

eng = matlab.engine.start_matlab()
#Get the parent of the script
script_path = os.path.dirname(os.path.abspath(__file__))
eng.cd(script_path, nargout=0)


def capture(get_celsisus=True):
    RGB, THM = eng.capture(nargout=2)
    rgb_img = np.array(RGB, dtype=np.uint8)
    rgb_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
    THM = np.array(THM)
    THM = (THM - 1000.) / 10.
    return rgb_img, THM