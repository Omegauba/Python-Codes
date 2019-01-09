# -*- coding: utf-8 -*-
"""
Fast Fourier Tranform for Images

Created on Mon Jan 07 13:28:05 2019

@author: OmegaUba
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\your image', 0)

def low_pass(img, filter_power):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    x_center = int(fshift.shape[0]//2)
    y_center = int(fshift.shape[1]//2)
    radius = int(min(fshift.shape[0], fshift.shape[1]))/filter_power
    for i in range(0, fshift.shape[0]):
        for j in range(0, fshift.shape[1]):
            if np.sqrt((i - x_center)**2 + (j - y_center)**2) > radius:
                fshift[i][j] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    
    return img_back

def high_pass(img, filter_power):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    x_center = int(fshift.shape[0]//2)
    y_center = int(fshift.shape[1]//2)
    radius = int(min(fshift.shape[0], fshift.shape[1]))/filter_power
    for i in range(0, fshift.shape[0]):
        for j in range(0, fshift.shape[1]):
            if np.sqrt((i - x_center)**2 + (j - y_center)**2) < radius:
                fshift[i][j] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    
    return img_back

#this makes the transformation
f = np.fft.fft2(img)
#this makes the  shift so you see 0 freq at center
fshift = np.fft.fftshift(f)
#log has to be applied to appreciate the magnitude
magnitude_spectrum = 20*np.log(np.abs(fshift))
